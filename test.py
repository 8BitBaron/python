import requests

from requests import get

ip = get('https://api.ipify.org').text
print('Public IP address is: {}'.format(ip))

