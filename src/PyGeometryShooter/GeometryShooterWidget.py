'''
Created on 25-02-2011

@author: John
'''
import math

# import OpenGL.GL
from OpenGL.GL import *
# import OpenGL
from OpenGL.GLU import *
from PyQt4.QtOpenGL import QGLWidget

class GeometryShooterWidget(QGLWidget):
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(500, 500)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Draw the spiral in 'immediate mode'
        # WARNING: You should not be doing the spiral calculation inside the loop
        # even if you are using glBegin/glEnd, sin/cos are fairly expensive functions
        # I've left it here as is to make the code simpler.
        radius = 1.0
        x = radius * math.sin(0)
        y = radius * math.cos(0)
        glColor(0.0, 1.0, 0.0)
        glBegin(GL_LINE_STRIP)
        for deg in xrange(1000):
            glVertex(x, y, 0.0)
            rad = math.radians(deg)
            radius -= 0.001
            x = radius * math.sin(rad)
            y = radius * math.cos(rad)
        glEnd()
        
        glEnableClientState(GL_VERTEX_ARRAY)
        
        spiral_array = []
        
        # Second Spiral using "array immediate mode" (i.e. Vertex Arrays)
        radius = 0.8
        x = radius * math.sin(0)
        y = radius * math.cos(0)
        glColor(1.0, 0.0, 0.0)
        for deg in xrange(820):
            spiral_array.append([x, y])
            rad = math.radians(deg)
            radius -= 0.001
            x = radius * math.sin(rad)
            y = radius * math.cos(rad)

        glVertexPointerf(spiral_array)
        glDrawArrays(GL_LINE_STRIP, 0, len(spiral_array))
        glFlush()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40.0, 1.0, 1.0, 30.0)
    
    def initializeGL(self):
        # set viewing projection
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40.0, 1.0, 1.0, 30.0)
