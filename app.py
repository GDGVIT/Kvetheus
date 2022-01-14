# import necessary libraries and functions
from urllib import response
from flask import Flask, jsonify, request
from src.modules.dnsenumeration import get_records
from src.modules.domain_whois import get_whois

# creating a Flask app
app = Flask(__name__)


@app.route("/ping", methods=["GET", "POST"])
def ping():
    return jsonify({"response": "pong"})


@app.route("/v1/api/domain/records", methods=["POST"])
def domainrecords():
    domain = request.args.get("domain")
    return {"response": get_records(request.args.get("domain"))}


@app.route("/v1/api/domain/whois", methods=["GET"])
def whois():
    return get_whois(request.args.get("q"))


if __name__ == "__main__":
    app.run(debug=True)
