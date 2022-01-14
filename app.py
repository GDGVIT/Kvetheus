# import necessary libraries and functions
from urllib import response
from flask import Flask, jsonify, request
from src.modules.dnsenumeration import get_records

# creating a Flask app
app = Flask(__name__)

@app.route('/ping', methods = ['GET', 'POST'])
def ping():
	return jsonify({'response': 'pong'})

@app.route('/v1/api/domain/records', methods = ['POST'])
def domainrecords():
    domain = request.args.get('domain')
    return jsonify({'response':get_records(domain)})

if __name__ == '__main__':
	app.run(debug = True)
