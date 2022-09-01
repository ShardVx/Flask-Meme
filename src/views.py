# { Required Modules }:
from flask import Blueprint, render_template
from datetime import date
import requests
import json

# { Functions }:
from .functions import get_meme

# { Routes/Pages }:
views = Blueprint('views', __name__)

@views.route('/')
def meme():
  meme_pic,subreddit,url,postLink = get_meme()
  today = date.today()
  return render_template('meme.html', meme_pic=meme_pic, subreddit=subreddit, date=today, postLink=postLink, url=url)
