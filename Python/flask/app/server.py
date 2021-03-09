import json
import config
import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/<int:poke_id>')
def hello(poke_id=1):
    r = requests.get(config.URL + str(poke_id))

    data = json.loads(r.text)

    image_link = data['sprites']['back_default']

    return render_template('index.html', data=data, image_link=image_link)

if __name__ == "__main__":
    app.run(debug=True)
