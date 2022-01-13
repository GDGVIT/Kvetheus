# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

@app.route('/ping', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "OK! Working!"
		return jsonify({'data': data})


# Driver function
if __name__ == '__main__':

	app.run(debug = True)
