# Copyright (c) 2022 by James K. Lawless
# jimbo@radiks.net
# License: MIT / X11
# See: http://jiml.us/license2022.php
# for full license details.
 
import argparse 
from ctypes import *
from sys import getfilesystemencoding

winmm = windll.winmm
filesystemencoding = getfilesystemencoding()

def mciSend(s):
    enc=s.encode(filesystemencoding)    
    i=winmm.mciSendStringA(enc,0,0,0)
    if i!=0:
        print("Error %d in mciSendString %s" % ( i, s ))

def playMP3(mp3Name):
    mciSend("Close All")
    mciSend("Open \"%s\" Type MPEGVideo Alias theMP3" % mp3Name)
    mciSend("Play theMP3 Wait")
    mciSend("Close theMP3")
    
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.description="play an MP3 or WAV file"
    parser.add_argument("-file",required=True)
    args=parser.parse_args()
    playMP3(args.file)
