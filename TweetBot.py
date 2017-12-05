import tweepy
import json
import requests
from Secrets import consumer_key,consumer_secret,access_token,access_secret

def get_url(url):
	response =requests.get(url)
	content=response.content.decode("utf8")
	return content
	
def get_json_from_url(url):
	content=get_url(url)
	js=json.loads(content)
	return js
	
bestemmia=''
while bestemmia is None or bestemmia=='':
	res=get_json_from_url("http://www.bestemmie.org/api/bestemmie/random")
	for r in res:
		bestemmia=r['bestemmia_upp']
		

print(bestemmia)

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_secret)

api=tweepy.API(auth)


api.update_status(bestemmia+" #bestemmie #world")

print("Tweettato")