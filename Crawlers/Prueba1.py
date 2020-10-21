import requests
r = requests.get('https://www.vodafone.es')
r.status_code
#print(r.text)

r.headers['content-type']