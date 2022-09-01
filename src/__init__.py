# { Required Modules }:
from flask import Flask
from os import path

# { Create App Function }:
def create_app():
  app = Flask(__name__) # Creating Flask Application
  
  from .views import views # Import views from views.py
  
  app.register_blueprint(views, url_prefix='/') # Register views.py blueprint
  
  return app
