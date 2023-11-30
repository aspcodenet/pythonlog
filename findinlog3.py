# ps jag vet att vi gör en sämre grep ;)

import os
import argparse


parser = argparse.ArgumentParser(description='Find logged in user in logfile')
parser.add_argument('--username', metavar='Username',  required=True,
                    help='Username to search for')
parser.add_argument('--dir', metavar='Directory',  required=True,
                    help='Directory to search in')

args = parser.parse_args()




for filename in os.listdir(args.dir):
    print("Scanning file")
    print(filename)

    #Read line by line
    f = open(args.dir + "\\" + filename, "r")
    lines = f.readlines()
    for line in lines:
        if args.username in line:
            print(line)

    f.close()

