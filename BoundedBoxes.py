'''
Given a set of bounding boxes and a rectangle R, Find all the bounding boxes that are
“covered” by the rectangle R, Please sort the output on y and then on x.
There are 8 bounding boxes and one rectangle R in the above picture, please let me know the
bounding boxes you think are “covered” by rectangle R.
NOTE : Please discuss the solution before implementation in Python
'''
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        return isinstance(other, Point) and self._x == other._x and self._y == other._y

class Rectangle:

    def get_point1(self):
        return self._point1

    def get_point2(self):
        return self._point2

    def __init__(self, point1, point2):
        if point1.get_x() < point2.get_x():
            self._point1 = point1
            self._point2 = point2
        else:
            self._point1 = point2
            self._point2 = point1

        if point1.get_x() == point2.get_x() or point1.get_y() == point2.get_y():
            raise Exception("Not a valid Rectangle, Please specify diagonal points of rectangle")
    
    def __eq__(self, other):
        return isinstance(other, Rectangle) and self._point1 == other._point1 and self._point2 == other._point2

    def overlap(self, rectangle):
        '''
        Check whether the any side of given intersect
        '''
        if isinstance(rectangle, Rectangle):
            return ( (self._point1.get_x() <= rectangle._point2.get_x() and 
                      self._point2.get_x() >= rectangle._point1.get_x()) and
                      (self._point1.get_y() <= rectangle._point2.get_y() and 
                       self._point2.get_y() >= rectangle._point1.get_y())
                    )        

def find_bounded_boxes(selected_region, boxes):
    bounded_boxes = []
    for box in boxes: # boxes are instances of Rectangle
        #print("Overlap %s "%selected_region.overlap(box))
        if selected_region.overlap(box):
            bounded_boxes.append(box)
        bounded_boxes.sort(key=lambda box: (min(box.get_point1().get_y(), box.get_point2().get_y()),
                                        max(box.get_point1().get_y(), box.get_point2().get_y()),
                                        box.get_point1().get_x(),
                                        box.get_point2().get_x()))
    return bounded_boxes
    