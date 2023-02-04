import requests

email_address = str(input('Email: asibahmed4@gmail.com'))
response = requests.get(
    "https://gmail.com/api/email/validate",
    params = {'email': email_address})

status = response.json()['status']
if status == "valid":
  print("email is valid")
elif status == "invalid":
  print("email is invalid")
else:
  print("email was unknown")