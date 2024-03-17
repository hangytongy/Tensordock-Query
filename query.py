import requests
import json
import time
from datetime import datetime
from slack import WebClient

endpoint = "https://console.tensordock.com/api/stock/list"
gpus = ['QUADRO_4000','A4000','QUADRO_5000','V100_16GB']
locations = ['na-us-chi-1','na-us-las-1','na-us-nyc-1','na-us-nyc-2'] 

# Initialize Slack client with your bot's API token
slack_client = WebClient(token="")

def main():

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date Time : {dt_string} \n")

    response = requests.get(endpoint)

    for gpu in gpus:
        for location in locations:

            stock = response.json()['stock'][gpu][location]

            if stock['available_now'] > 0:
                # Send a message to a Slack channel
                response = slack_client.chat_postMessage(
                    channel="#mining",
                    text=f"GPU {gpu} at location {location} is available. Stock: {stock['available_now']}"
                    )
            else:
                pass
                

if __name__ == "__main__":
    main()


