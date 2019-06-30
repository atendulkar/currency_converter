#!/usr/bin/python3
"""
# ---------------------------------------------------------------------------
# Name:        currency_converter.py
# Purpose:     To defined the currency converter APIs.
#
# Author:      Ashwin_Tendulkar
#
# Created:     28/06/2019
# ---------------------------------------------------------------------------
"""

from . import conversion_utils
from . import global_vars as gv


def get_currency_codes():
    """Method to get currency code supported by this library.
    @:return list: List of supported currency codes."""
    return conversion_utils.get_code()


def get_fullname(currency_code):
    """Function to get currency name for a given currency code.
    In case invalid code, function returns 'Invalid: Currency code.' message.
    @:param str currency_code: currency code
    @:return value str: Currency fullname."""

    # Validate currency code
    if currency_code not in get_currency_codes():
        return "Invalid: Currency code."
    return gv.VALID_CURRENCY_LIST[currency_code]


def display_all_currency_code():
    """Function to display all supported currencies by this
    implementation."""
    print("*"*50)
    print("List of currencies.")
    print("*"*50)
    for currency, full_name in gv.VALID_CURRENCY_LIST.items():
        print(currency, " -> ", full_name)
    print("*" * 50)
    print()


def get_rate_per_unit(from_currency, to_currency):
    """This function will return net amount for 'to_currency'
    w.r.t single unit of 'from_currency'.
    @:param str from_currency: Currency code for which you have
    @:param str to_currency: Currency code for which you want.
    @:return value int: Amount against single unit of 'from_currency'"""

    # Validate inputs
    if from_currency not in gv.VALID_CURRENCY_LIST:
        return "Invalid: inputs for 'from_currency'"
    if to_currency not in gv.VALID_CURRENCY_LIST:
        return "Invalid: inputs for 'to_currency'"

    # Build exchange rate url 'https://api.exchangeratesapi.io'
    url = gv.BASE_URL.format(currency=from_currency)

    # Get rates
    status, rates = conversion_utils.get_rates(url)

    # Checking for successful response.
    if not status:
        return "Invalid: Problem in getting rates."

    return rates.get("rates", dict()).get(to_currency, 0)


def currency_converter(from_currency, to_currency, amount):
    """Function to convert currency from 'from_currency' to
    'to_currency' for a given amount.
    @:param str from_currency: Currency code for which you have
    @:param str to_currency: Currency code for which you want.
    @:param float amount: Amount to be converted.
    @:return value int: Net amount after conversion."""

    # Get rate per unit.
    rate_per_unit = get_rate_per_unit(from_currency, to_currency)

    if isinstance(rate_per_unit, str):
        return "Invalid: value for 'rate_per_unit'"

    # Return net amount.
    return float(float("{0:.2f}".format(rate_per_unit)) * amount)
