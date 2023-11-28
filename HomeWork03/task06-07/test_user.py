import unittest
from user import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Ivan", "qwerty")

    def test_constructor(self):
        self.assertEqual(self.user.get_name(), "Ivan")
        self.assertEqual(self.user.get_password(), "qwerty")
        self.assertFalse(self.user.is_authenticated())

    def test_authenticate(self):
        self.assertTrue(self.user.authenticate("Ivan", "qwerty"))
        self.assertFalse(self.user.authenticate("Ivan", "123qwe"))
        self.assertFalse(self.user.authenticate("Petr", "qwe123"))

    def test_set_name(self):
        self.user.set_name("Petr")
        self.assertEqual(self.user.get_name(), "Petr")

    def test_set_password(self):
        self.user.set_password("newPassword")
        self.assertEqual(self.user.get_password(), "newPassword")

    def test_is_authenticated(self):
        self.assertFalse(self.user.is_authenticated())
        self.user.set_authenticated(True)
        self.assertTrue(self.user.is_authenticated())


if __name__ == '__main__':
    unittest.main()