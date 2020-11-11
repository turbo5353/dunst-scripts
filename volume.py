#!/usr/bin/env python3
import sys
import alsaaudio
import subprocess

# Configuration

# unique notification ID
msgId = "991049"

# Volume bar
# maximum length of the volume bar (in segments)
volumeLength = 32
# String to be used for building the volume bar
segment = "─"
# String to be used for the empty part of the volume bar
emptySegment = " "
# String to be placed before the volume bar
beforeBar = ""
# String to be placed after the volume bar
afterBar = ""

# Icons
# High volume
iconHigh = "audio-volume-high-symbolic"
# Medium volume
iconMedium = "audio-volume-medium-symbolic"
# Low volume
iconLow = "audio-volume-low-symbolic"
# Audio muted
iconMuted = "audio-volume-muted-blocking-symbolic"

# Volume value
# 0: the current volume will not be shown
# 1: the current volume will be shown on the left of the notification
# 2: the current volume will be shown on the right of the notification
showValue = 2
# String to be placed before the volume number
beforeValue = " "
# String to be placed after the volume number
afterValue = "%"

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

icon = iconMuted
msg = "muted"
if volume > 0 and mute != 1:
    length = volume / 100 * volumeLength
    msg = beforeBar + segment * int(length)
    msg = msg + (emptySegment * (int(volumeLength) - int(length))) + afterBar

    if showValue == 1:
        msg = beforeValue + str(volume) + afterValue + msg
    elif showValue == 2:
        msg = msg + beforeValue + str(volume) + afterValue

    if volume < 33:
        icon = iconLow
    elif volume < 66:
        icon = iconMedium
    else:
        icon = iconHigh

dunstCmd = ["dunstify", "-r", msgId, "-u", "low"]

if icon != "":
    dunstCmd.append("-i")
    dunstCmd.append(icon)

dunstCmd.append(msg)

subprocess.run(dunstCmd)

