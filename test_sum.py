import unittest
from Lab1 import sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        input_data=[3,4,5]
        result=sum(input_data)
        self.assertEqual(result,12)

        self.assertEqual(sum([]),0)

if __name__=="__main__":
    unittest.main()