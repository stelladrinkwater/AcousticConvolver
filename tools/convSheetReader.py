import pandas as pd
import shutil

"""
This is an example script for reading file names from an Excel sheet and moving them to a folder.
Written quick and messy.
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
        fromStringsPaths.append(file)
    except:
        print("Error on file " + str(file))
        fromStrings.remove(file)
        print("File removed")

for file in fromPiano:
    try:   
        file = ''.join(file.split())
        file = "./Piano/" + file + ".wav"
        fromPianoPaths.append(file)
    except:
        print("Error on file " + str(file))
        fromStrings.remove(file)
        print("File removed")


# Now to copy
for path in fromStringsPaths:
    try:
        source = str(path)
        dest = path.replace("./Strings/", "./violaSrc/Strings/")
        shutil.copyfile(source, dest)
        print("Copied file " + str(source))
    except:
        print("Error on file " + str(path))

for path in fromPianoPaths:
    try:
        source = path
        dest = path.replace("./Piano/", "./violaSrc/Piano/")
        shutil.copyfile(source, dest)
        print("Copied file " + str(source))
    except:
        print("Error on file " + str(path))