'''
Created on 25-02-2011

@author: John
'''
# from pyopenal import *
import math, pyopenal, random

from PyQt4.QtCore import QTimer, SIGNAL, SLOT, Qt
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt4 import QtGui
from PyQt4.QtOpenGL import QGLWidget

from moving_target import MovingTarget
from the_shooter import TheShooter
from PyQt4.uic.Compiler.qtproxies import QtCore

class GeometryShooterWidget(QGLWidget):
    
    __pyqtSignals__ = ("killed(int)",
                     "died(int)")
    
    def __init__(self, parent, timerInterval):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(800, 600)
        
        self.initializeAL()
        
        self.rtri = 0
        self.rquad = 0
        self.hits = 0
        self.deaths = 0
        
        if timerInterval == 0: 
            self.m_timer = 0;
        else:
            self.m_timer = QTimer()
            self.connect( self.m_timer, SIGNAL("timeout()"), self.timeOut)
            self.m_timer.start(timerInterval)

        self.populateGameWorld()
        
    
    def populateGameWorld(self):
        print '*** Populating Game World'
        
        self.targets = []
        self.projectiles = []
        self.shooter = TheShooter()
        
    def initializeAL(self):
        pyopenal.init(None)
        self.listener = pyopenal.Listener(22050)
        self.listener.position = (0.0, 0.0, -10.0)
        self.listener.at = (0.0, 0.0, 1.0)
        self.listener.up = (0.0, 1.0, 0.0)
        
        pyopenal.alDopplerFactor(10.0)
        pyopenal.alDopplerVelocity(10.0)
        
        self.musicBuffer = pyopenal.WaveBuffer("res/oxygene.wav")
        self.musicSource = pyopenal.Source()
        self.musicSource.buffer = self.musicBuffer
        self.musicSource.position = (0.0, 0.0, 0.0)
        self.musicSource.looping = True
        self.musicSource.gain = .25
        
        self.musicSource.play()
    
    def playBackgroundMusic(self):
        if self.musicSource.get_state() != pyopenal.AL_PLAYING:
            self.musicSource.play()
        else:
            self.musicSource.stop()
        
    def initializeGL(self):
        # set viewing projection
        glShadeModel(GL_SMOOTH);

        glClearColor(0.0, 0.0, 0.0, 0.0);
        glClearDepth(1.0);

        glEnable(GL_DEPTH_TEST);
        glDepthFunc(GL_LEQUAL);

        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);    

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # draw the moving targets
        for target in self.targets:
            target.draw(self.rquad)
        # draw the projectiles
        for projectile in self.projectiles:
            projectile.draw()
        self.shooter.draw()
        
    def resizeGL(self, width, height):
        height = height or 1

        glViewport( 0, 0, width, height )
    
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        # gluPerspective(45.0f,(GLfloat)width/(GLfloat)height,0.1f,100.0f);
        fieldOfView = 45.0
        zNear = 0.1
        zFar = 255.0
        aspect = float(width)/float(height);
        
        fH = math.tan(fieldOfView / 360.0 * 3.14159) * zNear;
        fW = fH * aspect;
        glFrustum( -fW, fW, -fH, fH, zNear, zFar );
        # glOrtho(-10.0f, 10.0f, -10.0f, 10.0f, 0.1f, 255.0f);
    
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
    
    def drawSpiral(self):
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
        
    def timeOut(self):
        self.rtri += 0.5
        self.rquad -= 0.25
        
        start = 7500
        
        if self.rtri % 750 == 0 and self.rtri > start:
            if random.randint(0, 1) == 1:
                self.targets.append(MovingTarget(self.targets))
            for target in self.targets:
                if not target.isOnMap():
                    self.targets.remove(target)
                 
        self.countHits(start)
        self.countDeaths(start)
        
        self.updateGL()
        
    def countHits(self, start):
        if self.rtri % 100 == 0 and self.rtri > start:
            for target in filter(lambda (x) : x.isAlive(), self.targets):
                for projectile in self.projectiles:
                    if target.isHit(projectile.getPosition()):
                        target.die(True)
                        self.hits += 1
                    if not projectile.isOnMap():
                        self.projectiles.remove(projectile)
        
        self.emit(SIGNAL('killed(int)'), self.hits)
    
    def countDeaths(self, start):
        if self.rtri % 100 == 0 and self.rtri > start:
            for target in filter(lambda (x) : x.isAlive(), self.targets):
                if target.isHit(self.shooter.getPosition()):
                        target.die(False)
                        self.deaths += 1
                    
        self.emit(SIGNAL('died(int)'), self.deaths)
        
        
    # keys
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Left:
            self.shooter.rotate('left')
        if key == Qt.Key_Right:
            self.shooter.rotate('right')
        if key == Qt.Key_Space:
            self.projectiles.append(self.shooter.shoot())
        else:
            QtGui.QWidget.keyPressEvent(self, event)

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_Left:
            0
        if key == Qt.Key_Right:
            0
        else:
            QtGui.QWidget.keyPressEvent(self, event)
