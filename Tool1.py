import turtle


def draw_sierpinski(length, depth=2, n=2.0):
    if depth == 0:
        for i in range(0, 3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length/n, depth-1, n)
        t.fd(length/n)
        draw_sierpinski(length/n, depth-1, n)
        t.bk(length/n)
        t.left(60)
        t.fd(length/n)
        t.right(60)
        draw_sierpinski(length/n, depth-1, n)
        t.left(60)
        t.bk(length/n)
        t.right(60)

# Triangles will be of different sides
l = int(input('Side of base triangle: '))
d = int(input('Iterations: '))
scale = float(input('Scale factor: '))

window = turtle.Screen()
t = turtle.Turtle()
draw_sierpinski(l, d, scale)
window.exitonclick()
