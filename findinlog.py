import os
for filename in os.listdir("C:\\Users\\stefa\\flog\\out"):
    print("Scanning file")
    print(filename)

    #Read line by line
    f = open("C:\\Users\\stefa\\flog\\out" + "\\" + filename, "r")
    line = f.readline()    
    while line:
        if "daniel" in line:
            print(line)
        line = f.readline()    
    f.close()

    #os.rename("C:\\Users\\stefa\\flog" + "\\" + filename, "out\\" + filename)
