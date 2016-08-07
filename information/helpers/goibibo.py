import requests

def get_ibibo_data():
    response = requests.get("https://hermes.goibibo.com/"+
                       "hotels/v2/search/data/v3/"+
                       "6771549831164675055/20160807/"
                       +"20160831/"+
                       "1-1_0?s=popularity&ct=b2c&cur=INR&pid=1")

    data = response.json().get('data',None)
    return data
    




