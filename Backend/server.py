from flask import Flask
from polygon import RESTClient
import requests

app = Flask(__name__)

client = RESTClient(api_key="sSdMfHNF6plcQt7FUUdkpo48gwcrnp6G")
url = "https://local-business-data.p.rapidapi.com/search"

querystring = {"query":"River City Science Academy","limit":"20","lat":"37.359428","lng":"-121.925337","zoom":"13","language":"en","region":"us"}

headers = {
	"X-RapidAPI-Key": "023207c256msh41bd9a165c606c8p1b9c09jsn29c80b6f2916",
	"X-RapidAPI-Host": "local-business-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

@app.route("/")
def hello_world():
    return [{'name':'Albert'}]



@app.route("/business")
def find_business_info():
    return 'Business Info'