import turtle
import numpy as np
t = turtle.Turtle(shape="turtle")

t.lt(90)

lv = 13
l = 90.0
s = 17

t.width(1)

t.penup()
t.bk(l)
t.pendown()
t.fd(l)

def sun_turt(scolor = ('red', 'yellow'), length = 100):
    t.color(scolor[0],scolor[1])
    t.begin_fill()
    while True:
        t.forward(200)
        t.left(np.random.randint(12,174))
        if abs(t.pos()) < 1:
            break
    t.end_fill()

def draw_tree(l, level):
    width = t.width()  # save the current pen width

    #t.width(width * 3.0 / 4.0)  # narrow the pen width
    l = 6./7. * l 

    t.lt(s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.rt(2 * s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.lt(s)
    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.rt(s*3)
    t.fd(l/2)

    t.width(width)  # restore the previous pen width

t.speed("normal")

draw_tree(l, 2)
#t.getscreen().getcanvas().postscript(file='testut.ps')

#sun_turt(['black','yellow'])

turtle.done()