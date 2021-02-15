import requests

def getSpotprice(headers):

    url = "https://jsonrpc.barry.energy/json-rpc#Get%20Spotprice"

    payload = {
      "method": "co.getbarry.api.v1.OpenApiController.getPrice",
      "id": 0,
      "jsonrpc": "2.0",
      "params": [
        "DK_NORDPOOL_SPOT_DK1",
        headers[1],
        headers[2]
      ]
    }

    return requests.post(url, json=payload, headers=headers[0]).json()