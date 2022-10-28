import requests
from urllib.parse import ParseResult

def get_auth_token(username:str, password:str, url:ParseResult):
    url = url
    r = requests.post(url._replace(path='/api/auth/').geturl(), json={'username': username, 'password': password})
    return r.json()['token']