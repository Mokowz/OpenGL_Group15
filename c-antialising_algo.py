# Yunus 
def antialias_ellipse(center_x, center_y, a, b):
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glBegin(GL_POINTS)
    for theta in range(0, 360, 1):
        x = center_x + a * cos(radians(theta)) * 6
        y = center_y + b * sin(radians(theta)) * 5
        sheared_x = shear_x(x, y)
        sheared_y = shear_y(x, y)

        # Calculate alpha (transparency) based on distance to ellipse boundary
        alpha = 1.0 - min(abs(x - sheared_x) / a, abs(y - sheared_y) / b)

        glColor4f(1.0, 1.0, 1.0, alpha)
        glVertex2f(sheared_x, sheared_y)

    glEnd()
    glDisable(GL_BLEND)
