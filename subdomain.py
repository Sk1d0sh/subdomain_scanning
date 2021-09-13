# dnspython
# requests
# argparse
import requests
from os import path
import argparse
import sys


parser= argparse.ArgumentParser()
parser.add_argument('-t','--target',help='Indica el dominio',required=True)
parser.add_argument('-w','--wordlist',help='Indica la worlist',required=True)
parser = parser.parse_args()

def main ():
    if parser.target:
        if parser.wordlist:
            if path.exists(parser.wordlist):
                wordlist = open(parser.wordlist,'r')
                wordlist = wordlist.read().split('\n')

                for subdomain in wordlist:
                    url= subdomain+'.'+ parser.target
                    urlhttp="http://"+url
                    urlhttps="https://"+url
                    try:
                        requestHttp = requests.get(urlhttp)
                        requestHttps =requests.get(urlhttps)
                    except requests.ConnectionError:
                        pass
                    else:
                        if requestHttp.status_code == 200:
                            print("(+) Oyeee se encontro este subdominio --> "+urlhttp)
                        if requestHttps.status_code == 200:
                            print("(+) Oyeee se encontro este subdominio --> "+urlhttps)
                        else:
                            pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()