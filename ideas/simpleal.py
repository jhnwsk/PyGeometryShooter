import pyopenal, time

pyopenal.init(None)
l = pyopenal.Listener(22050)
l.position = (0.0, 0.0, 0.0)
l.at = (0.0, 0.0, 1.0)
l.up = (0.0, 1.0, 0.0)

b = pyopenal.WaveBuffer("cutoff.wav")
b2 = pyopenal.WaveBuffer("cutoff.wav")

s = pyopenal.Source()
s2 = pyopenal.Source()

x_position = 0.0
s.position = (x_position, 0.0, 0.0)
s2.position = (0.0, 1.0, 0.0)


s.buffer = b
s.looping = True
s2.looping = False
s.pitch = 2.0
s.gain = 0.3
s.play()
s2.play()
side = 1 # is for right

s2.buffer = b2

while s.get_state() == pyopenal.AL_PLAYING:
    if x_position > 0.9:
        side = 2
    elif x_position < -0.9:
        s2.pitch = 0.5
        s2.play()
        side = 1
        
    if side == 1:
        x_position += 0.1
        s.position = (x_position, 0.0, 0.0)
    else:
        x_position -= 0.1
        s.position = (x_position, 0.0, 0.0)
    
    time.sleep(0.1)

pyopenal.quit()