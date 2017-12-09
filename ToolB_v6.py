from __future__ import division
from Tkinter import *
from math import sqrt, pow
import os
import glob
''' Calculates coordinates of Sierpinski Gasket Fractal elements. Input: Number of Iterations,
Frequencies of Operation (Two or Three), Dielectric Constant'''
'''v6 : Input base frequency and Scale factors'''
# Globals
f1 = 0  # Frequency 1

c = 299792458  # Speed of Light in m/s
x00 = 0  # x-coordinate Point 1
y00 = 0  # y-coordinate Point 1
x01 = 0  # x-coordinate Point 2
y01 = 0  # y-coordinate Point 2
x02 = 0  # x-coordinate Point 3
y02 = 0  # y-coordinate Point 3
count = 1
# dirname = "C:\Users\User\Desktop\Coordinates_Directory"
dirname = os.path.join(os.getcwd(), "Coordinates")

################### Helper Functions ##########################################


def helper():
    print "\nCalculates coordinates of Sierpinski Gasket Fractal elements based on required frequencies of operation" \
          ",number of iterations and Dielectric constant\n"


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


def divide_in_ratio(a1, a2, x):
    return (a1 + x*a2)/(x+1)


def midpoint(a1, a2):
    return (a1 + a2)/2


def draw_helper(canvas, level, x1, y1, x2, y2, x3, y3, scale1, scale2, a, h, switch):
        # print "Scale %f" %(scale)
        global count, dirname
        filename = dirname + '\Element_{0}.txt'.format(count)
        f = open(filename, 'w')
        if level == 1:
            s = '{0}, {1}\n'.format(x1 - a/2, y1 - h/3) + '{0}, {1}\n'.format(x2 - a/2, y2 - h/3) + \
                '{0}, {1}\n'.format(x3 - a/2, y3 - h/3)
            print s
            s += '{0}, {1}'.format(x1 - a/2, y1 - h/3)
            f.write(s + '\n')
            f.close()
            count += 1
            canvas.create_polygon(x1, y1, x2, y2, x3, y3, width=1)
        elif switch is True:
            x4 = divide_in_ratio(x1, x2, scale1)
            x5 = divide_in_ratio(x3, x2, scale1)
            x6 = midpoint(x3, x1)
            y4 = divide_in_ratio(y1, y2, scale1)
            y5 = divide_in_ratio(y3, y2, scale1)
            y6 = midpoint(y3, y1)
            draw_helper(canvas, level - 1, x1, y1, x4, y4, x6, y6, scale1, scale2, a, h, False)
            draw_helper(canvas, level - 1, x4, y4, x2, y2, x5, y5, scale1, scale2, a, h, False)
            draw_helper(canvas, level - 1, x6, y6, x5, y5, x3, y3, scale1, scale2, a, h, False)
        elif switch is False:
            x4 = divide_in_ratio(x1, x2, scale2)
            x5 = divide_in_ratio(x3, x2, scale2)
            x6 = midpoint(x3, x1)
            y4 = divide_in_ratio(y1, y2, scale2)
            y5 = divide_in_ratio(y3, y2, scale2)
            y6 = midpoint(y3, y1)
            draw_helper(canvas, level - 1, x1, y1, x4, y4, x6, y6, scale1, scale2, a, h, True)
            draw_helper(canvas, level - 1, x4, y4, x2, y2, x5, y5, scale1, scale2, a, h, True)
            draw_helper(canvas, level - 1, x6, y6, x5, y5, x3, y3, scale1, scale2, a, h, True)


def get_scale_factor():
    print "\nInfo: The program also supports two scale factors which will be used alternatively " \
          "in successive iterations to produce the structure\n"

    s1 = float(input('Scale factor(greater than 1): '))
    print "\nDo you want a mix scale design (Two scale factors). [Y/N]"
    response = raw_input()
    if response == 'Y' or response == 'y':
        s2 = float(input('Second Scale factor(greater than 1) : '))
    else:
        s2 = s1

    s = (s1, s2)
    return s


def get_frequencies_and_scale_factor():
    global f1
    f1 = float(input('Base Frequency(smallest, in GHz): '))
    assert(f1 > 0), "Base Frequency should be positive integer."
    s = get_scale_factor()
    return s


