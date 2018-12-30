client_key = 'SwDA0B5NpMZSWbH0ornhaGsk0'
client_secret = 'mlgQlhRpBbDdByPVkT74TGWnWaO8IPvTeGTK2zfFAEx7itaB3k'

import base64

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')


import requests

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)


search_headers = {
    'Authorization': 'Bearer {}'.format('mlgQlhRpBbDdByPVkT74TGWnWaO8IPvTeGTK2zfFAEx7itaB3k')
}

search_params = {
    'q': 'General Election',
    'result_type': 'recent',
    'count': 2
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

tweet_data = search_resp.json()

print(tweet_data)
# for x in tweet_data['statuses']:
#     print(x['text'] + '\n')