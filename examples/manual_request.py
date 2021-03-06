# Copyright (C) 2015 Twitter, Inc.

from twitter_ads.client import Client
from twitter_ads.cursor import Cursor
from twitter_ads.http import Request

CONSUMER_KEY = 'your consumer key'
CONSUMER_SECRET = 'your consumer secret'
ACCESS_TOKEN = 'user access token'
ACCESS_TOKEN_SECRET = 'user access token secret'
ADS_ACCOUNT = 'ads account id'

# initialize the twitter ads api client
client = Client(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# load up the account instance
account = client.accounts(ADS_ACCOUNT)

# using the Request object you can manually request any
# twitter ads api resource that you want.

resource = '/0/accounts/{account_id}/features'.format(account_id=account.id)
params = {'feature_keys': 'AGE_TARGETING,CPI_CHARGING'}

# build and execute the request
response = Request(client, 'get', resource, params=params).perform()
print(response.body['data'][0])

# you can also manually construct requests to be
# used in Cursor objects.

resource = '/0/targeting_criteria/locations'
params = {'location_type': 'CITY', 'q': 'port'}
request = Request(client, 'get', resource, params=params)
cursor = Cursor(None, request)

# execute requests and iterate cursor until exhausted
for obj in cursor:
    print(object['name'])
