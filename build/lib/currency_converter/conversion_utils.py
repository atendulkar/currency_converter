#!/usr/bin/python3
"""
# ---------------------------------------------------------------------------
# Name:        conversion_utils.py
# Purpose:     To implement utility functions. This utility contains banner
#              and get rate functions.
#
# Author:      Ashwin_Tendulkar
#
# Created:     27/06/2019
# ---------------------------------------------------------------------------
"""
import requests

from. import global_vars as gv


def get_rates(url):
    """Method to get currency rates and returns status of request(boolean)
     and request response in JSON format.
    @:param str url: Exchange site url
    @:return boolean: True for successful response, else False.
    @:return dict: Response in case of success else empty dict.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return True, response.json()
    return False, dict()


def get_code():
    """To get currency codes supported by this implementation.
    @:return list: List of supported currency codes."""
    return [code for code in gv.VALID_CURRENCY_LIST]
