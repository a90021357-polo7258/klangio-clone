
import requests
import os

url = "http://localhost:8000/api/analyze"
file_path = "c:\\Users\\xeon\\Desktop\\Anti-Gravity\\klangio-clone\\ai-server\\test_audio.wav"

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found.")
    exit(1)

try:
    with open(file_path, 'rb') as f:
        files = {'file': (os.path.basename(file_path), f, 'audio/wav')}
        data = {'instrument': 'vocal'}
        print(f"Sending request to {url} with instrument='vocal'...")
        response = requests.post(url, files=files, data=data)
        
    print(f"Status Code: {response.status_code}")
    # print(f"Response: {response.text}") # Too long
    if response.status_code == 200:
        json_data = response.json()
        print(f"Success! Message: {json_data['data']['message']}")
        print(f"Notes found: {json_data['data']['notes_count']}")
        if json_data['data']['notes_count'] > 0:
            print(f"First note: {json_data['data']['notes'][0]['note']}")
        else:
            print("No notes found.")
    else:
        print(f"Error: {response.text}")
        
except Exception as e:
    print(f"Request failed: {e}")
