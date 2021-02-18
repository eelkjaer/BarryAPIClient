import os

from barry_energy_api import BarryEnergyAPI, PriceZone


class TestBarryEnergyAPI:
    api_token = os.environ['API_KEY']
    days = 5
    pricezone = PriceZone.DK_EAST
    api = BarryEnergyAPI(api_token, days, pricezone)

    def test_spotprices(self):
        assert "error" not in self.api.spotprices()

    def test_consumption(self):
        assert "error" not in self.api.spotprices()

    def test_meteringpoints(self):
        assert "error" not in self.api.spotprices()
