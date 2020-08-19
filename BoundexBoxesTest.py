import unittest
import BoundedBoxes
from BoundedBoxes import Rectangle, Point

class TestBoundedBoxesMethods(unittest.TestCase):
    def setUp(self):
        self.instance = BoundedBoxes

    def tearDown(self):
        self.instance = None

    def test_outside_box(self):
        selected_region = Rectangle(Point(2, 5), Point(5, 12))
        boxes = [Rectangle(Point(0, 0), Point(1, 1)), 
                 Rectangle(Point(2, 3), Point(1, 1)),
                 Rectangle(Point(5, 13), Point(7, 15)),
                 Rectangle(Point(6, 8), Point(7, 11)),
                 Rectangle(Point(0, 9), Point(1, 11)),]
        
        bounded_box = self.instance.find_bounded_boxes(selected_region, boxes)
        self.assertEqual([], bounded_box)
    
    def test_overlap_box(self):
        selected_region = Rectangle(Point(2, 5), Point(5, 12))
        boxes = [
                 Rectangle(Point(3, 9), Point(4, 10)), 
                 Rectangle(Point(2, 5), Point(5, 12)),
                 Rectangle(Point(3, 5), Point(5, 12)),
                 Rectangle(Point(1, 8), Point(3, 10)),
                 Rectangle(Point(3, 11), Point(4, 15)),
                ]
            
        expected = [
                 Rectangle(Point(2, 5), Point(5, 12)),
                 Rectangle(Point(3, 5), Point(5, 12)),
                 Rectangle(Point(1, 8), Point(3, 10)), 
                 Rectangle(Point(3, 9), Point(4, 10)),
                 Rectangle(Point(3, 11), Point(4, 15)),
                ]
        
        bounded_box = self.instance.find_bounded_boxes(selected_region, boxes)
        self.assertEqual(expected, bounded_box)
    
    def test_border_box(self):
        selected_region = Rectangle(Point(2, 5), Point(5, 12))
        boxes = [
                 Rectangle(Point(1, 12), Point(2, 14)),
                 Rectangle(Point(5, 12), Point(6, 16)),
                 Rectangle(Point(1, 7), Point(2, 10)),
                 Rectangle(Point(3, 2), Point(4, 5)),
                ]
        
        expected = [
            Rectangle(Point(3, 2), Point(4, 5)),
            Rectangle(Point(1, 7), Point(2, 10)),
            Rectangle(Point(1, 12), Point(2, 14)),
            Rectangle(Point(5, 12), Point(6, 16)),
        ]
        bounded_box = self.instance.find_bounded_boxes(selected_region, boxes)
        self.assertEqual(expected, bounded_box)

    def test_selected_box_complete_overlap(self):
            selected_region = Rectangle(Point(2, 5), Point(5, 12))
            boxes = [
                    Rectangle(Point(1, 3), Point(6, 13)),
                    Rectangle(Point(0, 0), Point(1, 13)),
                    Rectangle(Point(1, 1), Point(6, 4))
                    ]
            
            expected = [
                Rectangle(Point(1, 3), Point(6, 13))
            ]
            bounded_box = self.instance.find_bounded_boxes(selected_region, boxes)
            self.assertEqual(expected, bounded_box)

if __name__ == '__main__':
    unittest.main()