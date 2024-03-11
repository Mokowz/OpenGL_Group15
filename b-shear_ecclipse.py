# Yunus

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, radians

def shear_x(x, y):
    return x + 2 * y

def shear_y(x, y):
    return 2 * x + y

def draw_ellipse(center_x, center_y, a, b):
    glBegin(GL_POLYGON)
    for theta in range(0, 360, 1):
        x = center_x + a * cos(radians(theta)) * 6
        y = center_y + b * sin(radians(theta)) * 5
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

    glColor3f(1.0, 1.0, 1.0)
    draw_ellipse(-2, 2, 1, 1)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()
