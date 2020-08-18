import unittest
import BoundedBoxes

class TestBoundedBoxesMethods(unittest.TestCase):
    def setUp(self):
        self.instance = BoundedBoxes

    def tearDown(self):
        self.instance = None

    def test_inside_box(self):
        rectange = [(2, 2), (4, 4)]
        boxes = [[(0, 0), (2, 2)]]
        
        bounded_box = self.instance.find_bounded_boxes(rectange, boxes)
        print(bounded_box)

if __name__ == '__main__':
    unittest.main()