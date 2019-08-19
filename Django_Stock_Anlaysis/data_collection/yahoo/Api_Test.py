import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"

querystring = {"symbol":"AMRN"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "0deaf62298msh6b83cd7e47980f1p1188d5jsn1be44317f0a2"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)