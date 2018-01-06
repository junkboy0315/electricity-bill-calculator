import unittest
import calculator

class TestPriceCalculator(unittest.TestCase):

    def test_get_price(self):
        price_calculator = calculator.PriceCalculator()

        # validation (check if vendor name is wrong)
        self.assertRaises(ValueError, lambda: price_calculator.get_price('wrong vendor name', 0))

        # validation (kWh must be >0)
        self.assertRaises(ValueError, lambda: price_calculator.get_price('chuden', -1))

        #validation (kWh must be int or float)
        self.assertRaises(ValueError, lambda: price_calculator.get_price('chuden', 'wrong kWh'))

        # chuden
        self.assertEqual(price_calculator.get_price('chuden', 0), 331)
        self.assertEqual(price_calculator.get_price('chuden', 20), 433)
        self.assertEqual(price_calculator.get_price('chuden', 200), 4630)
        self.assertEqual(price_calculator.get_price('chuden', 400), 10230)

        # htb
        self.assertEqual(price_calculator.get_price('htb', 0), 313)
        self.assertEqual(price_calculator.get_price('htb', 20), 410)
        self.assertEqual(price_calculator.get_price('htb', 200), 4388)
        self.assertEqual(price_calculator.get_price('htb', 400), 9698)

        # koyo
        self.assertEqual(price_calculator.get_price('koyo', 0), 222)
        self.assertEqual(price_calculator.get_price('koyo', 20), 323)
        self.assertEqual(price_calculator.get_price('koyo', 200), 4317)
        self.assertEqual(price_calculator.get_price('koyo', 400), 9487)

        # sanix
        self.assertEqual(price_calculator.get_price('sanix', 0), 6125)
        self.assertEqual(price_calculator.get_price('sanix', 20), 6125)
        self.assertEqual(price_calculator.get_price('sanix', 200), 6125)
        self.assertEqual(price_calculator.get_price('sanix', 400), 9800)

        # looop
        self.assertEqual(price_calculator.get_price('looop', 0), 0)
        self.assertEqual(price_calculator.get_price('looop', 20), 480)
        self.assertEqual(price_calculator.get_price('looop', 200), 4800)
        self.assertEqual(price_calculator.get_price('looop', 400), 9600)

        # mitsuuroko
        self.assertEqual(price_calculator.get_price('mitsuuroko', 0), 331)
        self.assertEqual(price_calculator.get_price('mitsuuroko', 20), 443)
        self.assertEqual(price_calculator.get_price('mitsuuroko', 200), 4613)
        self.assertEqual(price_calculator.get_price('mitsuuroko', 400), 9602)

    def test_get_price_list(self):
        price_calculator = calculator.PriceCalculator()

        target_vendors = ['chuden', 'htb', 'sanix', 'looop']
        price_list = price_calculator.get_price_list(target_vendors, 100, 151, 10)

        # returns `dict` type value
        self.assertEqual(isinstance(price_list, dict), True)

        # list contains right keys
        self.assertEqual(price_list.keys(), {'kwh_at', 'chuden', 'htb', 'sanix', 'looop'})

        # list contains right array
        self.assertEqual(price_list['kwh_at'], [100, 110, 120, 130, 140, 150])
        self.assertEqual(len(price_list['chuden']), 6)
        self.assertEqual(len(price_list['htb']), 6)
        self.assertEqual(len(price_list['sanix']), 6)
        self.assertEqual(len(price_list['looop']), 6)

if __name__ == "__main__":
    unittest.main()
