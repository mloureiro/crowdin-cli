import requests

r = requests.get('https://www.google.com')
print(f'status code: { r.status_code}')