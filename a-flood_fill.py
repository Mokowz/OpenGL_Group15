import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np

def draw_ellipse(center_x, center_y, a, b, fill_color):
    glColor3f(*fill_color)
    glBegin(GL_POLYGON)
    for theta in range(0, 360, 1):
        x = center_x + a * math.cos(math.radians(theta))
        y = center_y + b * math.sin(math.radians(theta))
        glVertex2f(x, y)
    glEnd()

def flood_fill(x, y, old_color, new_color):
    color = get_pixel_color(x, y)
    if np.all(color == old_color):
        set_pixel_color(x, y, new_color)
        flood_fill(x+1, y, old_color, new_color)
        flood_fill(x-1, y, old_color, new_color)
        flood_fill(x, y+1, old_color, new_color)
        flood_fill(x, y-1, old_color, new_color)

def get_pixel_color(x, y):
    buffer = glReadPixels(int(x), int(y), 1, 1, GL_RGB, GL_FLOAT)
    return buffer[0]

def set_pixel_color(x, y, color):
    glColor3f(*color)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-10, 10, -10, 10)

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