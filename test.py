import requests
from config import url1
response = requests.get(url1)



if response.status_code == 200:
    
    
    result = response.json()
    print(result)
else:
    print(f'Error:{response.text}')