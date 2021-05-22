import requests

LOGIN_SERVICE_URL = 'app-login:5005/authorize'

def logged_in(token: str):
    def main(func):
        data = {'token': token}
        r = requests.post(LOGIN_SERVICE_URL, data)
        if r.status_code == 200:
            func()
        else:
            print('Authorization failed')
    return main
