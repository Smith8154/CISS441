import requests
url = 'https://en.wikipedia.org/wiki/Cleveland,_Tennessee'
req = requests.get(url)
print(url, "\n" 'HTTP Status Code:', req.status_code)
with open('wiki_cleveland_tn.txt', mode='w') as fo:
    fo.write(req.text)
