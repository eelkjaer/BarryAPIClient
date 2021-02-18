def createHeader(apitoken, fromdate, todate, pricezone):
    apiHeader = {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + apitoken
    }

    return [apiHeader, fromdate, todate, pricezone]


def dateFormat(date):
    return date.strftime("%Y-%m-%dT%H:%M:%SZ")