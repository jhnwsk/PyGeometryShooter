'''
Created on Feb 25, 2011

@author: john
'''

class Projectile:
    
    def __init__(self):
        self.initGraphics()
        
    def initGraphics(self):
        self.speed = 2.0
        self.scale = .2
        self.rotation = 0.0
        self.position = [0.0, 0.0, -10.0]