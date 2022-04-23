import twitter

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

api = twitter.Api(consumer_key='yq4FLUzRXCyRU6iJaysf2BdsB',
                      consumer_secret='UeojQFvB9C7EJUQoLUYHWkyvg42diPHUK0t5v4xAQ7imTTusk0',
                      access_token_key='1118339159100403713-LajXmXFzyR5uAeMjT679cKVMbWY5Ly',
                      access_token_secret='PmTv4SpnBXZyyg74sK7fBQmXPTzL50BvwTefrsuNU2zLb')

print(api.VerifyCredentials())