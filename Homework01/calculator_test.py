import unittest
from calculator import Calculator


class EasyTest:

    def __init__(self):
        pass

    @staticmethod
    def test():
        if 8 != Calculator.calculation(2, 6, '+'):
            raise AssertionError("Ошибка в методе")

        if 0 != Calculator.calculation(2, 2, '-'):
            raise AssertionError("Ошибка в методе")

        if 14 != Calculator.calculation(2, 7, '*'):
            raise AssertionError("Ошибка в методе")

        if 2 != Calculator.calculation(100, 50, '/'):
            raise AssertionError("Ошибка в методе")

        try:
            Calculator.calculation(8, 4, '_')
        except:
            AssertionError("Ошибка в методе")

        assert 8 == Calculator.calculation(2, 6, '+')
        assert 0 == Calculator.calculation(2, 2, '-')
        assert 14 == Calculator.calculation(2, 7, '*')
        assert 2 == Calculator.calculation(100, 50, '/')


class CalculatorTest(unittest.TestCase):

    def test_result(self):
        self.assertEqual(90.0, Calculator.calculating_discount(purchase_amount=100, discount_amount=10))

    def test_zero_result(self):
        self.assertEqual(0, Calculator.calculating_discount(purchase_amount=0, discount_amount=10))

    def test_zero_discount(self):
        self.assertEqual(100, Calculator.calculating_discount(purchase_amount=100, discount_amount=0))

    def test_discount_less_0(self):
        self.assertEqual(105, Calculator.calculating_discount(purchase_amount=100, discount_amount=-5))

    def test_discount_more_100(self):
        self.assertEqual(-10, Calculator.calculating_discount(purchase_amount=100, discount_amount=110))

    def test_negative_amount(self):
        self.assertEqual(-50, Calculator.calculating_discount(purchase_amount=-100, discount_amount=50))


if __name__ == "__main__":
    EasyTest.test()
    unittest.main()
