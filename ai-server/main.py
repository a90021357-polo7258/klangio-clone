import os
# Force CPU usage for TensorFlow to avoid GPU OOM or initialization errors
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import librosa
import numpy as np
import tempfile
from pathlib import Path
import yt_dlp
import shutil
import glob
import logging
import tensorflow as tf
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import music21
from music21 import converter, note, stream, metadata, percussion, clef

# Configure logging
logging.basicConfig(
    filename='server_error.log', 
    level=logging.ERROR, 
    format='%(asctime)s %(levelname)s: %(message)s'
)

app = FastAPI(
    title="Melodify AI Server",
    description="AI-powered audio to sheet music conversion for Melodify",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://klangio-clone.vercel.app",
        "https://klangio-clone-*.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def configure_ffmpeg():
    """Find FFmpeg in Winget packages and add to PATH if not found"""
    if shutil.which("ffmpeg"):
        return None

    print("FFmpeg not found in PATH. Searching in Winget directory...")
    user_home = os.path.expanduser("~")
    winget_path = os.path.join(user_home, "AppData", "Local", "Microsoft", "WinGet", "Packages")
    
    # Search patterns for generic version matching
    patterns = [
        os.path.join(os.getcwd(), "ffmpeg.exe"), # Priority: Local file
        os.path.join(winget_path, "Gyan.FFmpeg*", "ffmpeg*", "bin"),
        os.path.join(winget_path, "Gyan.FFmpeg*", "bin"),
    ]
    
    for pattern in patterns:
        if pattern.endswith("ffmpeg.exe"):
            found = [pattern] if os.path.exists(pattern) else []
            is_file = True
        else:
            found = glob.glob(pattern)
            is_file = False
            
        if found:
            ffmpeg_path = found[0]
            print(f"Found FFmpeg at: {ffmpeg_path}")
            
            # Add to PATH for librosa/audioread
            ffmpeg_dir = os.path.dirname(ffmpeg_path) if is_file else ffmpeg_path
            os.environ["PATH"] += os.pathsep + ffmpeg_dir
            return ffmpeg_dir # Return DIRECTORY for usage in PATH-like additions checks, but yt-dlp might want exe?
            # yt-dlp ffmpeg_location can be exe or dir. Let's return the EXE path if possible or dir.
            # Actually, standardizing on returning the DIRECTORY is safer for PATH and yt-dlp binary search.
            return ffmpeg_dir
            
    print("FFmpeg not found in Winget directory or local build.")
    return None

# Configure FFmpeg on startup
FFMPEG_DIR = configure_ffmpeg()

# Global Model Loading (Lazy but shared)
BASIC_PITCH_MODEL = None

def get_basic_pitch_model():
    global BASIC_PITCH_MODEL
    if BASIC_PITCH_MODEL is None:
        print("Loading Basic Pitch model...")
        try:
            from basic_pitch.inference import predict
            # Just import is enough for now, real model load happens on first predict usually
            # But we can try to force load if needed.
            # actually basic_pitch loads model on demand inside predict. 
            # We can't easily pre-load unless we dig into the library.
            # But importing tensorflow here helps.
            import tensorflow as tf
            BASIC_PITCH_MODEL = True
            print("Basic Pitch requirements loaded.")
        except Exception as e:
            print(f"Failed to load Basic Pitch requirements: {e}")
    return BASIC_PITCH_MODEL

class YoutubeRequest(BaseModel):
    url: str
    instrument: str = "piano"

@app.get("/")
async def root():
    """서버 상태 확인"""
    return {
        "message": "Melodify AI Server",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    """헬스 체크"""
    return {"status": "healthy"}

def sanitize_filename(filename: str) -> str:
    """Windows 호환 파일명으로 변환"""
    import re
    # 윈도우 금지 문자 제거: < > : " / \ | ? *
    return re.sub(r'[<>:"/\\|?*]', '', filename).strip()

async def process_audio_file(file_path: str, original_filename: str, instrument: str = "piano"):
    """
    공통 오디오 분석 로직
    instrument: 'piano', 'guitar', 'vocal', 'drum' 등
    """
    try:
        # Sanitize filename for internal use
        safe_filename = sanitize_filename(original_filename)
        print(f"Processing {original_filename} (safe: {safe_filename}) for instrument: {instrument}")
        
        # 오디오 로드
        # duration=30: 처음 30초만 분석 (무료 티어 제한 시뮬레이션)
        y, sr = librosa.load(file_path, sr=22050, duration=30)
        
        # 템포 감지
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        
        # 악기별 피치 감지 설정
        fmin = librosa.note_to_hz('C2')
        fmax = librosa.note_to_hz('C7')
        
        if instrument == 'guitar':
            fmin = librosa.note_to_hz('E2')
            fmax = librosa.note_to_hz('E6')
        elif instrument == 'bass':
            fmin = librosa.note_to_hz('E1')
            fmax = librosa.note_to_hz('G4')
        elif instrument == 'violin':
            fmin = librosa.note_to_hz('G3')
            fmax = librosa.note_to_hz('A7')
        elif instrument == 'wind':
            fmin = librosa.note_to_hz('C3')
            fmax = librosa.note_to_hz('C7')
        
        # Vocal & Wind Implementation with pYIN (Monophonic)
        if instrument == 'vocal' or instrument == 'wind':
            def log_to_file(msg):
                with open("debug_vocal.log", "a", encoding="utf-8") as f:
                    import datetime
                    f.write(f"{datetime.datetime.now()}: {msg}\n")
            
            try:
                log_to_file(f"Starting {instrument} Analysis for {original_filename}")
                print(f"Starting {instrument} Analysis for {original_filename} using pYIN...")
                
                # pYIN Pitch Tracking
                fmin_vocal = fmin
                fmax_vocal = fmax
                
                log_to_file(f"Running librosa.pyin... (sr={sr}, duration={len(y)/sr:.2f}s)")
                
                # Frame size for high resolution
                f0, voiced_flag, voiced_probs = librosa.pyin(
                    y, 
                    fmin=fmin_vocal, 
                    fmax=fmax_vocal, 
                    sr=sr,
                    frame_length=2048,
                    hop_length=512
                )
                
                n_frames = len(f0)
                n_voiced = np.sum(voiced_flag)
                log_to_file(f"pYIN Analysis done. Frames: {n_frames}, Voiced: {n_voiced}")
                
                if n_voiced == 0:
                     log_to_file("WARNING: No voiced frames detected!")
                
                unique_notes = []
                current_midi = None
                start_time = 0.0
                times = librosa.times_like(f0, sr=sr, hop_length=512)
                
                for i, (pitch, voiced) in enumerate(zip(f0, voiced_flag)):
                    if voiced and not np.isnan(pitch):
                        midi_val = int(round(librosa.hz_to_midi(pitch)))
                        
                        if current_midi is None:
                            # Note Start
                            current_midi = midi_val
                            start_time = times[i]
                        elif current_midi != midi_val:
                            # Note Change
                            end_time = times[i]
                            duration = end_time - start_time
                            if duration >= 0.1: # Min duration 100ms
                                unique_notes.append({
                                    'time': float(start_time),
                                    'note': librosa.midi_to_note(current_midi),
                                    'frequency': float(librosa.midi_to_hz(current_midi)),
                                    'duration': float(duration),
                                    'velocity': 100.0
                                })
                            current_midi = midi_val
                            start_time = times[i]
                    else:
                        # Silence / Unvoiced
                        if current_midi is not None:
                            # Note End
                            end_time = times[i]
                            duration = end_time - start_time
                            if duration >= 0.1:
                                unique_notes.append({
                                    'time': float(start_time),
                                    'note': librosa.midi_to_note(current_midi),
                                    'frequency': float(librosa.midi_to_hz(current_midi)),
                                    'duration': float(duration),
                                    'velocity': 100.0
                                })
                            current_midi = None
                            
                # Handle last note if file ends while voiced
                if current_midi is not None:
                    end_time = times[-1]
                    duration = end_time - start_time
                    if duration >= 0.1:
                        unique_notes.append({
                            'time': float(start_time),
                            'note': librosa.midi_to_note(current_midi),
                            'frequency': float(librosa.midi_to_hz(current_midi)),
                            'duration': float(duration),
                            'velocity': 100.0
                        })

                # Music21 Generation (Lead Sheet)
                s = stream.Score()
                p = stream.Part()
                p.insert(0, metadata.Metadata())
                p.metadata.title = original_filename
                p.metadata.composer = "Melodify AI (Vocal)"
                
                for n_data in unique_notes:
                    m21_note = music21.note.Note(n_data['note'])
                    # Quarter Length approximation (assuming 120 BPM for now, or use detected tempo)
                    # Duration in seconds * (BPM / 60) = Quarter Lengths
                    ql = n_data['duration'] * (tempo / 60.0)
                    m21_note.quarterLength = round(ql * 4) / 4.0
                    if m21_note.quarterLength == 0: m21_note.quarterLength = 0.25
                    p.append(m21_note)
                    
                s.insert(0, p)
                
                # MIDI & XML Generation
                import base64
                
                # 1. MIDI
                midi_filename = f"{safe_filename}.mid"
                midi_path = os.path.join(os.path.dirname(file_path), midi_filename)
                
                # Write MIDI using Music21 or PrettyMIDI? 
                # Music21 write('midi') sometimes buggy, let's use PrettyMIDI for consistency or Music21 if simple.
                # Let's use Music21 write('midi') since we have the Score object ready.
                s.write('midi', fp=midi_path)
                
                with open(midi_path, "rb") as f:
                    midi_base64 = base64.b64encode(f.read()).decode('utf-8')
                    
                # 2. XML
                xml_filename = f"{safe_filename}.xml"
                xml_path = os.path.join(os.path.dirname(file_path), xml_filename)
                s.write('musicxml', fp=xml_path)
                with open(xml_path, "rb") as f:
                    xml_base64 = base64.b64encode(f.read()).decode('utf-8')
                
                if os.path.exists(midi_path): os.remove(midi_path)
                if os.path.exists(xml_path): os.remove(xml_path)

                return {
                    "success": True,
                    "data": {
                        "fileName": original_filename,
                        "duration": float(len(y) / sr),
                        "tempo": float(tempo),
                        "instrument": instrument,
                        "notes_count": len(unique_notes),
                        "notes": unique_notes[:200],
                        "sample_rate": sr,
                        "midi_base64": midi_base64,
                        "xml_base64": xml_base64,
                        "message": f"{instrument.capitalize()} 모드: pYIN 단선율 분석 완료!"
                    }
                }

            except Exception as e:
                import traceback
                tb = traceback.format_exc()
                log_to_file(f"Vocal Analysis Exception: {e}\n{tb}")
                print(f"Vocal Analysis failed: {e}")
                # Fallback to default
                pass 

        # Drum Implementation with Onset Detection & Spectral Classification
        if instrument == 'drum':
             try:
                print(f"Starting Drum Analysis for {original_filename}...")
                
                # Spectral Centroid for classification
                spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
                onset_env = librosa.onset.onset_strength(y=y, sr=sr)
                onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
                onset_times = librosa.frames_to_time(onset_frames, sr=sr)
                
                unique_notes = []
                
                # Heuristic mapping
                # Kick (36): Low freq, High energy
                # Snare (38): Mid freq, Noise
                # Hi-Hat (42): High freq
                
                for i, frame in enumerate(onset_frames):
                    # Analyze local spectral centroid around the onset
                    # Window: -2 to +2 frames
                    start_f = max(0, frame - 2)
                    end_f = min(len(spectral_centroid), frame + 2)
                    local_centroid = np.mean(spectral_centroid[start_f:end_f])
                    
                    # Classification Logic
                    midi_note = 38 # Default to Snare
                    note_name = "Snare"
                    
                    if local_centroid < 1200:
                        midi_note = 36 # Kick (Bass Drum 1)
                        note_name = "Kick"
                    elif local_centroid > 4500:
                        midi_note = 42 # Closed Hi-Hat
                        note_name = "Hi-Hat"
                    
                    unique_notes.append({
                        'time': float(onset_times[i]),
                        'note': note_name, # Display name
                        'midi': midi_note, # Helper for creating MIDI
                        'frequency': float(local_centroid), # Just for reference
                        'duration': 0.1, # Drums are one-shot
                        'velocity': 100.0
                    })
                
                print(f"Drum Analysis done. Found {len(unique_notes)} beats.")

                # Music21 Generation (Percussion)
                s = stream.Score()
                p = stream.Part()
                p.insert(0, metadata.Metadata())
                p.metadata.title = original_filename
                p.metadata.composer = "Melodify AI (Drum)"
                
                # Use Percussion Clef? Music21 support is varied, let's use Treble but map correctly in MIDI
                # Or try to construct a drum staff.
                # For output simplicity:
                
                # Use a specific Unpitched object or Note with special head?
                # For MusicXML compatibility, simple Notes mapped to lines with PercussionClef is best.
                p.clef = clef.PercussionClef()
                
                for n_data in unique_notes:
                    # Map to specific lines/spaces for visualization?
                    # Kick: F4 (Space 1), Snare: C5 (Space 3), Hi-Hat: G5 (Space 5/Above) - roughly
                    # Standard Drum Map in notation:
                    # Kick: F4 or E4
                    # Snare: C5
                    # HiHat: G5 (X head)
                    
                    display_pitch = "C5" # Snare default
                    notehead = "normal"
                    
                    if n_data['midi'] == 36: # Kick
                        display_pitch = "F4"
                    elif n_data['midi'] == 42: # Hi-Hat
                        display_pitch = "G5"
                        notehead = "x"
                        
                    m21_note = music21.note.Note(display_pitch)
                    m21_note.notehead = notehead
                    m21_note.quarterLength = 0.25 # 16th note default
                    
                    # Insert at absolute offset? 
                    # Music21 stream append logic is relative. 
                    # We need to calculate rests or use absolute insert (insert(offset, obj))
                    # insert is better for uneven rhythms
                    
                    # Convert seconds to quarterLength (assuming 120 BPM = 0.5s per beat, 1 ql)
                    # onset / (60/120) = onset * 2
                    offset = n_data['time'] * (tempo / 60.0)
                    p.insert(offset, m21_note)

                s.insert(0, p)
                
                # MIDI Generation using PrettyMIDI (Better for Drums channel 10)
                import pretty_midi
                pm = pretty_midi.PrettyMIDI()
                # Program 0 is fine, but is_drum=True is key
                inst = pretty_midi.Instrument(program=0, is_drum=True)
                
                for n_data in unique_notes:
                    pm_note = pretty_midi.Note(
                        velocity=100, 
                        pitch=n_data['midi'], 
                        start=n_data['time'], 
                        end=n_data['time'] + 0.1
                    )
                    inst.notes.append(pm_note)
                
                pm.instruments.append(inst)
                
                # Files
                import base64
                
                # 1. MIDI
                midi_filename = f"{safe_filename}.mid"
                midi_path = os.path.join(os.path.dirname(file_path), midi_filename)
                pm.write(midi_path)
                
                with open(midi_path, "rb") as f:
                    midi_base64 = base64.b64encode(f.read()).decode('utf-8')
                    
                # 2. XML
                xml_filename = f"{safe_filename}.xml"
                xml_path = os.path.join(os.path.dirname(file_path), xml_filename)
                s.write('musicxml', fp=xml_path)
                with open(xml_path, "rb") as f:
                    xml_base64 = base64.b64encode(f.read()).decode('utf-8')
                
                if os.path.exists(midi_path): os.remove(midi_path)
                if os.path.exists(xml_path): os.remove(xml_path)

                return {
                    "success": True,
                    "data": {
                        "fileName": original_filename,
                        "duration": float(len(y) / sr),
                        "tempo": float(tempo),
                        "instrument": instrument,
                        "notes_count": len(unique_notes),
                        "notes": unique_notes[:200],
                        "sample_rate": sr,
                        "midi_base64": midi_base64,
                        "xml_base64": xml_base64,
                        "message": f"Drum 모드: 리듬 분석 및 3-Part(Kick/Snare/HH) 분류 완료!"
                    }
                }
             except Exception as e:
                print(f"Drum Analysis failed: {e}")
                logging.error(f"Drum Analysis Failed: {e}", exc_info=True)
                pass
        if instrument == 'piano' or instrument == 'violin':
            try:
                print(f"Using Basic Pitch for {original_filename}...")
                
                # Predict (CPU analysis might be slow)
                model_output, midi_data, note_events = predict(
                    file_path,
                    onset_threshold=0.5,
                    frame_threshold=0.3
                )
                
                # Convert Basic Pitch events to our format
                # note_events: list of (start_time, end_time, pitch_midi, amplitude, onsets)
                unique_notes = []
                for start, end, pitch, amplitude, _ in note_events:
                    # MIDI to Note Name
                    note_name = librosa.midi_to_note(pitch)
                    freq = librosa.note_to_hz(note_name)
                    
                    # Hand Separation (Middle C = C4 = MIDI 60)
                    hand = 'right' if pitch >= 60 else 'left'
                    
                    unique_notes.append({
                        'time': float(start),
                        'note': note_name,
                        'frequency': float(freq),
                        'hand': hand,
                        'duration': float(end - start),
                        'velocity': float(amplitude)
                    })
                
                # 시간순 정렬
                unique_notes.sort(key=lambda x: x['time'])
                
                # MIDI & MusicXML Generation
                import base64
                from music21 import converter
                
                # 1. MIDI Save & Base64
                midi_filename = f"{original_filename}.mid"
                midi_path = os.path.join(os.path.dirname(file_path), midi_filename)
                midi_data.write(midi_path)
                
                with open(midi_path, "rb") as f:
                    midi_base64 = base64.b64encode(f.read()).decode('utf-8')
                
                # 2. MusicXML Conversion & Base64
                xml_filename = f"{original_filename}.xml"
                xml_path = os.path.join(os.path.dirname(file_path), xml_filename)
                
                try:
                    # Parse MIDI with music21 and write to XML
                    score = converter.parse(midi_path)
                    score.write('musicxml', fp=xml_path)
                    
                    with open(xml_path, "rb") as f:
                        xml_base64 = base64.b64encode(f.read()).decode('utf-8')
                except Exception as e:
                    print(f"MusicXML conversion failed: {e}")
                    xml_base64 = None
                
                # Clean up temp files
                if os.path.exists(midi_path): os.remove(midi_path)
                if os.path.exists(xml_path): os.remove(xml_path)

                return {
                    "success": True,
                    "data": {
                        "fileName": original_filename,
                        "duration": float(len(y) / sr), 
                        "tempo": float(tempo),
                        "instrument": instrument,
                        "notes_count": len(unique_notes),
                        "notes": unique_notes[:200], 
                        "sample_rate": sr,
                        "midi_base64": midi_base64,
                        "xml_base64": xml_base64,
                        "message": f"{instrument} 모드: Basic Pitch 다성 분석 완료! (양손 분리됨)"
                    }
                }
                
            except Exception as e:
                print(f"Basic Pitch failed, falling back to Librosa: {e}")
                # Fallthrough to default Librosa logic


        # Guitar Implementation with Basic Pitch
        if instrument == 'guitar':
            try:
                print(f"Starting Guitar Analysis for {original_filename}...")
                
                print(f"Starting Guitar Analysis for {original_filename}...")
                
                # Limit GPU memory growth to prevent OOM
                gpus = tf.config.experimental.list_physical_devices('GPU')
                if gpus:
                    try:
                        for gpu in gpus:
                            tf.config.experimental.set_memory_growth(gpu, True)
                    except RuntimeError as e:
                        print(e)
                
                print(f"Predicting...")
                
                print(f"Predicting with high sensitivity...")
                
                # Predict
                try:
                    model_output, midi_data, note_events = predict(
                        file_path,
                        onset_threshold=0.4, # Lowered from 0.5 (More sensitive)
                        frame_threshold=0.2, # Lowered from 0.3 (More sensitive to sustain)
                        minimum_note_length=50, 
                        minimum_frequency=None,
                        maximum_frequency=None
                    )
                except ValueError as ve:
                    # Handle "zero-size array" error when no notes are found
                    print(f"Basic Pitch found no notes: {ve}")
                    # Create empty data to prevent crash
                    import pretty_midi
                    midi_data = pretty_midi.PrettyMIDI()
                    note_events = []
                    
                print(f"Prediction done. Note events: {len(note_events)}")
                
                if len(note_events) == 0:
                     print("Warning: No notes detected by Basic Pitch.")
                     # We can choose to raise exception to trigger Librosa fallback, 
                     # OR just return empty result. 
                     # Let's raise to trigger Librosa fallback as it might find *something* (monophonic)
                     raise ValueError("No notes detected by Basic Pitch")

                # Create Music21 Stream for TAB
                s = stream.Score()
                p = stream.Part()
                p.insert(0, metadata.Metadata())
                p.metadata.title = original_filename
                p.metadata.composer = "Melodify AI"
                
                # ... rest of logic ...
                    
                    # ... rest of music21 logic ...
                
                # Setup Guitar Staff and Tablature
                # music21 doesn't have a direct 'Tablature' stream class that renders easily to XML in all readers,
                # but we can simulate it or use specific notation.
                # However, for simple XML export, providing correct pitch is priority.
                # Standard Tuning: E2, A2, D3, G3, B3, E4
                
                # Helper to find best string/fret
                guitar_tuning = {
                    1: 64, # E4 (High E) - String 1
                    2: 59, # B3 - String 2
                    3: 55, # G3 - String 3
                    4: 50, # D3 - String 4
                    5: 45, # A2 - String 5
                    6: 40  # E2 (Low E) - String 6
                }
                
                def get_best_fret(midi_val):
                    # Greedy approach: prefer lower frets, prefer open strings
                    best_string = 6
                    best_fret = 0
                    min_score = 1000
                    
                    for string_num, open_midi in guitar_tuning.items():
                        fret = midi_val - open_midi
                        if 0 <= fret <= 24: # Valid fret range
                            # Score calculation (lower is better)
                            score = fret * 2  # Higher frets cost more
                            if fret == 0: score = 0 # Open string is best
                            
                            if score < min_score:
                                min_score = score
                                best_string = string_num
                                best_fret = fret
                                
                    return best_string, best_fret

                measure_notes = []
                current_measure_idx = 0
                unique_notes = []  # Initialize list to fix UnboundLocalError
                
                # Convert Basic Pitch notes to Music21 objects with TAB data
                # basic_pitch outputs midi_data (PrettyMIDI object) which is easier to iterate
                for pm_note in midi_data.instruments[0].notes:
                    m21_note = note.Note()
                    m21_note.pitch.midi = pm_note.pitch
                    
                    # Quantize duration to avoid "inexpressible durations" error
                    # Rounding to nearest 0.125 (32nd note) usually works for XML export
                    duration_val = (pm_note.end - pm_note.start) * 2
                    # Ensure minimum duration
                    if duration_val < 0.125: duration_val = 0.125
                    
                    # Round to reasonable fraction
                    from fractions import Fraction
                    # Simple quantization: round to nearest 0.25 (16th note) or keep as float if supported?
                    # Music21 usually handles floats, but extremely odd ones break XML.
                    # Best approach: use quarterLength as float but rounded.
                    m21_note.quarterLength = round(duration_val * 4) / 4.0 
                    if m21_note.quarterLength == 0: m21_note.quarterLength = 0.25
                    
                    # Add simple Tablature annotation (text for now as full XML TAB is complex)
                    string_num, fret_num = get_best_fret(pm_note.pitch)
                    m21_note.addLyric(f"Str:{string_num}")
                    m21_note.addLyric(f"Fret:{fret_num}")
                    
                    # Store for JSON response
                    unique_notes.append({
                        'time': float(pm_note.start),
                        'note': librosa.midi_to_note(pm_note.pitch),
                        'frequency': float(librosa.note_to_hz(librosa.midi_to_note(pm_note.pitch))),
                        'string': string_num,
                        'fret': fret_num,
                        'duration': float(pm_note.end - pm_note.start),
                        'velocity': float(pm_note.velocity)
                    })
                    
                    p.append(m21_note)
                
                s.insert(0, p)
                
                # Make simple list for frontend
                unique_notes.sort(key=lambda x: x['time'])

                # MIDI & XML Generation
                import base64
                
                # 1. MIDI
                midi_filename = f"{safe_filename}.mid"
                midi_path = os.path.join(os.path.dirname(file_path), midi_filename)
                midi_data.write(midi_path)
                with open(midi_path, "rb") as f:
                    midi_base64 = base64.b64encode(f.read()).decode('utf-8')
                    
                # 2. XML (with Fret data if possible, or standard notation)
                xml_filename = f"{safe_filename}.xml"
                xml_path = os.path.join(os.path.dirname(file_path), xml_filename)
                s.write('musicxml', fp=xml_path)
                with open(xml_path, "rb") as f:
                    xml_base64 = base64.b64encode(f.read()).decode('utf-8')
                
                if os.path.exists(midi_path): os.remove(midi_path)
                if os.path.exists(xml_path): os.remove(xml_path)

                return {
                    "success": True,
                    "data": {
                        "fileName": original_filename,
                        "duration": float(len(y) / sr),
                        "tempo": float(tempo),
                        "instrument": instrument,
                        "notes_count": len(unique_notes),
                        "notes": unique_notes[:200],
                        "sample_rate": sr,
                        "midi_base64": midi_base64,
                        "xml_base64": xml_base64,
                        "message": f"Guitar 모드: Basic Pitch 분석 및 TAB 매핑 완료!"
                    }
                }

            except Exception as e:
                print(f"Basic Pitch Guitar failed: {e}")
                logging.error(f"Guitar Analysis Failed: {e}", exc_info=True)
                import traceback
                traceback.print_exc()
                # Fallback to default

        
        # --- 기존 Librosa 단선율/단순 로직 (피아노 외 또는 Basic Pitch 실패 시) ---
        
        # 피치 감지 (기본값)
        pitches, magnitudes = librosa.piptrack(
            y=y,
            sr=sr,
            fmin=fmin,
            fmax=fmax
        )
        
        # 음표 추출 (간단한 버전)
        notes = []
        hop_length = 512
        
        for t in range(0, pitches.shape[1], 10):  # 10프레임마다 샘플링
            index = magnitudes[:, t].argmax()
            pitch = pitches[index, t]
            
            if pitch > 0 and magnitudes[index, t] > 0.1:  # 임계값
                note_name = librosa.hz_to_note(pitch)
                time = librosa.frames_to_time(t, sr=sr, hop_length=hop_length)
                
                notes.append({
                    'time': float(time),
                    'note': note_name,
                    'frequency': float(pitch)
                })
        
        # 중복 제거 (연속된 같은 음표)
        unique_notes = []
        prev_note = None
        for note in notes:
            if note['note'] != prev_note:
                if instrument == 'piano': # Fallback piano logic
                    split_freq = librosa.note_to_hz('C4')
                    note['hand'] = 'right' if note['frequency'] >= split_freq else 'left'

                unique_notes.append(note)
                prev_note = note['note']
        
        # Fallback MIDI Generation
        midi_base64 = None
        try:
            import pretty_midi
            import base64
            
            pm = pretty_midi.PrettyMIDI()
            inst_program = 0 if instrument == 'piano' else 24 # 24: Guitar
            inst = pretty_midi.Instrument(program=inst_program)
            
            for note in unique_notes:
                pitch = librosa.note_to_midi(note['note'])
                start = note['time']
                end = start + 0.5 
                pm_note = pretty_midi.Note(velocity=100, pitch=int(pitch), start=start, end=end)
                inst.notes.append(pm_note)
            
            pm.instruments.append(inst)
            
            midi_path = os.path.join(os.path.dirname(file_path), f"{original_filename}_fallback.mid")
            pm.write(midi_path)
            
            with open(midi_path, "rb") as f:
                midi_base64 = base64.b64encode(f.read()).decode('utf-8')
            
            if os.path.exists(midi_path): os.remove(midi_path)
            
        except Exception as e:
            print(f"Fallback MIDI generation failed: {e}")

        return {
            "success": True,
            "data": {
                "fileName": original_filename,
                "duration": float(len(y) / sr),
                "tempo": float(tempo),
                "instrument": instrument,
                "notes_count": len(unique_notes),
                "notes": unique_notes[:100],
                "sample_rate": sr,
                "midi_base64": midi_base64,
                "xml_base64": None, # Fallback doesn't support XML for now
                "message": f"{instrument} 모드로 분석이 완료되었습니다. (Librosa Fallback)"
            }
        }
        
    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Audio analysis failed: {str(e)}")

@app.post("/api/analyze")
async def analyze_audio(file: UploadFile = File(...), instrument: str = Form("piano")):
    """오디오 파일 업로드 및 분석"""
    # 파일 타입 검증
    allowed_types = ["audio/mpeg", "audio/wav", "audio/ogg", "audio/mp4", "audio/x-m4a"]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"지원하지 않는 파일 형식입니다. 허용: {', '.join(allowed_types)}"
        )
    
    # 임시 파일로 저장
    with tempfile.NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix) as tmp_file:
        content = await file.read()
        tmp_file.write(content)
        tmp_path = tmp_file.name
    
    try:
        return await process_audio_file(tmp_path, file.filename, instrument)
    finally:
        # 임시 파일 삭제
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

