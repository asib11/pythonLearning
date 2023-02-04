import requests

url = 'https://286545066348-j31et1vt78arg8ii5voun5qpqn252lq1.apps.googleusercontent.com'
res = requests.post(url, auth=('asibahmed4@gmail.com', '27asib42'))
if res.status_code == 200:
    print('ok')
else:
    print('decline')
#print(f'response is {res.status_code}')
#print(res.headers)
#print(res.text)

