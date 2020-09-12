#assisgnment 6.2

import math
pi = math.pi
def volume (radius,height):
    return (1/3)*pi*radius*radius*height
def surfacearea (radius,slantheight):
    return pi*radius*slantheight+pi*radius*radius
radius = float(5)
height = float(12)
slantheight = float(10)
print("volume of cone :" ,volume(radius,height))
print("surface area of cone : " ,surfacearea(radius,slantheight))

"""
output

volume of cone : 314.15926535897927
surface area of cone :  235.61944901923448
"""














