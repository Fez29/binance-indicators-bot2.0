from datamodels import TradingBotRequest, ResponseData
import requests
from shared import logger

async def buyOrderRequest(symbol, stop_loss, target_profit, buy_currency, buy_amount, url, indicator):
    try:
        request_data = TradingBotRequest(
            coin_symbol=symbol,
            stop_loss=stop_loss,
            target_profit=target_profit,
            buy_currency=buy_currency,
            buy_amount=buy_amount,
            indicator=indicator
        )
        # Convert the instance to a JSON string
        json_data = request_data.json()
        # Send the request with the JSON data
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json_data, headers=headers)

        detail = response.json().get("detail", {})
        response_data = ResponseData(
            status=response.json().get("status", detail.get("status", "")),
            buyOrderId=response.json().get("buyOrderId", detail.get("buyOrderId", "")),
            symbol=response.json().get("symbol", detail.get("symbol", "")),
            msg=response.json().get("msg", detail.get("msg", ""))
        )
        print(f"{response}")
        if response.status_code == 200:
            print(f"Request was successful! Response: {response_data}, BuyOrderId: {response_data.buyOrderId}")
            return response_data.buyOrderId
        else:
            print(f"Request failed with status code {response.status_code}. Response body: {response_data}")
            logger.error(f"Request failed with status code {response.status_code}. Response body: {response_data}")
    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(f"An error occurred: {e}")
        raise Exception(f"buyOrderRequest An error occurred: {e}")

