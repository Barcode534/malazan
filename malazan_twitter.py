import json
import tweepy
import random
import csv

api_key = "uRB40NTUh1OoP258mjr8SUMXn"
api_secret = "WdDWq2FegV2QZrs4TOXtrkry4lvifcPxNsCtprRWic2xn5sGuI"

access_token = "1153109923154333697-DJ7cMaKvLgeyUR1n7sWYTIw3eE4VWN"
access_token_secret = "28TsSM1cYAOObZUsRC73blmh3WYuQR5lZ4f8TJW0QsKWr"

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