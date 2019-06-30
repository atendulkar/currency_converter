#!/usr/bin/python3
"""
# ---------------------------------------------------------------------------
# Name:        global_vars.py
# Purpose:     To declare global variables.
#
# Author:      Ashwin_Tendulkar
#
# Created:     28/06/2019
# ---------------------------------------------------------------------------
"""

# Exchange rate url
BASE_URL = "https://api.exchangeratesapi.io/latest?base={currency}"

# Valid currency list.
# This data is taken from https://fxtop.com/en/countries-currencies.php
VALID_CURRENCY_LIST = {"CAD": "Canadian dollar",
                       "HKD": "Hong Kong dollar",
                       "ISK": "Icelandic króna",
                       "PHP": "Philippine peso",
                       "DKK": "Danish krone",
                       "HUF": "Hungarian forint",
                       "CZK": "Czech koruna",
                       "RON": "Romanian new Leu",
                       "SEK": "Swedish krona",
                       "IDR": "Indonesian rupiah",
                       "INR": "Indian rupee",
                       "BRL": "Brazilian real",
                       "RUB": "Russian ruble",
                       "HRK": "Croatian kuna",
                       "JPY": "Japanese yen",
                       "THB": "Thai baht",
                       "CHF": "Swiss franc",
                       "EUR": "Euro",
                       "MYR": "Malaysian ringgit",
                       "BGN": "Bulgarian lev",
                       "TRY": "Turkish lira",
                       "CNY": "Chinese yuan renminbi",
                       "NOK": "Norwegian krone",
                       "NZD": "New Zealand dollar",
                       "ZAR": "South African rand",
                       "USD": "US dollar",
                       "MXN": "Mexican peso",
                       "SGD": "Singapore dollar",
                       "AUD": "Australian dollar",
                       "ILS": "Israeli new shekel",
                       "KRW": "South Korean won",
                       "PLN": "Polish zloty"}
