#!/usr/bin/python
import os, sys, getopt

os.system("echo Hello from the other side!")


def main(argv):
   wordlistFile = ''
   try:
      opts, args = getopt.getopt(argv,"hw",["wordlist="])
   except getopt.GetoptError:
      print('bruteforce_generator.py -w <wordlist>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('bruteforce_generator.py -w <wordlist>')
         sys.exit()
      elif opt in ("-w", "--wordlist"):
         wordlistFile = arg
   print (wordlistFile)

if __name__ == "__main__":
   main(sys.argv[1:])