# ps jag vet att vi gör en sämre grep ;)

import os

baseDir = "C:\\Users\\stefa\\flog\\out"
lookFor = "ste"

for filename in os.listdir(baseDir):
    print("Scanning file")
    print(filename)

    #Read line by line
    f = open(baseDir + "\\" + filename, "r")
    lines = f.readlines()
    for line in lines:
        if lookFor in line:
            print(line)

    f.close()

