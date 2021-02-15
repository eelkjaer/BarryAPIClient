import requests

def getConsumption(headers):

  url = "https://jsonrpc.barry.energy/json-rpc#Get%20Aggeregated%20Consumption"

  payload = {
    "method": "co.getbarry.api.v1.OpenApiController.getAggregatedConsumption",
    "id": 0,
    "jsonrpc": "2.0",
    "params": [
      headers[1],
      headers[2]
    ]
  }

  return requests.post(url, json=payload, headers=headers[0]).json()