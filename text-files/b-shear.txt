import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np

def shear_x(x, y):
    return x + 2 * y

def shear_y(x, y):
    return 2 * x + y

def draw_ellipse(center_x, center_y, a, b, fill_color):
    glColor3f(*fill_color)
    glBegin(GL_POLYGON)
    for theta in range(0, 360, 1):
        x = center_x + a * math.cos(math.radians(theta))
        y = center_y + b * math.sin(math.radians(theta))
        sheared_x = shear_x(x, y)
        sheared_y = shear_y(x, y)
        glVertex2f(sheared_x, sheared_y)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-20, 20, -20, 20)

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    fill_color = np.array([0.0, 1.0, 1.0])  # Cyan color
    draw_ellipse(-2, 2, 6, 5, fill_color)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()
