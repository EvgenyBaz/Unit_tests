class Shop:

    def __init__(self, products: list):
        self.products = products

    def get_products(self):
        return self.products

    def set_products(self, products):
        self.products = products

    # @return отсортированный по возрастанию и цене список продуктов
    def sort_products_by_price(self):
        return sorted(self.products, key=lambda x: x.cost)

    # @return самый дорогой продукт
    def get_most_expensive_product(self):
        return max(self.products, key=lambda x: x.cost)