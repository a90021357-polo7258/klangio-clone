import os
import sys

def debug_guitar_logic():
    print("Starting Guitar Debug...")
    
    try:
        print("Importing libraries...")
        import librosa
        import numpy as np
        from basic_pitch.inference import predict
        import tensorflow as tf
        from music21 import converter, note, chord, stream, layout, clef, metadata, key, meter, instrument
        import music21
        
        print(f"Libraries imported successfully.")
        print(f"TensorFlow version: {tf.__version__}")
        print(f"Music21 version: {music21.__version__}")
        
        # Test with a dummy file or create one
        # Create a simple sine wave file using librosa
        import soundfile as sf
        sr = 22050
        t = np.linspace(0, 5, int(sr*5))
        y = 0.5 * np.sin(2 * np.pi * 440 * t) # A4
        
        test_file = "debug_guitar_test.wav"
        sf.write(test_file, y, sr)
        print(f"Created test file: {test_file}")
        
        # Run Basic Pitch
        print("Running Basic Pitch prediction...")
        model_output, midi_data, note_events = predict(
            test_file,
            onset_threshold=0.5,
            frame_threshold=0.3
        )
        print("Prediction successful.")
        
        # Run Music21 Logic
        print("Running Music21 Logic...")
        
        s = stream.Score()
        p = stream.Part()
        p.insert(0, metadata.Metadata())
        p.metadata.title = "Debug Test"
        
        guitar_tuning = {
            1: 64, 2: 59, 3: 55, 4: 50, 5: 45, 6: 40
        }
        
        def get_best_fret(midi_val):
            best_string = 6
            best_fret = 0
            min_score = 1000
            for string_num, open_midi in guitar_tuning.items():
                fret = midi_val - open_midi
                if 0 <= fret <= 24:
                    score = fret * 2
                    if fret == 0: score = 0
                    if score < min_score:
                        min_score = score
                        best_string = string_num
                        best_fret = fret
            return best_string, best_fret

        # Dummy note processing
        for pm_note in midi_data.instruments[0].notes:
            m21_note = note.Note()
            m21_note.pitch.midi = pm_note.pitch
            string_num, fret_num = get_best_fret(pm_note.pitch)
            m21_note.addLyric(f"Str:{string_num}")
            m21_note.addLyric(f"Fret:{fret_num}")
            p.append(m21_note)
            
        s.insert(0, p)
        
        # Test generic XML write
        xml_path = "debug_output.xml"
        s.write('musicxml', fp=xml_path)
        print(f"MusicXML written to {xml_path}")
        
        # Cleanup
        if os.path.exists(test_file): os.remove(test_file)
        if os.path.exists(xml_path): os.remove(xml_path)
        
        print("ALL TESTS PASSED")

    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_guitar_logic()
