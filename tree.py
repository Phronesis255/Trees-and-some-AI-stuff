import pygame, math
import numpy as np


pygame.init()
window = pygame.display.set_mode((2680, 2080))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
keyp = ""
fname = ""
r = g = b = 0
x1 = x2 = y1 = y2 = 0.0
ndep = np.full(15, fill_value = 0.0)

def drawTree(x1, y1, angle, depth):
    if depth:
        x2 = x1 + float(math.cos(math.radians(angle)) * math.sin(depth) * depth * 15.0)
        y2 = y1 + float(math.sin(math.radians(angle)) * depth * 15.0)
        pygame.draw.line(screen, (r,g,b), (x1, y1), (x2, y2), 1)
        drawTree(x2, y2, math.cos((depth)^3) * (angle - angle2), depth - 1)
        drawTree(x2, y2,  np.log(10*depth)* (angle + angle2), depth - 1)
        # * math.sin(depth)
        #math.cos(angle + angle2)
def drawTree2(x1, y1, angle, depth):
    if depth:
        x2 = x1 + float(math.cos(math.radians(angle)) * math.sin(depth) * depth * 15.0)
        ndep[depth] = x1
        y2 = y1 + float(math.sin(math.radians(angle)) * depth * 15.0)
        #pygame.draw.line(screen, (r,g,b), (x1, y1), (x2, y2), 1)
        drawTree2(x2, y2, math.cos((depth)^3) * (angle - angle2), depth - 1)
        drawTree2(x2, y2,  np.log(10*depth)* (angle + angle2), depth - 1)
        print(ndep, "\n", ndep.shape)
        # * math.sin(depth)
        #math.cos(angle + angle2)


def input1(event):
    if event.type == pygame.QUIT:
        exit(0)
angle2=35
window.fill([255,255,255])
drawTree2(1340, 1500, -90, 14)
pygame.display.flip()
while True:
    keyp = input("what do you want to do? ")
    if keyp == "save":
        fname = input("Enter file name... ")
        fname = fname + ".jpg"
        pygame.image.save(window, fname)
        exit(0)
    elif keyp == "exit":
        exit(0)    
    input1(pygame.event.wait())