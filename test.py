#!/usr/bin/python3
"""
# ---------------------------------------------------------------------------
# Name:        test.py
# Purpose:     To test functions defined in the currency_converter package.
#
# Author:      Ashwin_Tendulkar
#
# Created:     30/06/2019
# ---------------------------------------------------------------------------
"""
import unittest

import currency_converter as cc


class TestFunctions(unittest.TestCase):

    def test_get_currency_codes(self):
        """Testing function 'get_currency_codes'"""
        self.assertEqual(
            cc.get_currency_codes(),
            ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK',
             'RON', 'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK',
             'JPY', 'THB', 'CHF', 'EUR', 'MYR', 'BGN', 'TRY',
             'CNY', 'NOK', 'NZD', 'ZAR', 'USD', 'MXN', 'SGD',
             'AUD', 'ILS', 'KRW', 'PLN'])

    def test_get_fullname(self):
        """Testing function 'get_fullname'"""
        self.assertEqual(cc.get_fullname('USD'), 'US dollar')

    def test_get_fullname_invalid(self):
        """Testing function 'get_fullname'"""
        self.assertIn('Invalid', cc.get_fullname('US'))


def main():
    # cc.display_all_currency_code()
    # print(cc.get_currency_codes())
    print(cc.get_rate_per_unit('USD', 'INR'))
    # print(cc.get_fullname('US'))
    # print(cc.currency_converter('USD', 'EUR', 41))
    pass


if __name__ == '__main__':
    # unittest.main()
    main()
