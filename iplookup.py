from tabulate import tabulate
import socket,sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) == 1:
    print(bcolors.FAIL + "1) You need to add a wordlist! Run the script like this: "+bcolors.WARNING+"python iplookup.py urls.txt" + bcolors.ENDC)
    print(bcolors.WARNING + "2) Don't add "+bcolors.FAIL+"(http://)"+bcolors.WARNING+" or"+bcolors.FAIL+" (https://)"+bcolors.WARNING+", it will cause error!"+ bcolors.ENDC)
    exit()

wordfile = sys.argv[1]

with open(wordfile, "r") as wordlist:
    for words in wordlist:
        x=words.strip()
        class bcolors:
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKCYAN = '\033[96m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            print(bcolors.WARNING+'The IP Address of '+bcolors.OKCYAN+f'{x}'+bcolors.WARNING+' is -->'+bcolors.FAIL+f' {socket.gethostbyname(x)}'+bcolors.ENDC)