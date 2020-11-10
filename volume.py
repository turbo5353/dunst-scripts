#!/usr/bin/env python3
import os
import sys
import alsaaudio

# Configuration

# unique notification ID
msgId = "991049"

# maximum length of the volume bar
volumeLength = 35

# Character (or string) to be used for building the volume bar
segment = "x"

# icon to be used in the notification
icon = "audio-volume-muted-blocking-symbolic"

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
    length = volume / 100 * volumeLength
    msg = segment * int(length)

dunstParams = "-r " + msgId + " -u low "
if icon != "":
    dunstParams = dunstParams + " -i " + icon + " "

dunstCmd = "dunstify " + dunstParams + msg
os.system(dunstCmd)