@app.post("/api/process-youtube")
async def process_youtube(request: YoutubeRequest):
    """YouTube URL 다운로드 및 분석 (pytubefix 사용)"""
    url = request.url
    instrument = request.instrument
    
    import shutil
    from pytubefix import YouTube
    from pytubefix.cli import on_progress
    
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            print(f"Processing YouTube URL with pytubefix: {url}")
            # Try 'ANDROID' client which is often more reliable
            yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True, client='ANDROID')
            video_title = yt.title
            video_id = yt.video_id
            print(f"Title: {video_title}, ID: {video_id}")
            
            # Get audio stream
            ys = yt.streams.get_audio_only()
            if not ys:
                raise Exception("No audio stream found")
                
            # Download
            download_path = ys.download(output_path=temp_dir, filename=f"{video_id}.m4a")
            print(f"Downloaded to: {download_path}")
            
            # 오디오 분석 수행
            # process_audio_file handles loading with librosa, which supports m4a usually.
            # If librosa fails with m4a, we might need ffmpeg conversion, but let's try direct first.
            result = await process_audio_file(download_path, video_title, instrument)
            
            # 메타데이터 추가
            result['data']['videoId'] = video_id
            result['data']['title'] = video_title
            
            return result
                
        except Exception as e:
            print(f"YouTube processing error: {str(e)}")
            import traceback
            traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"YouTube processing failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
