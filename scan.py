#!/usr/bin/env python3
# Codename ZeroXsec666
# Don't change this codename, fuck bitch!


import requests
import argparse
import sys
import time


# colors
R = '\33[91m'
G = '\33[92m'
Y = '\33[93m'
C = '\33[96m'
B = '\33[94m'
P = '\33[95m'
D = '\33[90m'
E = '\33[0m'

# User-Agent but this fake
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

error = []
# comand line in terminal
def parse_args():
    # python as.py -s example.com
    parser = argparse.ArgumentParser(description='scan admin login and shell website')
    parser.add_argument('-s', '--scan', dest='scan', help='url target', required=True)
    return parser.parse_args()

def web():
    args = parse_args()
    url = args.scan
    #headers = {'User-Agent': user_agent}
    req = requests.get('http://'+url).status_code
    if req == 200:
        print('[{1}+{2}] {0} is {1}online{2}'.format(url,G,E))
    else:
        print('[{1}-{2}] {0} does not exist'.format(url,R,E))
        
def server():
    args = parse_args()
    url = 'http://'+args.scan
    headers = {'User-Agent': user_agent}
    req = requests.get(url, headers=headers)
    print('[{1}+{2}] Server: {1}{0}{2}'.format(req.headers['server'],G,E))
    
def robots():
    args = parse_args()
    url = args.scan
    headers = {'User-Agent': user_agent}
    host = 'http://'+url+'/'+'robots.txt'
    try:
        req = requests.get(host, headers=headers).status_code
        if req == 200:
            print('[{1}+{2}] Yeay found {1}{0}{2}'.format('robots.txt',G,E))
        else:
            print('[{1}-{2}] Can not found {1}{0}{2}'.format('robors.txt',R,E))
    except KeyboardInterrupt as e:
            print('[{0}-{1}] KeyboardInterrupt!'.format(R,E))
    except Exception as e:
        sys.exit(0)
        
# phpinfo() scan here
def phpinfo():
    print('{y}{:<60} {:<20}{e}'.format('[URL]','[STATUS]',y=Y,e=E))
    args = parse_args()
    url = args.scan
    phpinfo_list = open('phpinfo.txt', 'r') #wordlist change here
    headers = {'User-Agent': user_agent}
    for lines in phpinfo_list:
        lines = lines.replace('\n', '')
        host = 'http://'+url+'/'+lines
        try:
            req = requests.get(host, headers=headers).status_code
            if req == 200:
                print(' {:<60} | {g}{:<20}{e}'.format(host, req,g=G,e=E))
            elif req == 403:
                print(' {:<60} | {b}{:<20}{e}'.format(host, req,b=B,e=E))
            elif req == 404:
                print(' {:<60} | {r}{:<20}{e}'.format(host, req,r=R,e=E))
            else:
                print(' {:<60} | {r}{:<20}{e}'.format(host, req,r=R,e=E))
        except KeyboardInterrupt as e:
            print('[{0}-{1}] KeyboardInterrupt!'.format(R,E))
        except Exception as e:
            sys.exit(0)
            
# admin scan functions
def admin():
    print('{y}{:<60} {:20}{e}'.format('[URL]','[STATUS]',y=Y,e=E))
    args = parse_args()
    url = args.scan
    adm_list = open('admin.txt') #wordlist change here
    headers = {'User-Agent': user_agent}
    for lines in adm_list:
        lines = lines.replace('\n', '')
        host = 'http://'+url+'/'+lines
        try:
            req = requests.get(host, headers=headers).status_code
            if req == 200:
                print(' {:<60} | {g}{:<20}{e}'.format(host, req,g=G,e=E))
            elif req == 403:
                print(' {:<60} | {b}{:<20}{e}'.format(host, req,b=B,e=E))
            elif req == 404:
                print(' {:<60} | {r}{:<20}{e}'.format(host, req,r=R,e=E))
            else:
                print(' {:<60} | {r}{:<20}{e}'.format(host, req,r=R,e=E))
        except KeyboardInterrupt as e:
            print('[{0}-{1}] KeyboardInterrupt!'.format(R,E))
        except Exception as e:
            sys.exit(0)
            
# shell scan functions
def shell():
    print('{y}{:<60} {:20}{e}'.format('[URL]','[STATUS]',y=Y,e=E))
    args = parse_args()
    url = args.scan
    shl_list = open('shell.txt', 'r') #wordlist change here
    headers = {'User-Agent': user_agent}
    for lines in shl_list:
        lines = lines.replace('\n', '')
        host = 'http://'+url+'/'+lines
        try:
            req = requests.get(host, headers=headers).status_code
            if req == 200:
                print(' {:<60} | {g}{:<20}{e}'.format(host, req,g=G,e=E))
            elif req == 403:
                print(' {:<60} | {b}{:<20}{e}'.format(host, req,b=B,e=E))
            elif req == 404:
                print(' {:<60} | {r}{:<20}{e}'.format(host, req,r=R,e=E))
            else:
                print(' {:<60} | {r}{:<20}{e}'.format(host, req,r=R,e=E))
        except KeyboardInterrupt as e:
            print('[{0}-{1}] KeyboardInterrupt!'.format(R,E))
        except Exception as e:
            sys.exit(0)
        
# help or usage this my program            
def usage():
    info = '''{0}
Yeay error, usage example!

usage:
python scan.py -s htpp://urltarget.com

help:
python --help
           '''.format(E)
    print(info)
    
# add to main functions
def main():
    print('[{0}+{1}] Checking if website exist'.format(C,E))
    time.sleep(1)
    web()
    time.sleep(1)
    print('[{0}+{1}] Checking server'.format(C,E))
    time.sleep(1)
    server()
    time.sleep(1)
    print('[{0}+{1}] Checking robots.txt'.format(C,E))
    time.sleep(1)
    robots()
    time.sleep(1)
    print('[{0}+{1}] Wait...'.format(C,E))
    time.sleep(2)
    print('\n[{0}+{1}] Starting scan phpinfo(){1}'.format(C,E))
    phpinfo()
    print('\n[{0}+{1}] Starting scan admin login{1}'.format(C,E))
    admin()
    print('\n[{0}+{1}] Starting scan shell backdoor{1}'.format(C,E))
    shell()

# show this banner display
def banner():
    info = '''{c} Codename by ZeroXsec666 {c}

{c}|{e} © Copyright 2020 {c}| {e}http://dodilorentz.eu.org
           '''.format(r=R,c=C,y=Y,g=G,e=E)
    print(info)
    
# i will call main here
if __name__ == '__main__':
    #args = parse_args()
    if len(sys.argv) < 2:
        usage()
        #print(parser.usage())
        sys.exit(0)
    else:
        banner()
        main()
        print('\n[{0}+{1}] Program finished....'.format(C,E))