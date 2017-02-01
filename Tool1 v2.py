from __future__ import division
import turtle
from math import *


def calculate_angles(A, B, C, a, b, c, flag):
    # print "a = ", int(degrees(a)), "b = ", int(degrees(b))
    if flag == 1:
        # print "a = 60"
        b = atan(sin(a)/(C/B - cos(a)))
        c = pi - a - b
        A = B * (sin(a)/sin(b))
        result = [a, b, c, A]
        return result
    elif flag == 0:
        # print "b = 60"
        a = atan(sin(b)/(C/A - cos(b)))
        c = pi - a - b
        B = A * (sin(b)/sin(a))
        result = [a, b, c, B]
        return result
    elif flag == -1:
        C = A * (sin(c)/sin(a))
        return [a, b, c, C]


def draw_sierpinski(A, B, C, a, b, c, depth=2, n=2.0, flag=1):
    # print A, B, C, "Hello", [a, b, c]
    [a, b, c, side] = calculate_angles(A, B, C, a, b, c, flag)
    if flag == 1:
        A = side
    elif flag == 0:
        B = side
    elif flag == -1:
        C = side
    # print "CALCULATED ", [a, b, c]
    if depth == 0:
        t.fd(C)
        t.left(degrees(pi - b))
        t.fd(A)
        t.left(degrees(pi - c))
        t.fd(B)
        t.left(degrees(pi - a))

    else:
        # draw_sierpinski(A, B/n, C/2, a, b, c, depth-1, n, 1)
        draw_sierpinski(A, ((n - 1) * B)/n, C/2, a, b, c, depth-1, n, 1)
        t.fd(C/2)
        # draw_sierpinski(A/n, B, C/2, a, b, c, depth-1, n, 0)
        draw_sierpinski(((n - 1) * A)/n, B, C/2, a, b, c, depth-1, n, 0)
        t.bk(C/2)
        t.left(degrees(a))
        t.fd(((n - 1) * B)/n)
        t.right(degrees(a))
        # draw_sierpinski(((n - 1) * A)/n, ((n - 1) * B)/n, ((n - 1) * C)/n, a, b, c, depth-1, n, -1)
        draw_sierpinski(A/n, B/n, C/n, a, b, c, depth-1, n, -1)
        t.left(degrees(a))
        t.bk(((n - 1) * B)/n)
        t.right(degrees(a))

# Triangles will be of different sides
l = int(input('Side of base triangle: '))
assert (l > 0), "Side of the Triangle should be greater than zero."
d = int(input('Iterations: '))
assert (d >= 0), "Number of iterations should be non-negative"
scale = float(input('Scale factor: '))
assert (scale > 1), "Scale factor should be greater than 1."

window = turtle.Screen()
t = turtle.Turtle()
draw_sierpinski(l, l, l, radians(60), radians(60), radians(60), d, scale)
window.exitonclick()
