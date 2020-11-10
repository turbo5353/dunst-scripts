#!/usr/bin/env python3
import os
import sys
import alsaaudio

# Configuration
msgId = "991049"        # unique notification ID
volumeLength = 35       # maximum length of the volume bar
segment = "x"           # Character (or string) to be used for building the volume bar

m = alsaaudio.Mixer()
volume = m.getvolume()[0]
mute = m.getmute()[0]

if len(sys.argv) > 1:
    if sys.argv[1] == "toggle":
        mute = 1 - mute
        m.setmute(mute)
    else:
        value = int(sys.argv[1])
        volume = volume + value
        m.setvolume(volume)

msg = "muted"
if volume > 0 and mute != 1:
    length = volume / 100 * progressLength
    msg = segment * int(length)

dunstCmd = "dunstify -r " + msgId + " -u low " + msg
os.system(dunstCmd)

