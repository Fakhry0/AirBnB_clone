import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class."""

    def test_user_instance(self):
        """Test if user is an instance of User."""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test user attributes."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes_types(self):
        """Test user attributes types."""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)


if __name__ == '__main__':
    unittest.main()
