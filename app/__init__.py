# Authors: CS For Insight (Summer19 - JG)

try:
    from flask import Flask
except:
    print("could not import Flask from flask")

from config import Config

app = Flask(__name__, static_url_path='')
app.config.from_object(Config)

if __name__ == "__main__":
    app.run(debug=True)

from app import routes
