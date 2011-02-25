'''
Created on 25-02-2011

@author: John
'''
from OpenGL.GL import *
from OpenGL.GLU import *

class MovingTarget:
    
    def __init__(self):
        self.initSound()
        self.initGraphics()
    
    def initSound(self):
        self.sound = 0
    
    def initGraphics(self):
        self.rotationSpeed = 2.0
        self.position = [0.0, 0.0, -10.0]
        
    def draw(self, time):
        self.rotationSpeed += time
        glLoadIdentity();
        glTranslate(self.position[0],self.position[1],self.position[2]);
        glRotate(self.rotationSpeed,1.0,0.0,0.0);
        glRotate(self.rotationSpeed / 2,0,1,0);
    
        glColor(0.5,0.5,1.0);
        glBegin(GL_QUADS);
        glColor(0.0,1.0,0.0);
        glVertex( 1.0, 1.0,-1.0);
        glVertex(-1.0, 1.0,-1.0);
        glVertex(-1.0, 1.0, 1.0);
        glVertex( 1.0, 1.0, 1.0);
        glColor(1.0,0.5,0.0);
        glVertex( 1.0,-1.0, 1.0);
        glVertex(-1.0,-1.0, 1.0);
        glVertex(-1.0,-1.0,-1.0);
        glVertex( 1.0,-1.0,-1.0);
        glColor(1.0,0.0,0.0);
        glVertex( 1.0, 1.0, 1.0);
        glVertex(-1.0, 1.0, 1.0);
        glVertex(-1.0,-1.0, 1.0);
        glVertex( 1.0,-1.0, 1.0);
        glColor(1.0,1.0,0.0);
        glVertex( 1.0,-1.0,-1.0);
        glVertex(-1.0,-1.0,-1.0);
        glVertex(-1.0, 1.0,-1.0);
        glVertex( 1.0, 1.0,-1.0);
        glColor(0.0,0.0,1.0);
        glVertex(-1.0, 1.0, 1.0);
        glVertex(-1.0, 1.0,-1.0);
        glVertex(-1.0,-1.0,-1.0);
        glVertex(-1.0,-1.0, 1.0);
        glColor(1.0,0.0,1.0);
        glVertex( 1.0, 1.0,-1.0);
        glVertex( 1.0, 1.0, 1.0);
        glVertex( 1.0,-1.0, 1.0);
        glVertex( 1.0,-1.0,-1.0);
        glEnd();