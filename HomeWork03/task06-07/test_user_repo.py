import unittest
from user import User
from user_repo import UserRepository


class UserRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository()
        self.user = User("username", "password")
        self.user_repository.add_user(self.user)

    def test_add_user(self):
        self.assertEqual(len(self.user_repository.data), 1)
        self.assertTrue(self.user in self.user_repository.data)

    def test_find_by_name_true(self):
        result = self.user_repository.find_by_name("username")
        self.assertTrue(result)

    def test_find_by_name_false(self):
        result = self.user_repository.find_by_name("username2")
        self.assertFalse(result)

    def test_find_by_name_false_2(self):
        self.user_repository.data = []
        result = self.user_repository.find_by_name("username")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
