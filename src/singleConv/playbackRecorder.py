#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
playbackRecorder uses the sounddevice library stream function to playback an audio file 
while simultaneously recording a new audio file.

Args:
filename - Original file name
instName - Instrument Name
conNum - Convolution number
sRate - sampling rate
inDeviceID - numerical ID of audio device

Returns:
none, but a new audio file will be saved in the folder with the naming scheme orginalfilename-instName-C#
C# is for convolution number
"""

import sounddevice as sd

def playbackRecorder(filename, instName, conNum, sRate, deviceID):
    sd.default.device = deviceID
    curRecording = sd.playrec(myarray, sRate, channels=1)
