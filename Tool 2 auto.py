from __future__ import division
from Tkinter import *
from math import sqrt
# Globals
f1 = 0  # Frequency 1
f2 = 0  # Frequency 2
f3 = 0  # Frequency 3
c = 299792458  # Speed of Light in m/s
x00 = 0  # x-coordinate Point 1
y00 = 0  # y-coordinate Point 1
x01 = 0  # x-coordinate Point 2
y01 = 0  # y-coordinate Point 2
x02 = 0  # x-coordinate Point 3
y02 = 0  # y-coordinate Point 3


################### Helper Functions ##########################################


def print_helper_triangle():
    print "\n"
    for i in range(10):
        if i < 9:
            if i == 0:
                print " "*5 + "P2 (Top Vertex)"
            print " "*(10-i) + "/" + " "*i*2 + "\\"
        else:
            print " "*(10-i) + "-"*(i*2 + 2)
            print "P1" + " "*(10-i+i*2+1) + "P3"
    print "\nRefer Above Figure for help in filling coordinates\n"


def midpoint(a1, a2, x):
    return (a1 + x*a2)/(x+1)


def draw_helper(canvas, level, x1, y1, x2, y2, x3, y3, scale):
        # print "Scale %f" %(scale)
        if level == 1:
            print '({0}, {1})'.format(x1, y1) + '({0}, {1})'.format(x2, y2) + '({0}, {1})'.format(x3, y3)
            canvas.create_polygon(x1, y1, x2, y2, x3, y3, width=1)
        else:
            x4 = midpoint(x1, x2, scale)
            x5 = midpoint(x2, x3, scale)
            x6 = midpoint(x3, x1, scale)
            y4 = midpoint(y1, y2, scale)
            y5 = midpoint(y2, y3, scale)
            y6 = midpoint(y3, y1, scale)
            draw_helper(canvas, level - 1, x1, y1, x4, y4, x6, y6, scale)
            draw_helper(canvas, level - 1, x4, y4, x2, y2, x5, y5, scale)
            draw_helper(canvas, level - 1, x6, y6, x5, y5, x3, y3, scale)


def calculate_scale_factor(freq1, freq2, freq3):
    assert(freq1 > 0 and freq2 > 0), "Frequencies should be non - negative"
    s1 = freq2/freq1
    if freq3 > 0:
        s2 = freq3/freq2
    elif freq3 < 0:
        assert False, "Frequencies should be non - negative"
    else:
        s2 = s1
    if (s1/s2 > 0.95) and (s1/s2 < 1.05):
        s = (s1+s2)/2
    else:
        assert False, "Frequencies should be proportionate."
    return s


def get_frequencies_and_calc_scale_factor():
    global f1, f2, f3
    print "Enter frequencies in ascending order"
    f1 = float(input('First Frequency(smallest, in GHz): '))
    print "\n"
    f2 = float(input('Second Frequency(GHz): '))
    print "\nDo you want to add third frequency? (Y/N)   "
    response = raw_input()
    if response == 'Y':
        f3 = float(input('Third Frequency(GHz), such that f3/f2 is same as f2/f1: '))
        print "\n"
    s = calculate_scale_factor(f1, f2, f3)
    return s


def calculate_side():
    global f1, c
    epsilon = float(input('Dielectric Constant: '))
    assert(epsilon > 1), "Relative permittivity should be greater than 1"
    print "\n"
    # fn = 0.3*(cos(flare_angle/2))*sqrt(2.5/epsilon)*(scale^n)
    a = ((0.3*c*(sqrt(2.5)))/(f1*1e9*(sqrt(epsilon)))) * 1e3  # in mm
    return a


def get_initial_coordinates(a):
    global x00, y00, x01, y01, x02, y02
    x00 = 0
    y00 = 0
    x01 = a/2
    y01 = (sqrt(3) * a)/2
    x02 = a
    y02 = 0


############################ Main ###############################################

canvas_width = 200
canvas_height = 200
python_green = "#476042"

# Print Helper Diagram for inputting coordinates
# ----------------------------------------------------------
# print_helper_triangle()
# ---------------------------------------------------------
# Get Input Coordinates, Iterations and Scale factor

# x00 = int(input('Point 1 (Base) X-coord: '))
# y00 = int(input('Point 1 (Base) Y-coord: '))
# print "\n"
# x01 = int(input('Point 2 (Top vertex) X-coord: '))
# y01 = int(input('Point 2 (Top vertex) Y-coord: '))
# print "\n"
# x02 = int(input('Point 3 (Base) X-coord: '))
# y02 = int(input('Point 3 (Base) Y-coord: '))
# print "\n"

# ---------------------------------------------------------
''' Get coordinates of the Sierpinski Gasket fractal given the input frequencies, Relative permittivity.
 Choice of giving 2 or 3 input frequencies.'''
itr = int(input('Iterations : '))
assert(itr >= 1), "Iterations should be greater than equal to 1"
print "\n"

n = get_frequencies_and_calc_scale_factor()
assert(n > 1), "Scale factor should be greater than 1"

side = calculate_side()

get_initial_coordinates(side)
# Create top level canvas
master = Tk()
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)

w.pack()
# w.xview_moveto(500-1)
# w.yview_moveto(500-1)


# points = [0, 0,canvas_width,canvas_height/2, 0, canvas_height]
# points = [x00, y00, x01, y01, x02, y02]
# print type(n)

# if (n-1)>=1:
#     N = (n-1)
# elif (n-1)>0 and (n-1)<1:
#     N = (1/(n-1))

# print type(N)
# draw_helper(w, 2, 0, 0,canvas_width,canvas_height/2, 0, canvas_height, n-1)
print "\n" + "="*25 + " Fractal Elements Coordinates " + "="*25 + "\n"
# draw_helper(w, itr, 0, 0,canvas_width,canvas_height/2, 0, canvas_height)

draw_helper(w, itr+1, x00, y00, x01, y01, x02, y02, n-1)

# w.create_polygon(points, outline=python_green,
#           fill='yellow', width=1)

mainloop()
