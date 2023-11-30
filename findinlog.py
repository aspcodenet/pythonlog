import os
for filename in os.listdir("C:\\Users\\stefa\\flog\\out"): # \n
    print("Scanning file")
    print(filename)

    #Read line by line
    f = open("C:\\Users\\stefa\\flog\\out" + "\\" + filename, "r")

    lines = f.readlines()
    for line in lines:
        if "daniel" in line:
            print(line)

    f.close()

    #os.rename("C:\\Users\\stefa\\flog" + "\\" + filename, "out\\" + filename)
