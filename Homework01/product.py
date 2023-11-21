class Product:

    def __init__(self, title: str, cost: int):
        self.title = title  # // Название
        self.cost = cost  # Стоимость продукта

    def get_name(self):
        return self.title

    def set_name(self, title):
        self.title = title

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def __str__(self):
        return f"title: {self.title}, cost={self.cost}"
