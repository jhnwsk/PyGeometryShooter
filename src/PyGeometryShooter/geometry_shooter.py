'''
Created on 25-02-2011

@author: John
'''
from PyQt4 import QtGui, QtCore

from geometry_shooter_widget import GeometryShooterWidget

# You don't need anything below this
class GeometryShooter(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.widget = GeometryShooterWidget(self, 1)    
        self.setCentralWidget(self.widget)
        
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_M:
            self.widget.playBackgroundMusic()
        if key == QtCore.Qt.Key_Q:
            self.close()
        else:
            self.widget.keyPressEvent(event)
            
    def keyReleaseEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Q:
            self.close()
        else:
            self.widget.keyReleaseEvent(event)

        
if __name__ == '__main__':
    app = QtGui.QApplication(['Geometry Shooter'])
    window = GeometryShooter()
    window.show()
    app.exec_()