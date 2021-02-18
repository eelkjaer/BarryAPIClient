import enum

from barry_energy_api.entities import meteringpoints, spotprice, consumption
from barry_energy_api.entities.consumption import getConsumption
from barry_energy_api.entities.meteringpoints import getMeteringPoints
from barry_energy_api.entities.spotprice import getSpotprice
from barry_energy_api.utils import dateFormat, createHeader
from datetime import datetime, timedelta


class BarryException(Exception):
    pass

class PriceZone(enum.Enum):
    """
    DK_WEST = West Denmark (zip-code below 4999)
    DK_EAST = East Denmark (zip-code above 5000)
    FRANCE = Self explanatory
    """
    DK_WEST = "DK_NORDPOOL_SPOT_DK1"
    DK_EAST = "DK_NORDPOOL_SPOT_DK2"
    FRANCE = "FR_EPEX_SPOT_FR"


class BarryEnergyAPI:
    def __init__(self, api_token: str, pastdays: int, pricezone: PriceZone):
        # Sets the API key
        self.api_token = api_token
        self.pricezone = pricezone.value

        # Set the date range
        self.todate = datetime.utcnow()
        self.fromdate = dateFormat(self.todate - timedelta(days=pastdays))
        self.todate = dateFormat(self.todate)

        # Creates HTTP header
        self.header = createHeader(self.api_token, self.fromdate, self.todate, self.pricezone)

    def set_startdate(self, pastdays: int):
        """
        Changes the date which measuring is happening from.
        :param pastdays:
        Days before today
        """
        self.fromdate = dateFormat(datetime.utcnow() - timedelta(days=pastdays))

    def spotprices(self, pastdays=None):
        """
        Gives the spot prices in the specified from/to range.
        Spot prices are delivered ahead of our current time, up to 24 hours ahead.
        The price is excluding VAT and tarrifs.
        """
        try:
            headers = self.header
            if pastdays is not None:
                headers[1] = dateFormat(datetime.utcnow() - timedelta(days=pastdays))
            return getSpotprice(headers)
        except Exception as ex:
            raise BarryException(str(ex))

    def consumption(self, pastdays=None):
        """
        Gives the consumption on an hourly resolution.
        It accepts a past from and to date and MPID/PDL as input.

        Note that it will not return any data unless one is a Barry customer.
        The data usually has two to three days of delay, which is a limitation of the regulatory authorities.
        """
        try:
            headers = self.header
            if pastdays is not None:
                headers[1] = dateFormat(datetime.utcnow() - timedelta(days=pastdays))
            return getConsumption(headers)
        except Exception as ex:
            raise BarryException(str(ex))

    def meteringpoints(self, pastdays=None):
        """
        Gives information on all of your metering points subscribed to Barry.
        This method contains metadata on your metering points, including the price area and the MPID/PDL (Metering Point Identification).
        """
        try:
            headers = self.header
            if pastdays is not None:
                headers[1] = dateFormat(datetime.utcnow() - timedelta(days=pastdays))
            return getMeteringPoints(headers)
        except Exception as ex:
            raise BarryException(str(ex))
