'''
Created on 25-02-2011

@author: John
'''
from PyQt4 import QtGui, QtCore

from geometry_shooter_widget import GeometryShooterWidget

# You don't need anything below this
class GeometryShooter(QtGui.QMainWindow):
    
    lcdKill = QtGui.QLCDNumber
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        grid = QtGui.QGridLayout()
        
        self.widget = GeometryShooterWidget(self, 1)
        self.setCentralWidget(self.widget)
        
        self.lcdKill = QtGui.QLCDNumber(self)
        
        self.lcdBeKilled = QtGui.QLCDNumber(self)
        self.lcdBeKilled.move(0, 30)
        
        self.connect(self.widget, QtCore.SIGNAL('killed(int)'), self.lcdKill, QtCore.SLOT('display(int)') )
        self.connect(self.widget, QtCore.SIGNAL('died(int)'), self.lcdBeKilled, QtCore.SLOT('display(int)') )
        
        
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Nie chcesz juz szczelac?", QtGui.QMessageBox.Yes | 
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
        if key == QtCore.Qt.Key_A:
            print "you pressed a"
        else:
            self.widget.keyPressEvent(event)
            
    def keyReleaseEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Q:
            self.close()
        if key == QtCore.Qt.Key_A:
            print "you released a"
        else:
            self.widget.keyReleaseEvent(event)

        
if __name__ == '__main__':
    app = QtGui.QApplication(['Geometry Shooter'])
    window = GeometryShooter()
    window.show()
    app.exec_()