import requests
from getpass import getpass

URL = 'https://httpbin.org/basic-auth/Daniel/12345'

password = getpass('Ingresa la contraseña: ')

session = requests.session()
session.auth = ('Daniel', password)

response = session.get(URL)

if response.status_code == 200:
    print(response.json())

if response.status_code == 401:
    print('Unsuccessful authentication.')