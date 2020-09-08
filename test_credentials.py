import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.credential = Credential("mercy", "mercie", "twitter.com")  # create credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.credential.username, "mercy")
        self.assertEqual(self.credential.password, "mercie")
        self.assertEqual(self.credential.website, "twitter.com")


if __name__ == '__main__':
    unittest.main()
