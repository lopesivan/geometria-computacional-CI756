class Interval(object):
    def __init__(self, x, x1, closed, semiclosed=False):
        if x < x1:
            self.left = x 
            self.right = x1
        else:
            self.left = x1
            self.right = x
        self.semiclosed = semiclosed
        self.closed = closed