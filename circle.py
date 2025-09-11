import math

def circum(radius):
    return 2 * math.pi * radius

radius = int(input("Enter the radius of the circle: "))
print(circum(radius), "is the circumference of the circle of radius", radius)
