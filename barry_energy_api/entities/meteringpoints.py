import requests


def getMeteringPoints(headers):
    url = "https://jsonrpc.barry.energy/json-rpc#Get%20MeteringPoints"

    payload = {
        "method": "co.getbarry.api.v1.OpenApiController.getMeteringPoints",
        "id": 0,
        "jsonrpc": "2.0",
        "params": []
    }

    return requests.post(url, json=payload, headers=headers[0]).json()
