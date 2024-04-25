#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
acousticConvolve is a tool that automatically records iterative acoustic convolutions

This is currently designed to run in the MacOS command line. 
It relies on the MacOs specific coreaudio.
The program should be installed in the file folder of the source audio files.

The program takes user input in the command line for: Instrument name, # of convolutions, input/output #.

It will also take these tacks, which will deactive the command line communication function.
-s | instument name
-n | number of convolutions
-i | input number
-o | output number
"""

import sys
import sounddevice as sd

# Sampling rate is 96000 by default but can be changed here
sampling = 96000

def getInput():
    # Initialize main variables
    instName = ''
    numCon = 0
    aInput = 0
    aOutput = 0

    humanCheck = False
    humanCheckStr = ''

    # Read command line input (tacks)
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-s':
            try:
                instName = sys.argv[i+1] 
            except:
                print("Instrument name tack error")
        elif sys.argv[i] == '-n':
            try:
                numCon = int(sys.argv[i+1])
            except:
                print("Convolution number tack error")
        elif sys.argv[i] == '-i':
            try:
                aInput = int(sys.argv[i+1])
            except:
                print("Input number tack error")
        elif sys.argv[i] == '-o':
            try:
                aOutput = int(sys.argv[i+1])
            except:
                print("Output number tack error")

            
    while humanCheck == False:
        # Fill in missing variable data
        if instName == '':
            instName = input("Please enter the instrument name: ")
        if numCon == 0:
            numCon = int(input("Please enter the number of convolutions: "))
        if aInput == 0:
            aInput = int(input("Please enter the input number: "))
        if aOutput == 0:
            aOutput = int(input("Please enter the output number: "))

        # Print main variables and check with user
        print("Please check main variable values:")
        print("Instrument name: " + instName)
        print("Number of Convolutions: " + str(numCon))
        print("Input: " + str(aInput) + " Output: " + str(aOutput))

        print("Sample file name would be: srcfilenamehere_" + instName + "_C" + str(numCon))

        humanCheckStr = input("Is this correct? (y/n): ")

        if humanCheckStr == 'y':
            humanCheck = True
        else:
            # Re-init vars
            instName = ''
            numCon = 0
            aInput = 0
            aOutput = 0 

            print("Please enter the information again:")

    return instName, numCon, aInput, aOutput

userInputList = getInput()

# Globalize variables from input
instName = userInputList[0]
numCon = userInputList[1]
aInput = userInputList[2]
aOutput = userInputList[3]

# Talk to user about audio device, confirm ins/outs
print("\nHere is a list of all available audio devices: \n")
print(sd.query_devices())

inDeviceID = input("\nPlease enter the numerical id of the audio device to be used: ")



