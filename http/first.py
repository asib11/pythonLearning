import requests

url = 'https://286545066348-pnpisu8ioi7lq0jlvfaormnr8cjafqd1.apps.googleusercontent.com'
res = requests.post(url, auth=('asibahmed4@gmail.com'))
print(res.status_code)

if res.status_code == 200:
    print('ok')
else:
    print('decline')
#print(f'response is {res.status_code}')
#print(res.headers)
#print(res.text)

