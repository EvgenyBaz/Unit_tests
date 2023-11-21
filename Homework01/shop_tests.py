import unittest

from product import Product
from shop import Shop


class ShopTest(unittest.TestCase):

    def setUp(self) -> None:

        self.product_list = [Product('prod1', 1),
                             Product('prod2', 2),
                             Product('prod3', 4),
                             Product('prod4', 3)]
        self.shop = Shop(self.product_list)

    def test_sort_products_by_price(self):
        prod_list = self.shop.sort_products_by_price()
        print(*[item for item in prod_list], sep="\n") # визуальная проверка :)

        temporary_price = -1
        for product in prod_list:
            self.assertGreaterEqual(product.cost, temporary_price)
            temporary_price = product.cost


    def test_most_expensive_product(self):
        self.assertEqual(self.shop.get_most_expensive_product().cost, max(self.product_list, key=lambda x: x.cost).cost)


if __name__ == "__main__":
    unittest.main()
