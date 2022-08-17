# import necessary libraries and functions
from urllib import response
from flask import Flask, jsonify, request
from src.modules.macaddress import MacAddressLookup
from src.modules.dnsenumeration import get_records
from src.modules.domain_whois import get_whois
from src.modules.subdomain import get_subdomains
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/ping", methods=["GET", "POST"])
def ping():
    return jsonify({"response": "pong"})


@app.route("/v1/api/domain/records", methods=["POST"])
def domainrecords():
    return {"response": get_records(request.args.get("domain"))}


@app.route("/v1/api/domain/whois", methods=["GET"])
def whois():
    return get_whois(request.args.get("q"))


@app.route("/v1/api/domain/subdomains", methods=["POST"])
def subdomains():
    return get_subdomains(request.args.get("q"))


@app.route("/v1/api/mac", methods=["GET"])
def mac():
    return MacAddressLookup(request.args.get("q"))


if __name__ == "__main__":
    app.run(debug=True)
