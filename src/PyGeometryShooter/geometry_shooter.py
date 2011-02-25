'''
Created on 25-02-2011

@author: John
'''
from PyQt4 import QtGui

from geometry_shooter_widget import GeometryShooterWidget

# You don't need anything below this
class GeometryShooter(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        widget = GeometryShooterWidget(self, 1)    
        self.setCentralWidget(widget)
        
if __name__ == '__main__':
    app = QtGui.QApplication(['Spiral Widget Demo'])
    window = GeometryShooter()
    window.show()
    app.exec_()