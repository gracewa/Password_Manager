import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.user = User("mercy", "mercie")  # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.user.username, "mercy")
        self.assertEqual(self.user.password, "mercie")


if __name__ == '__main__':
    unittest.main()
