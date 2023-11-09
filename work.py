import time
import ntptime
import urequests
import random
import os
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN
from pngdec import PNG
from machine import Pin
import myDayTest
import network

graphics = PicoGraphics(display=DISPLAY_COSMIC_UNICORN)
gu = CosmicUnicorn()
gu.set_brightness(1.0)

# Enable the Wireless
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

connected = False
while not connected:
   connected = myDayTest.network_connect(wlan)
print("here")

png = PNG(graphics)
png.open_file("/sheet.png")

frame_width = 32
frame_height = 32

black = graphics.create_pen(0,0,0)

class frame:
    def __init__(self, frame_x, frame_y):
        self.frame_x = frame_x
        self.frame_y = frame_y

work = []
# describe as index from 0 - 5
work.append(frame (0, 5))
work.append(frame (0, 5))
work.append(frame (0, 5))
work.append(frame (1, 5))
work.append(frame (2, 5))
work.append(frame (2, 5))
work.append(frame (1, 5))
work.append(frame (1, 5))
work.append(frame (2, 5))
work.append(frame (1, 5))
work.append(frame (2, 5))
work.append(frame (3, 5))
work.append(frame (4, 5))
work.append(frame (5, 5))
work.append(frame (3, 5))
work.append(frame (4, 5))
work.append(frame (5, 5))
work.append(frame (3, 5))
work.append(frame (4, 5))
work.append(frame (5, 5))
work.append(frame (3, 5))
work.append(frame (4, 5))
work.append(frame (5, 5))
work.append(frame (3, 5))
work.append(frame (4, 5))
work.append(frame (5, 5))
work.append(frame (3, 5))
work.append(frame (4, 5))
work.append(frame (5, 5))
work.append(frame (3, 5))
work.append(frame (4, 5))
work.append(frame (5, 5))
work.append(frame (3, 5))
work.append(frame (4, 5))
work.append(frame (5, 5))
work.append(frame (3, 5))
work.append(frame (4, 5))
work.append(frame (5, 5))

chillin = []
# describe as index from 0 - 5
chillin.append(frame (0, 0))
chillin.append(frame (1, 0))
chillin.append(frame (0, 0))
chillin.append(frame (1, 0))
chillin.append(frame (0, 0))
chillin.append(frame (1, 0))
chillin.append(frame (0, 0))
chillin.append(frame (1, 0))
chillin.append(frame (0, 0))
chillin.append(frame (1, 0))
chillin.append(frame (0, 0))
chillin.append(frame (1, 0))
chillin.append(frame (0, 0))
chillin.append(frame (1, 0))
chillin.append(frame (0, 0))
chillin.append(frame (1, 0))
chillin.append(frame (0, 0))
chillin.append(frame (1, 0))
chillin.append(frame (0, 0))
chillin.append(frame (1, 0))

runnin = []
# describe as index from 0 - 5
runnin.append(frame (1,1))
runnin.append(frame (2, 1))
runnin.append(frame (3, 1))
runnin.append(frame (4, 1))
runnin.append(frame (1,1))
runnin.append(frame (2, 1))
runnin.append(frame (3, 1))
runnin.append(frame (4, 1))
runnin.append(frame (1,1))
runnin.append(frame (2, 1))
runnin.append(frame (3, 1))
runnin.append(frame (4, 1))
runnin.append(frame (1,1))
runnin.append(frame (2, 1))
runnin.append(frame (3, 1))
runnin.append(frame (4, 1))

