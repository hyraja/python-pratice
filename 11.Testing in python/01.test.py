import unittest
import testingpython01  # python file for testing


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = testingpython01.do_stuff(test_param)
        self.assertEqual(result, 15)


unittest.main()
