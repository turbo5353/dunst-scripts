#!/usr/bin/env python3
import sys
import alsaaudio

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

