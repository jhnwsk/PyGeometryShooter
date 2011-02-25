'''
Created on 25-02-2011

@author: John
'''
import math

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt4 import QtGui
from PyQt4.QtOpenGL import *

from PyGeometryShooter import GeometryShooterWidget

# You don't need anything below this
class GeometryShooter(QtGui.QMainWindow):
    ''' Example class for using SpiralWidget'''
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        widget = GeometryShooterWidget(self)    
        self.setCentralWidget(widget)
        
if __name__ == '__main__':
    app = QtGui.QApplication(['Spiral Widget Demo'])
    window = GeometryShooterWidget()
    window.show()
    app.exec_()