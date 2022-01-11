#!/usr/bin/python
import os, sys, getopt

try:
    wordlistList = sys.argv[1]
    wordlist = open(wordlistList, "r")
except:
    print "Usage: bruteforce_generator.py wordlist.txt"
    sys.exit(2)

for line in wordlist:
    line = line.strip()
    print line