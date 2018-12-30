import requests

client_key = 'SwDA0B5NpMZSWbH0ornhaGsk0'
client_secret = 'mlgQlhRpBbDdByPVkT74TGWnWaO8IPvTeGTK2zfFAEx7itaB3k'

import base64

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')


base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

access_token = auth_resp.json()['access_token']


search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params = {
    'q': 'USDJPY Long',
    'result_type': 'recent',
    'count': 5,
    "lang": "en",
    "verified": 'true'
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

tweet_data = search_resp.json()

for x in tweet_data['statuses']:
    print(x['text'] + '\n')