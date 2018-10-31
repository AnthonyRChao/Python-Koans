#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    sides = sorted([a, b, c])
    
    if sides[0] == 0:
        raise TriangleError('All sides should be greater than 0')
    elif sides[0] < 0:
        raise TriangleError('All sides should be greater than 0')
    elif sides[0] + sides[1] < sides[2]:
        raise TriangleError('Sum of any two sides should be greater than the third')

    types = { 
        1: 'equilateral', 
        2: 'isosceles', 
        3: 'scalene'
    }
    
    num_uniq_sides = len(set(sides))
    return types[num_uniq_sides]

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
