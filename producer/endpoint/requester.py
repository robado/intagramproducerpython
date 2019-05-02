import requests


def user_endpoint(access_token):
    r = requests.get('https://api.instagram.com/v1/users/self/?access_token={}'.format(access_token))
    return r.json()
