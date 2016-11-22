class Segment(object):
    def __init__(self, id, x1, x2, y1, y2):
        self.id = id
        if y1 > y2:
            self.upper = Point(x1, y1, self)
            self.lower = Point(x2, y2, self)
            if x1 < x2:
                self.left = Point(x1, y1, self)
                self.right = Point(x2, y2, self)
            else:
                self.left = Point(x2, y2, self)  
                self.right = Point(x1, y1, self)
        else:
            self.upper = Point(x2, y2, self)
            self.lower = Point(x1, y1, self)
            if x2 < x1:
                self.left = Point(x2, y2, self)
                self.right = Point(x1, y1, self)
            else:
                self.left = Point(x1, y1, self)
                self.right = Point(x2, y2, self)
        self.reported = False