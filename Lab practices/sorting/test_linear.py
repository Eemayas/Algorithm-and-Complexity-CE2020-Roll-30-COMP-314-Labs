import unittest
from counting_sort import counting_sort
from radix_sort import radix_sort
from bucket_sort import bucket_sort

class TestCounting(unittest.TestCase):
    def testCountingSort1(self):
        A = [2, 5, 3, 0, 2, 3, 0, 3]
        B = counting_sort(A)
        self.assertEqual(B, [0, 0, 2, 2, 3, 3, 3, 5])

    def testCountingSort2(self):
        A = []
        B = counting_sort(A)
        self.assertEqual(B, [])

    def testCountingSort3(self):
        A = [1]
        B = counting_sort(A)
        self.assertEqual(B, [1])

    def testCountingSort4(self):
        A = [4, 2, 2, 8, 3, 3, 1]
        B = counting_sort(A)
        self.assertEqual(B, [1, 2, 2, 3, 3, 4, 8])

    def testCountingSort5(self):
        A = [1, 4, 1, 2, 7, 5, 2]
        B = counting_sort(A)
        self.assertEqual(B, [1, 1, 2, 2, 4, 5, 7])

    def testCountingSort6(self):
        A = [10, 20, 10, 30, 20, 10]
        B = counting_sort(A)
        self.assertEqual(B, [10, 10, 10, 20, 20, 30])

    def testCountingSort7(self):
        A = [5, 4, 3, 2, 1]
        B = counting_sort(A)
        self.assertEqual(B, [1, 2, 3, 4, 5])

    def testCountingSort8(self):
        A = [0, 0, 0, 0]
        B = counting_sort(A)
        self.assertEqual(B, [0, 0, 0, 0])

    def testCountingSort9(self):
        A = [100, 200, 300, 400, 500]
        B = counting_sort(A)
        self.assertEqual(B, [100, 200, 300, 400, 500])

    def testCountingSort10(self):
        A = [0, 1, 0, 1, 0, 1]
        B = counting_sort(A)
        self.assertEqual(B, [0, 0, 0, 1, 1, 1])

    def testRadixSort1(self):
        A = radix_sort([5151, 84894984, 949494, 949, 94])
        self.assertEqual(A, [94, 949, 5151, 949494, 84894984])

    def testRadixSort2(self):
        A = radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
        self.assertEqual(A, [2, 24, 45, 66, 75, 90, 170, 802])

    def testRadixSort3(self):
        A = radix_sort([5, 3, 1, 4, 2])
        self.assertEqual(A, [1, 2, 3, 4, 5])

    def testRadixSort4(self):
        A = radix_sort([987654, 123456, 234567, 345678, 456789])
        self.assertEqual(A, [123456, 234567, 345678, 456789, 987654])
    
    def testBucketSort1(self):
        A = [0.100, 0.8, 0.9, .07, 0.6, 0.4, 0.6, 0.8, 0.4, 0.231, 0.884, 0.54]
        B = bucket_sort(A)
        self.assertEqual(B,[0.07, 0.1, 0.231, 0.4, 0.4, 0.54, 0.6, 0.6, 0.8, 0.8, 0.884, 0.9])
        
    def testBucketSort2(self):
        A = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
        B = bucket_sort(A)
        self.assertEqual(B, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    
    def testBucketSort3(self):
        A = [0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
        B = bucket_sort(A)
        self.assertEqual(B, [0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95])
    
    def testBucketSort4(self):
        A = [0.123, 0.456, 0.789, 0.321, 0.654, 0.987, 0.111, 0.999]
        B = bucket_sort(A)
        self.assertEqual(B, [0.111, 0.123, 0.321, 0.456, 0.654, 0.789, 0.987, 0.999])
    
    def testBucketSort5(self):
        A = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
        B = bucket_sort(A)
        self.assertEqual(B, [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])


if __name__ == "__main__":
    unittest.main()