def calculate_side(h):
    global f1, c
    epsilon = float(input('Dielectric Constant: '))
    assert(epsilon > 1), "Relative permittivity should be greater than 1"
    print "\n"
    # fn = 0.3*(cos(flare_angle/2))*sqrt(2.5/epsilon)*(scale^n)
    # -----------------------------------------------------------
    # a = ((0.3*c*(sqrt(2.5)))/(f1*1e9*(sqrt(epsilon)))) * 1e3  # in mm
    # -----------------------------------------------------------
    # a0 = ((0.3*c*(sqrt(2.5)))/(f1*1e9*(sqrt(epsilon))))
    # epsilon_eff = 0.5 * (epsilon + 1) + 0.25 * (epsilon - 1)/(sqrt(1 + 12 * h * 1e-3 / a0))
    # a_eff = ((0.3*c*(sqrt(2.5)))/(f1*1e9*(sqrt(epsilon_eff)))) * 1e3
    # a = a_eff - h/sqrt(epsilon)
    # print "a_eff (in mm) = {0} , a0 (in mm) = {1} , a (in mm) = {2} , epsilon_eff = {3} ".format(a_eff, a0*1e3, a, epsilon_eff)
    # -----------------------------------------------------------
    # a = ((2 * c) / (3 * f1 * 1e9 * sqrt(epsilon))) * 1e3
    # -----------------------------------------------------------
    # a0 = ((2 * c) / (3 * f1 * 1e9 * sqrt(epsilon)))
    # epsilon_eff = 0.5 * (epsilon + 1) + 0.25 * (epsilon - 1)/(sqrt(1 + 12 * h * 1e-3 / a0))
    # a_eff = ((2 * c) / (3 * f1 * 1e9 * sqrt(epsilon_eff))) * 1e3
    # a = a_eff - h/sqrt(epsilon)
    #
    # -----------------------------------------------------------

    # alpha = (0.5 * (epsilon * t - 2.199 * epsilon * a_eff + 12.853 * sqrt(epsilon) * a_eff - 16.436 * a_eff) / epsilon)
    # beta = pow((-1000 * t * epsilon + 2199 * epsilon * a_eff - 12853 * sqrt(epsilon) * a_eff + 16436 * a_eff), 2)
    # gamma = 4000 * epsilon * (6182 * epsilon - 9802 * sqrt(epsilon)) * pow(a_eff, 2)
    # assert(beta > gamma), "Beta less than gamma"
    # theta = (1 / epsilon) * 0.0005 * sqrt(beta - gamma)
    # a1 = alpha + theta
    # a2 = alpha - theta
    # print "a_eff (in mm) = {0} , a0 (in mm) = {1} , a (in mm) = {2} , epsilon_eff = {3} ".format(a_eff, a0*1e3, a, epsilon_eff)

    # ---------------------------------------------------------
    a0 = (c / (3 * f1 * 1e9 * sqrt(epsilon)))
    epsilon_eff = 0.5 * (epsilon + 1) + 0.25 * (epsilon - 1)/(sqrt(1 + 12 * h * 1e-3 / a0))
    a_eff = (c / (3 * f1 * 1e9 * sqrt(epsilon_eff))) * 1e3
    a = a_eff - h/sqrt(epsilon_eff)
    # ---------------------------------------------------------
    print "a_eff (in mm) = {0} , a0 (in mm) = {1} , a (in mm) = {2} , epsilon_eff = {3} ".format(a_eff, a0*1e3, a, epsilon_eff)
    #print "a = ", a
    return a


def get_initial_coordinates(a):
    global x00, y00, x01, y01, x02, y02
    x00 = 0
    y00 = 0
    x01 = a/2
    y01 = (sqrt(3) * a)/2
    x02 = a
    y02 = 0


def make_directory_for_results_and_cleanup():
    global dirname
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    else:
        file_list = glob.glob(dirname + '\*')
        for filename in file_list:
            os.remove(filename)

############################ Main ###############################################

helper()

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

n = get_frequencies_and_scale_factor()
assert ((n[0] > 1) and (n[1] > 1)), "Scale factor should be greater than 1"

itr = int(input('Iterations : '))
assert(itr >= 0), "Iterations should be Positive"
print "\n"
substrate_thickness = float(input('Substrate thickness in mm: '))
assert(substrate_thickness > 0), "Substrate thickness should be Positive"
side = calculate_side(substrate_thickness)
height = sqrt(3) * side / 2

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
print "Info: The files containing coordinates can be found in the following directory - {0} \n".format(dirname)

make_directory_for_results_and_cleanup()
draw_helper(w, itr+1, x00, y00, x01, y01, x02, y02, n[0]-1, n[1]-1, side, height, True)

# w.create_polygon(points, outline=python_green,
#           fill='yellow', width=1)

mainloop()
