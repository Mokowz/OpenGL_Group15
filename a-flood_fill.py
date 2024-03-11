# Ronny

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, radians

def draw_ellipse(center_x, center_y, a, b):
    glBegin(GL_POLYGON)
    for theta in range(0, 360, 1):
        x = center_x + a * cos(theta) * 6
        y = center_y + b * sin(theta) * 5
        glVertex2f(x, y)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-10, 10, -10, 10)

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
