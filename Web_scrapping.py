import tweepy 
import pandas as pd

api_key = 'sDi8ZM37CYRgSXkjkwPmEXfRR'
api_key_secret = 'TCp9gNRc57QtAz4AK383sVIjv6KkoyIrCUdgHsQxFPTjAuDa5f'

access_token = '1686638372859871232-BM1V6u5sLGCrHd0Z1Gr9S75bVz1p02'
access_token_secret = 'JUHuWsq9cRjxKhAGyIlodcyUyd0M3ZGkKsJm94DqnVjid'

# Authentication

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# getting to the tweets 

public_tweets = api.user_timeline(screen_name='ritvkkk', count=10)

# to see the first tweets text 

''' 
print(public_tweets[0].text) 

for tweet in public_tweets:
    print (tweet.text)        

'''

# To put all the tweets into a dictionary

data = {}
column_names = ['Time','User','Tweet']

for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

# converting data into df 

df = pd.DataFrame(data, columns = column_names)

# saving the df 

df.to_csv('tweets.csv')
