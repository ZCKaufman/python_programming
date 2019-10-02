import unittest

class TestReverseWords(unittest.TestCase):

    def test_reversewords(self):
        self.reverseWords('Zachary Kaufman'.upper(), 'Kaufman Zachary')
