from flask import Flask,request
from polygon import RESTClient
from requests_oauthlib import OAuth1Session


from local_business import get_local_business_data ,get_yahoo_data


app = Flask(__name__)

client = RESTClient(api_key="sSdMfHNF6plcQt7FUUdkpo48gwcrnp6G")




@app.route("/")
def hello_world():
    return [{'name':'Albert'}]



@app.route("/business",methods=['GET', 'POST'])
def find_business_info():
    
    stock_name =  request.args.get('name')
    
    # local = get_local_business_data(business_name)
    yahoo_finance = get_yahoo_data(stock_name)
  
    return yahoo_finance

    
    