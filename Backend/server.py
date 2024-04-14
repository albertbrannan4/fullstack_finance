from flask import Flask,request
from polygon import RESTClient
from requests_oauthlib import OAuth1Session


from local_business import get_local_business_data ,get_yahoo_data


app = Flask(__name__)

client = RESTClient(api_key="sSdMfHNF6plcQt7FUUdkpo48gwcrnp6G")




@app.route("/")
def hello_world():
    return [{'name':'Albert'}]



@app.route("/business",methods=['POST'])
def find_business_info():
    
    data = request.get_json()
    
    company_name = data['name']
    
    company_data = get_yahoo_data(company_name)
    
    
    return company_data

    
    