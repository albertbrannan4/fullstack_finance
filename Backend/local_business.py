import requests
import yfinance as yf


def get_local_business_data(business_name):
  

    url = "https://local-business-data.p.rapidapi.com/search"

    querystring = {"query":business_name,"limit":"20","lat":"37.359428","lng":"-121.925337","zoom":"13","language":"en","region":"us"}

    headers = {
    "X-RapidAPI-Key": "023207c256msh41bd9a165c606c8p1b9c09jsn29c80b6f2916",
    "X-RapidAPI-Host": "local-business-data.p.rapidapi.com"
    }

    location_data = requests.get(url, headers=headers, params=querystring)
    result = location_data.json()['data'][0]
         
    
    return result




def get_yahoo_data(stock_name):
    
   business_data = yf.Ticker(stock_name)
   

   info = business_data.info
   
#    income_statement = business_data.income_stmt
   
#    balance_sheet = business_data.balance_sheet
   
#    result = {"general_info": info}
   
   return info

   
   