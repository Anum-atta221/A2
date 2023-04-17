import requests

response = requests.get('http://localhost:5000')
message = response.text
print(f'Message received from server: {message}')
