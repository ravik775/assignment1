'''
Given a set of bounding boxes and a rectangle R, Find all the bounding boxes that are
“covered” by the rectangle R, Please sort the output on y and then on x.
There are 8 bounding boxes and one rectangle R in the above picture, please let me know the
bounding boxes you think are “covered” by rectangle R.
NOTE : Please discuss the solution before implementation in Python
'''

def find_bounded_boxes(rectange, boxes):
    '''
    rectange is a [(x1,y1), (x2, y2)]
    boxes is a [[(x1,y1), (x2, y2)], [(x1,y1), (x2, y2)]]

    The point A is always outside of the rectangle and the point B is always at the center of the rectangle

    Assuming the rectangle is axis-aligned, this makes things pretty simple:

    The slope of the line is s = (Ay - By)/(Ax - Bx).

    If -h/2 <= s * w/2 <= h/2 then the line intersects:
    The right edge if Ax > Bx
    The left edge if Ax < Bx.
    If -w/2 <= (h/2)/s <= w/2 then the line intersects:
    The top edge if Ay > By
    The bottom edge if Ay < By.
    Once you know the edge it intersects you know one coordinate: x = Bx ± w/2 or y = By ± h/2 depending on which edge you hit. The other coordinate is given by y = By + s * w/2 or x = Bx + (h/2)/s.

    '''
    bounded_boxes = []


    bounded_boxes.sort(key=lambda bound: (bound[0][1], bound[1][1], bound[0][0], bound[1][0]))
    return bounded_boxes
    