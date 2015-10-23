import unittest

import octokit
from .util import MockOctokitTestCase

class TestApi(MockOctokitTestCase):
    def test_current_user(self):
        with self.recorder.use_cassette('current_user'):
            login = self.client.current_user.login
            assert login == self.login

if __name__ == '__main__':
    unittest.main()
