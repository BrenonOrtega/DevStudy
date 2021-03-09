import requests
import config
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    poke_id = 1
    r = requests.get(config.URL + "1")
    print(r)
    return f"Hello Python! I'm Flask\n{r.text}"

if __name__ == "__main__":
    FLASK_APP = 'server.py'
    FLASK_ENV = 'development'
    app.run(debug=True)
