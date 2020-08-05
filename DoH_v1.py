##curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=facebook.com&type=A'
import requests
import json

headers = {
    'accept': 'application/dns-json',
}

params = (
    ('name', 'facebook.com'),
    ('type', 'A'),
)

response = requests.get('https://cloudflare-dns.com/dns-query', headers=headers, params=params)
data = json.dumps(response.json(), indent=2)
decoded = json.loads(data)

for x in decoded['Answer']:
    IP_Addr = x['data']
    print(IP_Addr)
