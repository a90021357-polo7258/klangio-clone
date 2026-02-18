import requests
import json
import time

# API Endpoint
url = "http://localhost:8000/api/analyze"
file_path = "ai-server/test_audio.wav"

payload = {
    "instrument": "violin"
}

files = {
    'file': ('test_audio.wav', open(file_path, 'rb'), 'audio/wav')
}

try:
    print(f"Sending request to {url} with instrument='violin'...")
    start_time = time.time()
    response = requests.post(url, data=payload, files=files)
    elapsed = time.time() - start_time
    
    print(f"Status Code: {response.status_code}")
    print(f"Time Taken: {elapsed:.2f}s")
    
    if response.status_code == 200:
        result = response.json()
        if result['success']:
            print("Success! Message: " + result['data']['message'])
            notes = result['data']['notes']
            print(f"Notes found: {len(notes)}")
            if len(notes) > 0:
                print(f"First note: {notes[0]['note']}")
        else:
            print(f"Analysis failed: {result}")
    else:
        print(f"Error: {response.text}")

except Exception as e:
    print(f"Request failed: {e}")
