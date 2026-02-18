
import wave
import math
import struct

sample_rate = 44100
duration = 1.0 # seconds
frequency = 440.0

obj = wave.open('ai-server/test_audio.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sample_rate)

for i in range(int(sample_rate * duration)):
   value = int(32767.0*math.cos(frequency*math.pi*float(i)/float(sample_rate)))
   data = struct.pack('<h', value)
   obj.writeframesraw( data )

obj.close()
print("Created ai-server/test_audio.wav")
