import requests
import time
import matplotlib.pyplot as plt
# import mplfinance as mpf


# CoinGecko API endpoint for the Bitcoin price
api_endpoint = 'https://api.coingecko.com/api/v3/simple/price'
coin_id = 'bitcoin'
vs_currency = 'usd'

# List to keep updating
bitcoin_vals = []

# Initialize the plot
plt.ion()
plt.figure()
plt.title("Bitcoin Price Visualization")
plt.ylabel("Price")

# Function to fetch live Bitcoin price
def fetch_bitcoin_price():
    try:
        # Specify the parameters for the API request
        params = {
            'ids': coin_id,
            'vs_currencies': vs_currency
        }

        # Send a GET request to the CoinGecko API
        response = requests.get(api_endpoint, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the price data from the response
            data = response.json()
            bitcoin_price = data[coin_id][vs_currency]
            bitcoin_vals.append(bitcoin_price)
            
            # Update the plot with the new data
            # mpf.plot(bitcoin_vals, type='candle', style='yahoo', title="Bitcoin Price Candlestick Chart")
            plt.plot(bitcoin_vals,'b-')
            plt.pause(0.001)
            
        else:
            # Handle the API request error
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        # Handle any network or connection errors
        print(f"An error occurred: {e}")

# Continuously fetch and display the live Bitcoin price
while True:
    fetch_bitcoin_price()
    # Wait for 10 seconds before fetching the price again
    time.sleep(5)




