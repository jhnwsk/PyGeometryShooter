'''
Created on 25-02-2011

@author: John
'''
import random, pyopenal, math, time
from OpenGL.GL import *
from OpenGL.GLU import *
from wx._misc import Sleep

class MovingTarget:
    
    def __init__(self, list):
        print "*** target aquired ***"
        mapRadius = 5.0
        self.scalarspeed = random.uniform(.0005, .005)
        # side
        side = random.randint(1, 4)
        self.alive = True
        self.list = list
        
        # position
        position = random.uniform(-5, 5)
        
        if side == 1: #north
            self.position = [position, mapRadius, -10.0]
            self.speed = [0.0, -self.scalarspeed, 0.0]
        elif side == 2: #south
            self.position = [position, -mapRadius, -10.0]
            self.speed = [0.0, self.scalarspeed, 0.0]
        elif side == 3: #east
            self.position = [-mapRadius, position, -10.0]
            self.speed = [self.scalarspeed, 0.0, 0.0]
        elif side == 4: #west
            self.position = [mapRadius, position, -10.0]
            self.speed = [-self.scalarspeed, 0.0, 0.0]
        
        print '*** targets position: ' + str(self.position) + ' speed: ' + str(self.speed) + ' ***'
        
        # sound and graphics
        self.initSound([-self.position[0], self.position[1], 0.0])
        self.initGraphics()
    
    def __del__(self):
        print "*** nice knowin' ya!"
        
    def isAlive(self):
        return self.alive
    
    def die(self, die):
        self.flySource.stop()
        if die:
            self.dieSource.position = [-self.position[0], self.position[1], 0.0]
            self.dieSource.play()
        else:
            self.killSource.position = [-self.position[0], self.position[1], 0.0]
            self.killSource.play()
            
        self.alive = False
        
    def initSound(self, position):
        
        pitch = random.randint(1, 10)
        pitch = 2.4 + pitch / 10.0
        
        # doppler
        self.shift = pyopenal.AL_DOPPLER_FACTOR * pitch * (pyopenal.AL_DOPPLER_VELOCITY - 0.0) / (pyopenal.AL_DOPPLER_VELOCITY + self.scalarspeed)
        
        # pyopenal.init(None)
        self.musicBuffer = pyopenal.WaveBuffer("res/cutoff.wav")
        self.flySource = pyopenal.Source()
        self.flySource.buffer = self.musicBuffer
        self.flySource.position = position
        self.flySource.pitch = pitch
        self.flySource.gain = 1.0
        self.flySource.velocity = [-self.speed[0] * 20000, self.speed[1] * 20000, self.speed[2]]
        self.flySource.looping = True
        
        self.dieBuffer = pyopenal.WaveBuffer("res/kill.wav")
        self.dieSource = pyopenal.Source()
        self.dieSource.buffer = self.dieBuffer
        self.dieSource.position = position
        self.dieSource.gain = 5.0
        self.dieSource.looping = False
        
        self.killBuffer = pyopenal.WaveBuffer("res/die.wav")
        self.killSource = pyopenal.Source()
        self.killSource.buffer = self.killBuffer
        self.killSource.position = position
        self.killSource.gain = 5.0
        self.killSource.looping = False
        
        self.flySource.play()
    
    def initGraphics(self):
        print "*** moving target initializing graphics ***"
        self.rotationSpeed = 0.1
        self.rotation = 2.0
        self.scale = .2
        
    def draw(self, time):
        self.rotation += self.rotationSpeed
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        self.position[2] += self.speed[2]
        
        self.flySource.position = [-self.position[0], self.position[1], 0.0]
        
        glLoadIdentity();
        glTranslate(self.position[0],self.position[1],self.position[2]);
        glRotate(self.rotation, 1, 0, 0);
        glRotate(self.rotation, 0, 1, 0);
    
        glScale(self.scale, self.scale, self.scale)
        glColor(0.5,0.5,1.0);
        if(self.alive):
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
        else:
            if self.dieSource.get_state() != pyopenal.AL_PLAYING and self.killSource.get_state() != pyopenal.AL_PLAYING:
                self.list.remove(self)
        
    def isOnMap(self):
        result = True
        for coordinate in self.position:
            if -10 > coordinate or coordinate > 10:
                result = False
        
        return result
        
    def isHit(self, rayCoords):
        print '*** testing ray coords ' + str(rayCoords) + ' against target ' + str(self.position) + ' ***'
        result = False
        distanceVector = [self.position[0] - rayCoords[0], 
                          self.position[1] - rayCoords[1], 
                          self.position[2] - rayCoords[2]]
        distance = math.sqrt(distanceVector[0]**2 + distanceVector[1]**2)
        
        if distance < .8:
            result = True
            
            
        return result
        