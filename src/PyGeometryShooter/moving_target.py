'''
Created on 25-02-2011

@author: John
'''
import random
from OpenGL.GL import *
from OpenGL.GLU import *

class MovingTarget:
    
    def __init__(self):
        self.initSound()
        self.initGraphics()
    
    def initSound(self):
        self.sound = 0
        #pyopenal.Listener()
    
    def initGraphics(self):
        print "*** moving target initializing graphics ***"
        self.rotationSpeed = 0.1
        self.rotation = 2.0
        self.scale = .2
        
        random_x = random.randint(-4, 4)
        random_y = random.randint(-4, 4)
        
        print '*** moving target position ' + str(random_x) + ' ' + str(random_y) + ' ***'
        self.position = [random_x, random_y, -10.0]
        # self.position = [0, 0, -10.0]
        
    def draw(self, time):
        self.rotation += self.rotationSpeed
        glLoadIdentity();
        glTranslate(self.position[0],self.position[1],self.position[2]);
        glRotate(self.rotation, 1, 0, 0);
        glRotate(self.rotation, 0, 1, 0);
    
        glScale(self.scale, self.scale, self.scale)
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