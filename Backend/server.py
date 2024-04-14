from flask import Flask
from polygon import RESTClient

app = Flask(__name__)

client = RESTClient(api_key="sSdMfHNF6plcQt7FUUdkpo48gwcrnp6G")

@app.route("/")
def hello_world():
    return [{'name':'Albert'}]