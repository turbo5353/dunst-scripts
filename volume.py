#!/usr/bin/env python3
import os
import sys
import alsaaudio

msgId = "991049"

m = alsaaudio.Mixer()
volume = m.getvolume()[0]
mute = m.getmute()[0]

if len(sys.argv) > 1:
    if sys.argv[1] == "toggle":
        mute = 1 - mute
        m.setmute(mute)
        pass
    else:
        value = int(sys.argv[1])
        volume = volume + value
        m.setvolume(volume)

msg = "muted"
if volume > 0 and mute != 1:
    msg = str(volume)

dunstCmd = "dunstify -r " + msgId + " -u low " + msg
os.system(dunstCmd)

