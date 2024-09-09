import unittest
from client3 import getDataPoint, getRatio

class TestClient3(unittest.TestCase):
    def test_getDataPoint(self):
        quote = {
            'stock': 'AAPL',
            'top_bid': {'price': '150.00'},
            'top_ask': {'price': '152.00'}
        }
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, 'AAPL')
        self.assertEqual(bid_price, 150.00)
        self.assertEqual(ask_price, 152.00)
        self.assertEqual(price, 151.00)

    def test_getRatio(self):
        ratio = getRatio(150.00, 100.00)
        self.assertEqual(ratio, 1.50)

if __name__ == '__main__':
    unittest.main()
