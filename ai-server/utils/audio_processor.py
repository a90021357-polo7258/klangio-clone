import librosa
import numpy as np
from typing import List, Dict, Tuple

class AudioProcessor:
    """오디오 파일 분석 클래스"""
    
    def __init__(self, audio_path: str, sr: int = 22050):
        """
        Args:
            audio_path: 오디오 파일 경로
            sr: 샘플링 레이트 (기본: 22050 Hz)
        """
        self.audio, self.sr = librosa.load(audio_path, sr=sr, duration=30)
        self.duration = len(self.audio) / self.sr
        
    def detect_pitch(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        피치(음높이) 감지
        
        Returns:
            pitches: 피치 배열
            magnitudes: 크기 배열
        """
        pitches, magnitudes = librosa.piptrack(
            y=self.audio,
            sr=self.sr,
            fmin=librosa.note_to_hz('C2'),
            fmax=librosa.note_to_hz('C7')
        )
        return pitches, magnitudes
    
    def detect_tempo(self) -> Tuple[float, np.ndarray]:
        """
        템포(BPM) 감지
        
        Returns:
            tempo: BPM 값
            beats: 비트 위치 배열
        """
        tempo, beats = librosa.beat.beat_track(y=self.audio, sr=self.sr)
        return float(tempo), beats
    
    def extract_notes(self, hop_length: int = 512, threshold: float = 0.1) -> List[Dict]:
        """
        음표 추출
        
        Args:
            hop_length: 프레임 간격
            threshold: 크기 임계값
            
        Returns:
            음표 리스트 [{'time': float, 'note': str, 'frequency': float}]
        """
        pitches, magnitudes = self.detect_pitch()
        
        notes = []
        
        # 10프레임마다 샘플링 (성능 최적화)
        for t in range(0, pitches.shape[1], 10):
            index = magnitudes[:, t].argmax()
            pitch = pitches[index, t]
            magnitude = magnitudes[index, t]
            
            if pitch > 0 and magnitude > threshold:
                note_name = librosa.hz_to_note(pitch)
                time = librosa.frames_to_time(t, sr=self.sr, hop_length=hop_length)
                
                notes.append({
                    'time': float(time),
                    'note': note_name,
                    'frequency': float(pitch),
                    'magnitude': float(magnitude)
                })
        
        return self._remove_duplicates(notes)
    
    def _remove_duplicates(self, notes: List[Dict]) -> List[Dict]:
        """연속된 같은 음표 제거"""
        if not notes:
            return []
        
        unique_notes = [notes[0]]
        
        for note in notes[1:]:
            if note['note'] != unique_notes[-1]['note']:
                unique_notes.append(note)
        
        return unique_notes
    
    def get_audio_info(self) -> Dict:
        """오디오 기본 정보"""
        tempo, _ = self.detect_tempo()
        
        return {
            'duration': self.duration,
            'sample_rate': self.sr,
            'tempo': tempo,
            'total_samples': len(self.audio)
        }
