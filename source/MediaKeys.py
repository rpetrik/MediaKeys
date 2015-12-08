"""
MediaKeys
=======
# Description
This script sends Windows media key event to the system based on first parameter to the script that gets looked up in
a dictionary and mapped to an appropriate command

It is a python script, so you have to have Python3 installed

# Usage
I use it by having created following shortcuts (.lnk) in my system path

location of the item                                                        name
"C:\Python34\python.exe c:\projects\personal\MediaKeys\source\MediaKeys.py p"      p
"C:\Python34\python.exe c:\projects\personal\MediaKeys\source\MediaKeys.py n"      n
"C:\Python34\python.exe c:\projects\personal\MediaKeys\source\MediaKeys.py pp"     pp
"C:\Python34\python.exe c:\projects\personal\MediaKeys\source\MediaKeys.py u"      u
"C:\Python34\python.exe c:\projects\personal\MediaKeys\source\MediaKeys.py d"      d

Now I can control music from my non Media Key enabled keyboard by:
To play/pause
Win+r, p, Enter 

To move to next song
Win+r, n, Enter

To move to previous/beginning of song
Win+r, pp, Enter

Volume Up/Down the same with u & d,

to repeat the command, just do: Win+r, Enter
I use it with MS Groove music, but is should work with any decent media player

# License
This is pretty much all taken from http://stackoverflow.com/questions/11906925/python-simulate-keydown (Noctis Skytower)

"""
import ctypes
import sys
import time

# from WinUser.h
MOUSEEVENTF_XDOWN = 0x0080
MOUSEEVENTF_XUP = 0x0100
MOUSEEVENTF_WHEEL = 0x0800
VK_XBUTTON1 = 0x05
VK_XBUTTON2 = 0x06
VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_BROWSER_BACK = 0xA6
VK_BROWSER_FORWARD = 0xA7

SendInput = ctypes.windll.user32.SendInput

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    ReleaseKey(hexKeyCode)

if __name__ == '__main__':
    dct = {
        "u" : VK_VOLUME_UP,
        "d" : VK_VOLUME_DOWN,
        "p" : VK_MEDIA_PLAY_PAUSE,
        "n" : VK_MEDIA_NEXT_TRACK,
        "pp": VK_MEDIA_PREV_TRACK,
    }    
    if (len(sys.argv) > 1):
        PressKey(dct.get(sys.argv[1], VK_MEDIA_PLAY_PAUSE))
