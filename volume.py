#!/usr/bin/env python3
import sys
import alsaaudio
import subprocess

# Configuration

# unique notification ID
msgId = "991049"

# maximum length of the volume bar
volumeLength = 32

# Character (or string) to be used for building the volume bar
segment = "─"

# icon to be used in the notification
icon = "audio-volume-muted-blocking-symbolic"

# If true, the current volume percent will be included in the notification
showPercent = True

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

    if showPercent:
        msg = msg + (" " * (int(volumeLength) - int(length)))
        msg = msg + " " + str(volume) + "%"

dunstCmd = ["dunstify", "-r", msgId, "-u", "low"]

if icon != "":
    dunstCmd.append("-i")
    dunstCmd.append(icon)

dunstCmd.append(msg)

subprocess.run(dunstCmd)

