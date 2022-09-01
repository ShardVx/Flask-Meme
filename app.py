# { Import CreateApp Function }:
from src import create_app

# { Run Web Server }:
app = create_app() # Will create the app to run the server

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True) # Running the webserver in localhost
