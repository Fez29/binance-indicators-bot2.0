from binance.client import Client
from api_keys import api_key, api_secret

testnet = True

# insert your api keys here
if testnet == True:
    # Testnet
    api_key = "HZcMh0e21m9HDNaElOYIpBZJ16xoVE25SqjXbmXrfXq6P9fS0kj8yUBiqbjcgM3h"
    api_secret = "oK4pSQLbBXA98TFodCIfNhV6gfL2w69ZjXsc6c0eOVzIvmzWhcICppFgLlJGV7qH"
else:
    api_key = "your_api_key"
    api_secret = "your_api_secret"

client = Client(api_key, api_secret)
