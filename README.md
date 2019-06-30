# Currency Converter
___

Currency Converter is a package developed in Python for dealing with currency exchange. This package will provide some basic API for currency exchange related operation.

## Getting Started
___
### Prerequisites
Python

### Installation

For installation use below command.
* Step1:
    * Download/Copy wheel file(currency_converter-1.0.0-py3-none-any.whl) from 'dist'
    * Run 'python3 -m pip install currency_converter-1.0.0-py3-none-any.whl' or 'pip install currency_converter-1.0.0-py3-none-any.whl'
* step2:
    *  python setup.py install
    *  pip install -r requirements.txt

### Python API

Import the package and use API as below:
* import currency_converter as cc
* cc.display_all_currency_code()
* print(cc.get_currency_codes())
* print(cc.get_rate_per_unit('USD', 'INR'))
* print(cc.get_fullname('EUR'))
* print(cc.currency_converter('USD', 'EUR', 41))

## Contributing
___
Please refer CONTRIBUTING.md for more details.

## Versioning
___
We use GitHub for versioning.

## Authors
___
* Ashwin Tendulkar -- initial work
## License
___
This project is licensed under the MIT License - see the LICENSE.md file for details

## References
___
Currency value fetching from URL https://api.exchangeratesapi.io
Valid currency reference taken from link https://fxtop.com/en/countries-currencies.php for development.
