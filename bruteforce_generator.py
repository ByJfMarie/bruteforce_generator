#!/usr/bin/python
import os, sys, getopt

try:
    wordlistList = sys.argv[1]
    wordlist = open(wordlistList, "r")
except:
    print ("Usage: bruteforce_generator.py wordlist.txt")
    sys.exit(2)

for line in wordlist:
    line = line.strip()
    char = len(line)
    os.system("crunch "+str(char)+" "+str(char)+" -t "+line+" -o bruteforce.txt")
    os.system("cat bruteforce.txt >> bruteforce_all.txt")
    