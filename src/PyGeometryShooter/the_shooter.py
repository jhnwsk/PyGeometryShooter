'''
Created on Feb 25, 2011

@author: john
'''
import pyopenal
from OpenGL.GL import *
from OpenGL.GLU import *

from projectile import Projectile

class TheShooter:
    
    def __init__(self):
        self.initGraphics()
        self.initSound()
        
    def initGraphics(self):
        self.rotationSpeed = 5
        self.rotation = 0.0
        self.position = [0.0, 0.0, -10.0]
        self.scale = .25
    
    def initSound(self):
        #pyopenal.init(None)
        self.musicBuffer = pyopenal.WaveBuffer("res/cutoff.wav")
        self.shootBuffer = pyopenal.WaveBuffer("res/shoot.wav")
        
        self.flySource = pyopenal.Source()
        self.flySource.buffer = self.musicBuffer
        self.flySource.position = (0.0, 0.0, 0.0)
        self.flySource.looping = True
        
        self.shootSource = pyopenal.Source()
        self.shootSource.buffer = self.shootBuffer
        self.shootSource.position = (0.0, 0.0, 0.0)
        self.shootSource.looping = False
    
    def rotate(self, side):
        if side == 'left':
            self.rotation += self.rotationSpeed
        elif side == 'right':
            self.rotation -= self.rotationSpeed
            
    def draw(self):
        glLoadIdentity();
        glTranslatef(self.position[0], self.position[1], self.position[2]);
        glRotatef(self.rotation, 0, 0, 1);
    
        glScale(self.scale, self.scale, self.scale)
        glBegin(GL_TRIANGLES);
        glColor(0, 1.0, 1.0);
        glVertex( 0.0, 1.0, 0.0);
        glColor(0.0,0.0,1.0);
        glVertex(-1.0,-1.0, 1.0);
        glColor(0.0,0.0,1.0);
        glVertex( 1.0,-1.0, 1.0);
        glColor(1.0,0.0,0.0);
        glVertex( 0.0, 1.0, 0.0);
        glColor(0.0,0.0,1.0);
        glVertex( 1.0,-1.0, 1.0);
        glColor(0.0,1.0,0.0);
        glVertex( 1.0,-1.0, -1.0);
        glColor(1.0,0.0,0.0);
        glVertex( 0.0, 1.0, 0.0);
        glColor(0.0,1.0,0.0);
        glVertex( 1.0,-1.0, -1.0);
        glColor(0.0,0.0,1.0);
        glVertex(-1.0,-1.0, -1.0);
        glColor(1.0,0.0,0.0);
        glVertex( 0.0, 1.0, 0.0);
        glColor(0.0,0.0,1.0);
        glVertex(-1.0,-1.0,-1.0);
        glColor(0.0,1.0,0.0);
        glVertex(-1.0,-1.0, 1.0);
        glEnd();
        
    def shoot(self):
        self.shootSource.play()
        return Projectile(self.rotation)
    
    def getPosition(self):
        return self.position