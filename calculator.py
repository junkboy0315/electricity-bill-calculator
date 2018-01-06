"""
Calculate Electricity Bills and exports as csv
"""

import math

import pandas as pd

VALID_VENDOR_LIST = ('chuden', 'htb', 'koyo', 'sanix', 'looop', 'mitsuuroko')

class PriceCalculator(object):
    def get_price_chuden(self, kwh):
        base_price = 331.23
        rate_range1 = 20.40 # from 15kwh to 120kwh
        rate_range2 = 26.96 # from 120kwh to 300kwh
        rate_range3 = 29.04 # above 300kwh

        fullprice_range1 = rate_range1 * 105
        fullprice_range2 = rate_range2 * 180

        price = 0

        if kwh > 300:
            price = base_price + fullprice_range1 + fullprice_range2 + (kwh - 300) * rate_range3
        elif kwh > 120:
            price = base_price + fullprice_range1 + (kwh - 120) * rate_range2
        elif kwh > 15:
            price = base_price + (kwh - 15) * rate_range1
        elif kwh >= 0:
            price = base_price

        return price

    def get_price_htb(self, kwh):
        base_price = 313.75
        rate_range1 = 19.33 # from 15kwh to 120kwh
        rate_range2 = 25.56 # from 120kwh to 300kwh
        rate_range3 = 27.54 # above 300kwh

        fullprice_range1 = rate_range1 * 105
        fullprice_range2 = rate_range2 * 180

        price = 0

        if kwh > 300:
            price = base_price + fullprice_range1 + fullprice_range2 + (kwh - 300) * rate_range3
        elif kwh > 120:
            price = base_price + fullprice_range1 + (kwh - 120) * rate_range2
        elif kwh > 15:
            price = base_price + (kwh - 15) * rate_range1
        elif kwh >= 0:
            price = base_price

        return price

    def get_price_koyo(self, kwh):
        base_price = 222.00
        rate_range1 = 20.34 # from 15kwh to 120kwh
        rate_range2 = 24.50 # from 120kwh to 300kwh
        rate_range3 = 27.20 # above 300kwh

        fullprice_range1 = rate_range1 * 105
        fullprice_range2 = rate_range2 * 180

        price = 0

        if kwh > 300:
            price = base_price + fullprice_range1 + fullprice_range2 + (kwh - 300) * rate_range3
        elif kwh > 120:
            price = base_price + fullprice_range1 + (kwh - 120) * rate_range2
        elif kwh > 15:
            price = base_price + (kwh - 15) * rate_range1
        elif kwh >= 0:
            price = base_price

        return price

    def get_price_sanix(self, kwh):
        base_price = 6125.00
        rate = 24.50 # above 250kwh

        price = 0

        if kwh > 250:
            price = base_price + rate * (kwh - 250)
        elif kwh >= 0:
            price = base_price

        return price

    def get_price_looop(self, kwh):
        rate = 24.00
        return rate * kwh

    def get_price_mitsuuroko(self, kwh):
        base_price = 331.23
        rate_range1 = 22.40 # from 15kwh to 120kwh
        rate_range2 = 24.13 # from 120kwh to 300kwh
        rate_range3 = 25.76 # above 300kwh

        fullprice_range1 = rate_range1 * 105
        fullprice_range2 = rate_range2 * 180

        price = 0

        if kwh > 300:
            price = base_price + fullprice_range1 + fullprice_range2 + (kwh - 300) * rate_range3
        elif kwh > 120:
            price = base_price + fullprice_range1 + (kwh - 120) * rate_range2
        elif kwh > 15:
            price = base_price + (kwh - 15) * rate_range1
        elif kwh >= 0:
            price = base_price

        return price

    def get_price(self, vendor, kwh):
        """
        Args:
            vendor (string): target vendor
            kwh (int | float): target kWh

        Returns:
            int: price at the target kwh (fractions omitted).

        Raises:
            ValueError: when `vendor` is unknown vendor name
                        when `kwh` type is other than int or float
                        when `kwh` is munus
        """

        # args validation
        if vendor not in VALID_VENDOR_LIST:
            raise ValueError('a vendor name is invalid.')
        elif not isinstance(kwh, int) and not isinstance(kwh, float):
            raise ValueError('a type of kwh must be int or float.')
        elif kwh < 0:
            raise ValueError('a value of kwh must be above 0.')

        # call specific function to get price by vendor.
        # function name must be 'get_price_****(vendor name)'
        get_price_for_specific_vendor = getattr(self, 'get_price_' + vendor)
        return math.floor(get_price_for_specific_vendor(kwh))

    def get_price_list(self, target_vendors, kwh_start, kwh_stop, kwh_step):
        """
        Args:
            target_vendors (list): target vendors you want to get price
            kwh_start (int): lowest kWh for calculation
            kwh_stop (int): highest kWh for calculation
            kwh_step (int): kWh step

        Returns:
            return price list for given vendors as follows:

            {
                'kwh_at': [100, 110, 120, 130, 140, 150],
                'chuden': [2065, 2269, 2473, 2742, 3012, 3282],
                'htb': [1956, 2150, 2343, 2598, 2854, 3110],
            }
        """

        # initial setup of list
        price_list = {'kwh_at': []}
        for vendor in target_vendors:
            price_list[vendor] = []

        # calc price
        for kwh in range(kwh_start, kwh_stop, kwh_step):
            price_list['kwh_at'].append(kwh)
            for vendor in target_vendors:
                price_list[vendor].append(self.get_price(vendor, kwh))

        return price_list

def main():
    """sample code for getting prices"""

    price_calculator = PriceCalculator()

    target_vendors = ['chuden', 'htb', 'koyo', 'sanix', 'looop', 'mitsuuroko']

    price_list = price_calculator.get_price_list(target_vendors, 100, 601, 10)

    df = pd.DataFrame(
        price_list,
        columns=['kwh_at'] + target_vendors
    )

    df.to_csv('result.csv', index=False)

if __name__ == "__main__":
    main()
