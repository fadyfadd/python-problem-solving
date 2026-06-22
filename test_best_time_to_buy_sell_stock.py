from typing import List


class StockUtility:

    def buy_sell_stock(self, prices: List[float]) -> float:

        min_price = float('inf')
        max_gain = 0

        for (i, price) in enumerate(prices):
            max_gain = max(max_gain, price - min_price)

            if price < min_price:
                min_price = price

        return max_gain


import unittest

class UnitTests(unittest.TestCase):

    def test_basic_profit(self):
        stock = StockUtility()
        self.assertEqual(stock.buy_sell_stock([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit(self):
        stock = StockUtility()
        self.assertEqual(stock.buy_sell_stock([7, 6, 4, 3, 1]), 0)

    def test_increasing(self):
        stock = StockUtility()
        self.assertEqual(stock.buy_sell_stock([1, 2, 3, 4, 5]), 4)

    def test_single_day(self):
        stock = StockUtility()
        self.assertEqual(stock.buy_sell_stock([5]), 0)

    def test_constant_prices(self):
        stock = StockUtility()
        self.assertEqual(stock.buy_sell_stock([3, 3, 3, 3]), 0)


min_price = float('inf')
x = min_price - 1
print(x)