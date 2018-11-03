# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by *** and Eric Martin for COMP9021


from math import pi, hypot


class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({:.2f}, {:.2f})'.format(self.x, self.y)

class Disk():
    def __init__(self,*, centre = Point(0, 0), radius = 0):
        self.centre = centre
        self.radius = radius
        self.area = pi*(radius**2)

##    def print_area(self):
##        print ('the area of the disk is:{}'.format(self.area))

    def __repr__(self):
        return 'Disk({},{:.2f})'.format(self.centre, self.radius)
    
    def intersects(self,disk):
        between_centres = hypot(abs(self.centre.x - disk.centre.x),abs(self.centre.y - disk.centre.y))
##        print(between_centres)
        if between_centres <= abs(self.centre.x + disk.centre.x):
            return True
        else:
            return False

    def absorb(self,disk):
        between_centres = hypot(abs(self.centre.x - disk.centre.x),abs(self.centre.y - disk.centre.y))
        
        if between_centres > abs(self.radius - disk.radius):
            theta = 1/2 + abs(self.radius - disk.radius)/(2*between_centres)
            new_x = (1-theta)*self.centre.x + (theta*disk.centre.x)
            new_y = (1-theta)*self.centre.y + (theta*disk.centre.y)
            new_radius = (between_centres + disk.radius + self.radius)/2
            return Disk(centre = Point(new_x,new_y),radius = new_radius)
        else:
            # self absorb disk
            if self.radius >= disk.radius:
                new_x = self.centre.x
                new_y = self.centre.y
                new_radius = self.radius
                return Disk(centre = Point(new_x,new_y),radius = new_radius)
            # disk absorb self
            else:
                new_x = disk.centre.x
                new_y = disk.centre.y
                new_radius = disk.radius
                return Disk(centre = Point(new_x,new_y),radius = new_radius)
    
    def change_radius(self, r):
        self.radius = r
        self.area = pi*(r**2) 
