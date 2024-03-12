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

def draw_ellipse(center_x, center_y, a, b, fill_color):
    glColor3f(*fill_color)  # Set the fill color
    glBegin(GL_POLYGON)
    for theta in range(0, 360, 1):
        x = center_x + a * cos(radians(theta)) * 6
        y = center_y + b * sin(radians(theta)) * 5
        sheared_x = shear_x(x, y)
        sheared_y = shear_y(x, y)
        glVertex2f(sheared_x, sheared_y)
    glEnd()

def boundary_fill(x, y, fill_color, boundary_color):
    current_color = (GLfloat * 4)()  # Create a 4-element array to store the current color
    glGetFloatv(GL_CURRENT_COLOR, current_color)  # Get the current color
    current_color_rgb = (current_color[0], current_color[1], current_color[2])

    if current_color_rgb != fill_color and current_color_rgb != boundary_color:
        glColor3f(*boundary_color)  # Set boundary color to cyan
        glBegin(GL_POINTS)
        glVertex2i(x, y)
        glEnd()
        boundary_fill(x + 1, y, fill_color, boundary_color)
        boundary_fill(x - 1, y, fill_color, boundary_color)
        boundary_fill(x, y + 1, fill_color, boundary_color)
        boundary_fill(x, y - 1, fill_color, boundary_color)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-20, 20, -20, 20)

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    fill_color = (0.0, 1.0, 0.0)  # Green color
    draw_ellipse(-2, 2, 1, 1, fill_color)

    # Boundary fill the ellipse with cyan color
    boundary_fill(-2, 2, fill_color, (0.0, 1.0, 1.0))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()
