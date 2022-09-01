# { Required Modules }:
import requests
import json

# { Meme Generator Function }:
def get_meme():
  url = "https://meme-api.herokuapp.com/gimme"
  response = json.loads(requests.request('GET', url).text)
  meme_large = response['preview'][-2]
  subreddit = response['subreddit']
  url = response['url']
  postLink = response['postLink']
  return meme_large, subreddit, url, postLink
