import tweepy
import random
import csv

api_key = #redacted
api_secret = #redacted

access_token = #redacted
access_token_secret = #redacted

print("my twitter bot")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

try:
    redirect_url = auth.get_authorization_url()
    print("working")
except tweepy.TweepError:
    print('Error! Failed to get request token.')

api = tweepy.API(auth)
quotes = []

with open('C:/Users/Cwlrs/Downloads/malazan.csv', 'rt', encoding = 'utf-8') as csvfile:
    lines = csv.reader(csvfile)
    for line in lines:
        print(len(line[0]))
        if len(line[0]) < 280:
            quotes.append(line[0])

for x in range(len(quotes)):
    quotes[x] = quotes[x].replace("\n", " ")
    print(quotes[x])

selection = random.randint(0,len(quotes))
tweet = quotes[selection]
print("final: ", tweet)
api.update_status(tweet)
