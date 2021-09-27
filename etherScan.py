import requests
from datetime import datetime

def getEth(apikey, module = 'gastracker',action= 'gasoracle'):
    
    response = requests.get(f'https://api.etherscan.io/api?module={module}&action={action}&apikey={apikey} ').json()

    ether_gas_info =   {"suggestBaseFee":response['result']["suggestBaseFee"],"UTC-date":datetime.utcnow()}



    return " ".join( str(x) for x in [ether_gas_info])
    