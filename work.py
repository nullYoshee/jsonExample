import time
import ntptime
import urequests
import random
import os
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN
from pngdec import PNG
from machine import Pin

graphics = PicoGraphics(display=DISPLAY_COSMIC_UNICORN)
gu = CosmicUnicorn()


gu.set_brightness(1.0)


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

faceframes =["work", "chillin","runnin", "ded", "den", "dino", "meeting", "fire", "me", "note"]

selected_frame = random.choice(faceframes)
print(f"Selected frame: {selected_frame}")

busy = False

def DoorStuff():
    global busy

    #auto set brightness from light sensor        
    #gu.set_brightness(max(.15,min(1.,gu.light()/600)))
    
    busy = True
    
    #pick random face
    selected_frame = random.choice(faceframes)
    print(f"Selected frame: {selected_frame}")
    # Use the correct list of frames based on selected_frame
    if selected_frame == "work":
        frame_list = work
    elif selected_frame == "chillin":
        frame_list = chillin
    elif selected_frame == "runnin":
        frame_list = runnin
    elif selected_frame == "ded":
        frame_list = ded
    elif selected_frame == "den":
        frame_list = den
    elif selected_frame == "dino":
        frame_list = dino
    elif selected_frame == "meeting":
        frame_list = meeting
    elif selected_frame == "fire":
        frame_list = fire
    elif selected_frame == "me":
        frame_list = me
    elif selected_frame == "note":
        frame_list = note
    else:
        frame_list = []  # Handle the case when selected_frame is invalid


    for frame in frame_list:
        gu.set_brightness(1.0)
        #fuckin comments need to be tabbed
        # Clear the display before drawing the new frame
        graphics.set_pen(black)
        graphics.clear()

        # Decode and display the current frame
        png.decode(0, 0, source=(frame.frame_x * frame_width, frame.frame_y * frame_height, frame_width, frame_height), scale=(1, 1), rotate=0)
        #gu.adjust_brightness(-0.25)  # brightness ad
                
        gu.update(graphics)        
        time.sleep(0.1)  # Adjust speed of anim

    # Clear display
    graphics.set_pen(black)
    graphics.clear()
    gu.update(graphics)
    
    time.sleep(5) # Time out so it does not trigger again immediately
    
    busy = False


while True:
    #if gu.is_pressed(CosmicUnicorn.SWITCH_A):
        if not busy:
            DoorStuff()