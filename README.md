<h1 align="center">Welcome to Barry Energy API Client 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://travis-ci.com/eelkjaer/BarryAPIClient" target="_blank">
    <img alt="Build status" src="https://travis-ci.com/eelkjaer/BarryAPIClient.svg?branch=main" />
  </a>
</p>

> Simple python package to work with the API of Barry Energy. 
> The API documentation can be found [here](https://developer.barry.energy).

> Please be aware that this project is <u>NOT</u> offical.

## Install

```sh
pip3 install barry-energy-api
```

## Usage

#### Get your API Token
```sh
Get from mobile app under "Add-ons" -> "Barry API"
```
<br>

1. Import the package
```python
from barry_energy_api import PriceZone, BarryEnergyAPI
```
2. Initialize the API
```python
api = BarryEnergyAPI('api-token', 5, PriceZone.DK_EAST)
```
3. Get aggregated consumption for the last 5 days as defined when API was initialized.
```python
api.consumption()
```
4. Get prices from the last two days.
##### Notice that methode has overloading
```python
api.spotprices(2)
```


## Author

👤 **Emil Elkjær Nielsen**

* Website: https://evsn.dk
* Github: [@eelkjaer](https://github.com/eelkjaer)
* LinkedIn: [@emil-elkjær](https://linkedin.com/in/emil-elkjær)


## Inspiration
Package setup [@Frankkkkk](https://github.com/Frankkkkk)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [Emil Elkjær Nielsen](https://github.com/eelkjaer) <br />
This project is [MIT](LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_