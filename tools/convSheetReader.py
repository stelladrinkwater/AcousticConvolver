import pandas as pd
import shutil

"""
This is an example script for reading file names from an Excel sheet and moving them to a folder.
Written quick and messily, not be resused, but to be referenced.
"""

convSheet = pd.read_excel('./pyRead.xlsx')

fromStrings = convSheet['Viola - Strings'].tolist()
fromPiano = convSheet['Viola - Piano'].tolist()

fromPianoPaths = []
fromStringsPaths = []

# Remove spaces in file names, then add "./" and ".wav" for paths

for file in fromStrings:
    try:   
        file = ''.join(file.split())
        file = "./Strings/" + file + ".wav"
        fromPianoPaths.append(file)
    except:
        print("Error on file " + str(file))
        fromStrings.remove(file)
        print("File removed")

for file in fromPiano:
    try:   
        file = ''.join(file.split())
        file = "./Piano/" + file + ".wav"
        fromStringsPaths.append(file)
    except:
        print("Error on file " + str(file))
        fromStrings.remove(file)
        print("File removed")

# Now to copy
for path in fromStringsPaths:
    source = path
    dest = path.replace("./Strings/", "./violaSrc/Strings/")
    shutil.copyfile(source, dest)

for path in fromPianoPaths:
    source = path
    dest = path.replace("./Piano/", "./violaSrc/Piano/")
    shutil.copyfile(source, dest)