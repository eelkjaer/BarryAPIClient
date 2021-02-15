from datetime import datetime, timedelta
from utils import createHeader, dateFormat
from consumption import getConsumption
from meteringpoints import getMeteringPoints
from spotprice import getSpotprice


## Set dates
fromdate = datetime.utcnow()
todate = dateFormat(fromdate - timedelta(days=1))
fromdate = dateFormat(fromdate)
##

## Create list with API header and required date range.
header = createHeader(fromdate, todate)

## API calls
consumption = getConsumption(header)
meteringpoints = getMeteringPoints(header)
spotprice = getSpotprice(header)


## Show results
print("Your metering point(s):")
print(meteringpoints)

print("Your spot price:")
print(spotprice)

print("Current consumption:")
print(consumption)
