import sys
sys.path.append("..")
from unittest import TestCase
import unittest
import cloudPC as cl

class Test(TestCase):
    def test_register(self):
        self.assertTrue(cl.register('abcd3233546','bbb'))

    def test_upload(self):
        self.assertTrue(cl.upload('bbb','bbb'))

    def test_download(self):
        self.assertTrue(cl.download('bbb','bbb'))

if __name__ == '__main__':
    unittest.main()
