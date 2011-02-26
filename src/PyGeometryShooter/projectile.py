'''
Created on Feb 25, 2011

@author: john
'''
import math
from OpenGL.GL import *
from OpenGL.GLU import *

class Projectile:
    
    def __init__(self, rotation):
        
        print '*** shooting at angle ' + str(rotation) + ' ***'
        # pointing upwards
        self.speed = [.0, .01]
        self.rotation = math.radians(rotation)
        self.speed = [self.speed[0]*math.cos(self.rotation)-self.speed[1]*math.sin(self.rotation),
                      self.speed[0]*math.sin(self.rotation)+self.speed[1]*math.cos(self.rotation)]
        self.shape = [self.speed[0]*100, self.speed[1]*100]
        self.initGraphics()
        
    def __del__(self):
        print '*** fire some mo\'! ***'
        
    def getPosition(self):
        return self.position
    
    def isOnMap(self):
        result = True
        for coordinate in self.position:
            if -10 > coordinate or coordinate > 10:
                result = False
        
        return result
    
    def initGraphics(self):
        self.scale = .2
        self.rotation = 0.0
        self.position = [0.0, 0.0, -10.0]
    
    def draw(self):
        # self.position[0] += self.speed
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        # self.position[2] += self.speed
        
        glLoadIdentity();
        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], self.position[2]);
        #glLoadIdentity();
        glRotatef(self.rotation, 0.0, 0.0, 1.0);
        glScale(self.scale, self.scale, self.scale)
        glBegin(GL_LINES);
        glColor(1.0,0.0,0.0);
        glVertex(0.0, 0.0)
        glColor(1.0,0.0,0.0);
        glVertex(self.shape[0], self.shape[1])
        glEnd()
        glPopMatrix()