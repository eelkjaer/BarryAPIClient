def createHeader(fromdate, todate):

    from credentials import getApiKey
    apiKey = getApiKey() #Simply returns a String with the API key from Barry

    apiHeader = {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + apiKey
    }

    return [apiHeader, fromdate, todate]


def dateFormat(date):
    return date.strftime("%Y-%m-%dT%H:%M:%SZ")