den = []
# describe as index from 0 - 5
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (5, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (5, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (5, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (5, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (5, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (4, 3))
den.append(frame (5, 3))

ded = []
# describe as index from 0 - 5
ded.append(frame (0, 4))
ded.append(frame (0, 4))
ded.append(frame (0, 4))
ded.append(frame (1, 4))
ded.append(frame (1, 4))
ded.append(frame (1, 4))
ded.append(frame (1, 4))
ded.append(frame (2, 4))
ded.append(frame (2, 4))
ded.append(frame (2, 4))
ded.append(frame (2, 4))
ded.append(frame (3, 4))
ded.append(frame (3, 4))
ded.append(frame (3, 4))
ded.append(frame (3, 4))
ded.append(frame (3, 4))
ded.append(frame (4, 4))
ded.append(frame (4, 4))
ded.append(frame (4, 4))
ded.append(frame (4, 4))
ded.append(frame (4, 4))
ded.append(frame (4, 4))
ded.append(frame (4, 4))
ded.append(frame (4, 4))
ded.append(frame (5, 4))
ded.append(frame (5, 4))
ded.append(frame (5, 4))
ded.append(frame (5, 4))
ded.append(frame (5, 4))
ded.append(frame (5, 4))
ded.append(frame (5, 4))
ded.append(frame (5, 4))
ded.append(frame (5, 4))

dino = []
# describe as index from 0 - 5
dino.append(frame (0, 2))
dino.append(frame (1, 2))
dino.append(frame (2, 2))
dino.append(frame (1, 2))
dino.append(frame (0, 2))
dino.append(frame (0, 2))
dino.append(frame (1, 2))
dino.append(frame (2, 2))
dino.append(frame (1, 2))
dino.append(frame (0, 2))
dino.append(frame (0, 2))
dino.append(frame (1, 2))
dino.append(frame (2, 2))
dino.append(frame (1, 2))
dino.append(frame (0, 2))
dino.append(frame (0, 2))
dino.append(frame (1, 2))
dino.append(frame (2, 2))
dino.append(frame (1, 2))
dino.append(frame (0, 2))

meeting = []
# describe as index from 0 - 5
meeting.append(frame (0, 3))
meeting.append(frame (1, 3))
meeting.append(frame (0, 3))
meeting.append(frame (1, 3))
meeting.append(frame (0, 3))
meeting.append(frame (1, 3))
meeting.append(frame (0, 3))
meeting.append(frame (1, 3))
meeting.append(frame (0, 3))
meeting.append(frame (1, 3))
meeting.append(frame (2, 3))
meeting.append(frame (3, 3))
meeting.append(frame (2, 3))
meeting.append(frame (3, 3))
meeting.append(frame (2, 3))
meeting.append(frame (3, 3))
meeting.append(frame (2, 3))
meeting.append(frame (3, 3))
meeting.append(frame (2, 3))
meeting.append(frame (3, 3))
meeting.append(frame (0, 3))
meeting.append(frame (1, 3))
meeting.append(frame (0, 3))
meeting.append(frame (1, 3))
meeting.append(frame (0, 3))
meeting.append(frame (1, 3))
meeting.append(frame (0, 3))
meeting.append(frame (1, 3))
meeting.append(frame (0, 3))
meeting.append(frame (1, 3))
meeting.append(frame (2, 3))
meeting.append(frame (3, 3))
meeting.append(frame (2, 3))
meeting.append(frame (3, 3))
meeting.append(frame (2, 3))
meeting.append(frame (3, 3))
meeting.append(frame (2, 3))
meeting.append(frame (3, 3))
meeting.append(frame (2, 3))
meeting.append(frame (3, 3))

fire = []
# describe as index from 0 - 5
fire.append(frame (2, 0))
fire.append(frame (3, 0))
fire.append(frame (4, 0))
fire.append(frame (5, 0))
fire.append(frame (4, 0))
fire.append(frame (3, 0))
fire.append(frame (2, 0))
fire.append(frame (3, 0))
fire.append(frame (4, 0))
fire.append(frame (5, 0))
fire.append(frame (4, 0))
fire.append(frame (3, 0))
fire.append(frame (2, 0))
fire.append(frame (3, 0))
fire.append(frame (4, 0))
fire.append(frame (5, 0))
fire.append(frame (4, 0))
fire.append(frame (3, 0))
fire.append(frame (2, 0))
fire.append(frame (3, 0))
fire.append(frame (4, 0))
fire.append(frame (5, 0))
fire.append(frame (4, 0))
fire.append(frame (3, 0))
fire.append(frame (2, 0))

me = []
# describe as index from 0 - 5
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))
me.append(frame (5, 2))

note = []
# describe as index from 0 - 5
note.append(frame (3, 2))
note.append(frame (3, 2))
note.append(frame (3, 2))
note.append(frame (3, 2))
note.append(frame (3, 2))
note.append(frame (3, 2))
note.append(frame (3, 2))
note.append(frame (3, 2))
note.append(frame (3, 2))
note.append(frame (4, 2))
note.append(frame (4, 2))
note.append(frame (4, 2))
note.append(frame (4, 2))
note.append(frame (4, 2))
note.append(frame (4, 2))
note.append(frame (4, 2))
note.append(frame (4, 2))
note.append(frame (4, 2))
note.append(frame (4, 2))

weekly = []
# describe as index from 0 - 5
weekly.append(frame (4, 0))
weekly.append(frame (5, 0))
weekly.append(frame (4, 0))
weekly.append(frame (5, 0))
weekly.append(frame (4, 0))
weekly.append(frame (5, 0))
weekly.append(frame (4, 0))
weekly.append(frame (5, 0))
weekly.append(frame (4, 0))
weekly.append(frame (5, 0))
weekly.append(frame (4, 0))
weekly.append(frame (5, 0))
weekly.append(frame (4, 0))
weekly.append(frame (5, 0))
weekly.append(frame (4, 0))
weekly.append(frame (5, 0))
weekly.append(frame (4, 0))
weekly.append(frame (5, 0))
weekly.append(frame (4, 0))
weekly.append(frame (5, 0))

workDuties =[work,chillin,runnin,note,weekly]

calText = "work"
print(f"Selected frame: {calText}")

busy = False

def DoorStuff():
    global busy

    #auto set brightness from light sensor
    #print(gu.light()/300)
    gu.set_brightness(max(.25,min(1.,gu.light()/300)))
    gu.set_volume(0.001) 
    #play random sound
    #wp.play(random.choice(audioFile), loop=1)
    
    busy = True
    calData = myDayTest.fuck()
    calText = calData["Title"]
    calStatus = calData["Status"]
    calColor = calData["Color"]
    
    workin = random.choice(workDuties)
    
    print(f"calendar data: {calText} {calStatus} {calColor}")
    
    # Use the correct list of frames based on calText
    if "work" in calText :
        spriteList = workin
        
    elif "chillin" in calText :
        spriteList = chillin
    elif "runnin" in calText :
        spriteList = runnin
    elif "ood" in calText :
        spriteList = ded
    elif "lynx" in calText :
        spriteList = den
    elif "lunch" in calText :
        spriteList = dino
    elif "meeting" in calText :
        spriteList = meeting
    elif "fire" in calText :
        spriteList = fire
    elif "me" in calText :
        spriteList = me
    elif "broken" in calText :
        spriteList = note
    elif "sleep" in calText :
        # Clear display set spriteList to 0
        spriteList = []
        graphics.set_pen(black)
        graphics.clear()
        gu.update(graphics)
    else:
        spriteList = meeting
        
    
    for frame in spriteList:
        if len(spriteList) != 0:
            #gu.set_brightness(1.0)
            #fuckin comments need to be tabbed
            # Clear the display before drawing the new frame
            graphics.set_pen(black)
            graphics.clear()

            # Decode and display the current frame
            png.decode(0, 0, source=(frame.frame_x * frame_width, frame.frame_y * frame_height, frame_width, frame_height), scale=(1, 1), rotate=90)
            #gu.adjust_brightness(-0.25)  # brightness ad
                    
            gu.update(graphics)        
            time.sleep(0.1)  # Adjust speed of anim

    # Clear display
    graphics.set_pen(black)
    graphics.clear()
    gu.update(graphics)
    
    time.sleep(15) # Time out so it does not trigger again immediately
    
    busy = False


while True:
        if not busy:
            DoorStuff()
