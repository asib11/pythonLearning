import requests
url='https://icanhazdadjoke.com/'
res = requests.get(url,headers={'accept': 'application/json'},params={'term':'cat'})
#res = requests.get(url,headers={'accept':'text/plain'})
data = res.json()
print(data['joke'])
#print(res)
#print(res.headers)
#print(res.text)
#print(res.status_code)
