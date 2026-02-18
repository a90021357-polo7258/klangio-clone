import requests
import json
import time

# API Endpoint
url = "http://localhost:8000/api/process-youtube"

# Test YouTube Drum Solo (Famous Funky Drummer Break or similar)
# 'Amen Break' - https://www.youtube.com/watch?v=gxJuM2Q07bI (Only 6 seconds long)
# Or 'Simple Drum Beat' - https://www.youtube.com/watch?v=FjS6T8b3-mE
test_url = "https://www.youtube.com/watch?v=FjS6T8b3-mE" 

payload = {
    "url": test_url,
    "instrument": "drum" 
}

try:
    print(f"Sending YouTube Drum request to {url}...")
    start_time = time.time()
    response = requests.post(url, json=payload)
    elapsed = time.time() - start_time
    
    print(f"Status Code: {response.status_code}")
    print(f"Time Taken: {elapsed:.2f}s")
    
    if response.status_code == 200:
        result = response.json()
        if result['success']:
            print("Success! Message: " + result['data']['message'])
            notes = result['data']['notes']
            print(f"Beats found: {len(notes)}")
            
            # Print distribution
            kicks = sum(1 for n in notes if n['note'] == 'Kick')
            snares = sum(1 for n in notes if n['note'] == 'Snare')
            hihats = sum(1 for n in notes if n['note'] == 'Hi-Hat')
            print(f"Distribution - Kick: {kicks}, Snare: {snares}, Hi-Hat: {hihats}")
            
            if len(notes) > 0:
                print(f"First beat at {notes[0]['time']:.2f}s: {notes[0]['note']}")
        else:
            print(f"Analysis failed: {result}")
    else:
        print(f"Error: {response.text}")

except Exception as e:
    print(f"Request failed: {e}")
