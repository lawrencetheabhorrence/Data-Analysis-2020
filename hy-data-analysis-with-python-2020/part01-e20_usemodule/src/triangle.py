" right triangle related methods "
# Enter you module contents here
from math import sqrt

__version__ = "1.0"
__author__ = "lawrencetheabhorrence"


def hypothenuse(a, b):
    " calculates the hypotenuse given the other sides of the right triangle "
    return sqrt(a*a + b*b)

def area(a, b):
    " calculates the area of a right triangle given lengths of two perpendicular line segs"
    return 0.5*a*b