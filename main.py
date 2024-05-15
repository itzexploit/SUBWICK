from requests import get
from sys import argv
from colorama import Fore , init
from pystyle import Colorate , Colors
from os import system , name
from urllib.parse import urlparse
from threading import Thread as thr
from socket import gethostbyname

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX; rest = Fore.RESET

system('cls' if name == 'nt' else 'clear')

banner = '''
        ███████╗██╗   ██╗██████╗ ██╗    ██╗██╗ ██████╗██╗  ██╗
        ██╔════╝██║   ██║██╔══██╗██║    ██║██║██╔════╝██║ ██╔╝
        ███████╗██║   ██║██████╔╝██║ █╗ ██║██║██║     █████╔╝ 
        ╚════██║██║   ██║██╔══██╗██║███╗██║██║██║     ██╔═██╗ 
        ███████║╚██████╔╝██████╔╝╚███╔███╔╝██║╚██████╗██║  ██╗
        ╚══════╝ ╚═════╝ ╚═════╝  ╚══╝╚══╝ ╚═╝ ╚═════╝╚═╝  ╚═╝
              Created By John Wick - Team Pytho Learn
                                                      
'''

print(Colorate.Horizontal(Colors.red_to_blue,banner,2))

try:
    url = str(argv[1])
    path = str(argv[2])
except:
    print(f'\n  {red}<{yellow}url{red}> {red}<{yellow}sublist_path{red}> {blue}| {green}Example {red}: {yellow}python {green}main.py https://google.com list.txt {rest}')

def main():
    try:
        ff = open(path,'r').read().split()
        for f in ff:
            try:
                parsed_url = urlparse(url)
                target = parsed_url.netloc
                pinger = gethostbyname(target)
                ccc = f'{f}.{target}'
                cc = f'https://{ccc}'
                r = get(cc,timeout=3)
                print(f'\n  {red}[{yellow}+{red}]{cyan} SubDomain Finded {yellow}:{green} {cc} {red}:{yellow} {pinger} | Status_Code : {r.status_code}')
            except:
                print(f'\n  {red}[{yellow}+{red}]{red} {green}Cant Find This Subdomain {yellow}:{red} {cc}')
    except:
        pass

thr(target=main).start()
