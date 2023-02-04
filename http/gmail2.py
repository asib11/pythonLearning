import requests
url='https://mail.google.com/mail/u/0'
#res = requests.get(url,headers={'accept': 'application/json'})
res = requests.get(url,headers={'accept':'text/plain'})
data = res.json()
print(data)