import unittest

from HW1.Classify_Triangle import classify_Triangle


class Test(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_Triangle(1,1,1), "The Triangle is equilateral but the triangle is not a right triangle")
    def test_iso(self):
        self.assertEqual(classify_Triangle(3,2,2), "The Triangle is isosceles but the triangle is not a right triangle")
    def test_iso_front_two(self):
        self.assertEqual(classify_Triangle(7,7,4), "The Triangle is isosceles but the triangle is not a right triangle")
    def test_iso_edges(self):
        self.assertEqual(classify_Triangle(5,2,5), "The Triangle is isosceles but the triangle is not a right triangle")
    def test_scalineNotRight(self):
        self.assertEqual(classify_Triangle(1,2,3), "The Triangle is scalene but the triangle is not a right triangle")
    def test_scalineRight(self):
        self.assertEqual(classify_Triangle(5,4,3), "The Triangle is scalene and the triangle is a right triangle")
    def test_rightMiddleNumIsLargest(self):
        self.assertEqual(classify_Triangle(3,5,4), "The Triangle is scalene and the triangle is a right triangle")
    def test_rightLastNumIsLargest(self):
        self.assertEqual(classify_Triangle(3,4,5), "The Triangle is scalene and the triangle is a right triangle")
