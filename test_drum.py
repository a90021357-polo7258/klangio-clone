import requests
import json
import base64
import time

# API Endpoint
url = "http://localhost:8000/api/analyze"

# Test Audio File (use silence or any wav file as input, logic relies on onset)
# Ideally we should use a drum loop, but for quick check any audio works.
file_path = "ai-server/test_audio.wav" 

try:
    print(f"Sending request to {url} with instrument='drum'...")
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "audio/wav")}
        data = {"instrument": "drum"}
        start_time = time.time()
        response = requests.post(url, files=files, data=data)
        elapsed = time.time() - start_time
        
    print(f"Status Code: {response.status_code}")
    print(f"Time Taken: {elapsed:.2f}s")
    
    if response.status_code == 200:
        result = response.json()
        if result['success']:
            print(f"Success! Message: {result['data']['message']}")
            notes = result['data']['notes']
            print(f"Beats found: {len(notes)}")
            if len(notes) > 0:
                print(f"First beat: {notes[0]['note']} (MIDI {notes[0]['midi']}) at {notes[0]['time']:.2f}s")
                
                # Distribution
                kicks = sum(1 for n in notes if n['note'] == 'Kick')
                snares = sum(1 for n in notes if n['note'] == 'Snare')
                hihats = sum(1 for n in notes if n['note'] == 'Hi-Hat')
                print(f"Distribution - Kick: {kicks}, Snare: {snares}, Hi-Hat: {hihats}")
            
            # Check Base64
            if result['data']['midi_base64']:
                print("MIDI Base64 received.")
            if result['data']['xml_base64']:
                print("XML Base64 received.")
        else:
            print("Analysis failed (logic error)")
    else:
        print(f"Error: {response.text}")

except Exception as e:
    print(f"Request failed: {e}")
