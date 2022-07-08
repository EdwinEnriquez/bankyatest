from datetime import datetime, date
from flask import Flask, jsonify,json
import os

from requests import request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/cat-facts', methods=['GET'])
@app.route('/cat-facts/', methods=['GET'])
@app.route('/cat-facts/<int:number>', methods=['GET'])
def catfacts(number=1):
    if number in range(0,501):
        response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount="+str(number))
        input_dict = [response.json()] if number == 1 else response.json()
        fmt = '%Y-%m-%dT%H:%M:%S.%fZ'
        output_dict = [x for x in input_dict if datetime.strptime(x['updatedAt'],fmt).year == 2022]
        if len(output_dict) > 0:
            output_json = json.dumps(output_dict, skipkeys = True, allow_nan = True, indent = 4)    
        else:
            output_json = {"error": "Posible no-one facts update at 2022 was found went you make a request of 1 element"}
        return output_json
    else:
        return jsonify({"error":"Only can request between 1 and 500 facts"})

@app.errorhandler(500)
def internal_error(error):
    return "500 error" 
@app.errorhandler(404)
def internal_error(error):
    return "404 error" 


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)