import random
import tweepy
import json
import os

# uncomment the code below and change it to your working directory
# this is mostly just to fix an issue I had with running python3 from linux cron
# this can probably be ignored if you're running it manually, IE: "python3 tweetbot.py"
# otherwise, if you run it like "python3 /home/username/folder/tweetbot.py" you might need this code
# os.chdir("/home/username/folder") 


def random_tweet(string_array, link_array):
    a = random.choice(string_array)
    b = random.choice(link_array)
    return a + b


def read_txt(filename):
    filelist = open(filename).readlines()
    return filelist


file = open('secure.json').read()
data = json.JSONDecoder().decode(file)

ck = data.get('consumer_key')
cs = data.get('consumer_secret')
at = data.get('access_token')
ats = data.get('access_token_secret')

blurbs = read_txt('blurbs.txt')
links = read_txt('links.txt')
tweet = random_tweet(blurbs, links)

client = tweepy.Client(
    consumer_key=ck, consumer_secret=cs,
    access_token=at, access_token_secret=ats
)

response = client.create_tweet(
    text=tweet
)

print(tweet)

