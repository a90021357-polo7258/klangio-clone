from music21 import stream, note, tempo, meter, chord
from typing import List, Dict
import numpy as np

class MIDIConverter:
    """MIDI 및 MusicXML 변환 클래스"""
    
    def __init__(self, notes_data: List[Dict], bpm: float = 120):
        """
        Args:
            notes_data: 음표 데이터 리스트
            bpm: 템포 (기본: 120 BPM)
        """
        self.notes_data = notes_data
        self.bpm = bpm
        
    def create_music_stream(self) -> stream.Stream:
        """
        music21 스트림 생성
        
        Returns:
            music21.stream.Stream 객체
        """
        s = stream.Stream()
        
        # 템포 설정
        s.append(tempo.MetronomeMark(number=self.bpm))
        
        # 박자 설정 (4/4)
        s.append(meter.TimeSignature('4/4'))
        
        # 음표 추가
        for note_data in self.notes_data:
            try:
                # 음표 이름에서 옥타브 번호 추출
                note_name = note_data['note']
                
                # Note 객체 생성
                n = note.Note(note_name)
                n.offset = note_data['time']
                n.quarterLength = 0.5  # 8분음표 (간단화)
                
                s.append(n)
            except Exception as e:
                # 잘못된 음표는 건너뛰기
                print(f"음표 추가 실패: {note_data['note']} - {e}")
                continue
        
        return s
    
    def export_midi(self, output_path: str) -> str:
        """
        MIDI 파일로 내보내기
        
        Args:
            output_path: 출력 파일 경로
            
        Returns:
            저장된 파일 경로
        """
        s = self.create_music_stream()
        s.write('midi', fp=output_path)
        return output_path
    
    def export_musicxml(self, output_path: str) -> str:
        """
        MusicXML 파일로 내보내기
        
        Args:
            output_path: 출력 파일 경로
            
        Returns:
            저장된 파일 경로
        """
        s = self.create_music_stream()
        s.write('musicxml', fp=output_path)
        return output_path
    
    def export_pdf(self, output_path: str) -> str:
        """
        PDF 악보로 내보내기 (Lilypond 필요)
        
        Args:
            output_path: 출력 파일 경로
            
        Returns:
            저장된 파일 경로
        """
        s = self.create_music_stream()
        
        try:
            # Lilypond를 사용하여 PDF 생성
            s.write('lily.pdf', fp=output_path)
            return output_path
        except Exception as e:
            raise Exception(f"PDF 생성 실패 (Lilypond 설치 필요): {e}")
    
    def get_stream_info(self) -> Dict:
        """스트림 정보 반환"""
        s = self.create_music_stream()
        
        return {
            'total_notes': len(s.flatten().notes),
            'duration': s.duration.quarterLength,
            'tempo': self.bpm
        }
