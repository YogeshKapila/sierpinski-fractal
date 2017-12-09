from __future__ import division
from Tkinter import *


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


def divide_in_ratio(a1, a2, x):
    return (a1 + x*a2)/(x+1)


def midpoint(a1, a2):
    return (a1 + a2)/2


def draw_helper(canvas, level, x1, y1, x2, y2, x3, y3, scale):
        # print "Scale %f" %(scale)
        if level == 1:
            print '({0}, {1})'.format(x1, y1) + '({0}, {1})'.format(x2, y2) + '({0}, {1})'.format(x3, y3)
            canvas.create_polygon(x1, y1, x2, y2, x3, y3, width=1)
        else:
            x4 = divide_in_ratio(x1, x2, scale)
            x5 = divide_in_ratio(x3, x2, scale)
            x6 = midpoint(x3, x1)
            y4 = divide_in_ratio(y1, y2, scale)
            y5 = divide_in_ratio(y3, y2, scale)
            y6 = midpoint(y3, y1)
            draw_helper(canvas, level - 1, x1, y1, x4, y4, x6, y6, scale)
            draw_helper(canvas, level - 1, x4, y4, x2, y2, x5, y5, scale)
            draw_helper(canvas, level - 1, x6, y6, x5, y5, x3, y3, scale)

############################ Main ###############################################

canvas_width = 500
canvas_height = 500
python_green = "#476042"

# Print Helper Diagram for inputting coordinates
print_helper_triangle()

# Get Input Coordinates, Iterations and Scale factor
x00 = int(input('Point 1 (Base) X-coord: '))
y00 = int(input('Point 1 (Base) Y-coord: '))
print "\n"
x01 = int(input('Point 2 (Top vertex) X-coord: '))
y01 = int(input('Point 2 (Top vertex) Y-coord: '))
print "\n"
x02 = int(input('Point 3 (Base) X-coord: '))
y02 = int(input('Point 3 (Base) Y-coord: '))
print "\n"

itr = int(input('Iterations : '))
assert(itr >= 1), "Iterations should be greater than equal to 1"
print "\n"
n = float(input('Scale : '))
assert(n > 1), "Scale factor should be greater than 1"

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
