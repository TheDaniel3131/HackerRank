#!/bin/python3
import math
import os

# Python: Shape Classes with Area method

# Rectangle:
# Constructor for Rectangle must take two arguments that denote thelengths of the rectangle's side
# Class must have an area method that returns the area of the rectangle

class Rectangle:
    # Define constructor for Recntagle
    def __init__(self, length, width):
        self.length = length;
        self.width = width;
    
    # Find the area of the rectangle
    def area(self):
        return self.length * self.width;

# Constructor for Circle must take one argument that denotes the radius of the circle.
# Circle class must have an area method that returns the area of the circle. To implement the area method, use a precise Pi value, prefereably the constant math pi.

class Circle:
    # Define constructor for Circle
    def __init__(self, radius):
        self.radius = radius;
    
    # Find the area of the circle
    def area(self):
        return math.pi * (self.radius ** 2);

if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
