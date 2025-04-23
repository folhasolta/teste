import os
import time
from colorama import init, Fore, Style

init(autoreset=True)

k = Fore.WHITE
v = Style.RESET_ALL
w = Fore.RED
ww = Fore.RED

def slowprint(text, delay=0.02):
    print(text)
    time.sleep(delay)

os.system("clear")
print()

ascii = [
    f"{k}   _________ __                              __    ",
    f"{k}  /   _____/|  |   _______  _______    ____ |  | __",
    f"{k}  \_____  \ |  |  /  _ \  \/ /\__  \ _/ ___\|  |/ /",
    f"{k}  /        \|  |_(  <_> )   /  / __ \\\\  \___|    < ",
    f"{k} /_______  /|____/\____/ \_/  (____  /\___  >__|_ \\",
    f"{k}         \/                        \/     \/     \\/",
]

menu = [
    f"     {w}[ {v}1{w} ] {v}Del canais     {w}[ {v}10{w} ] {v}Ban all",
    f"     {w}[ {v}2{w} ] {v}Ren serv       {w}[ {v}11{w} ] {v}+Cargos",
    f"     {w}[ {v}3{w} ] {v}Foto serv      {w}[ {v}12{w} ] {v}Del emojis",
    f"     {w}[ {v}4{w} ] {v}+Canais        {w}[ {v}13{w} ] {v}Del sticker",
    f"     {w}[ {v}5{w} ] {v}Spam msg       {w}[ {v}14{w} ] {v}Del sons",
    f"     {w}[ {v}6{w} ] {v}Ren canais     {w}[ {v}15{w} ] {v}DM all",
    f"     {w}[ {v}7{w} ] {v}Kick all       {w}[ {v}16{w} ] {v}Del cargos",
    f"     {w}[ {v}8{w} ] {v}Call topo      {w}[ {v}17{w} ] {v}Nick all",
    f"     {w}[ {v}9{w} ] {v}Spam fotos     {w}[ {v}18{w} ] {v}Wipe all",
]

for linha in ascii:
    slowprint(linha, delay=0.03)

print()

for linha in menu:
    slowprint(linha, delay=0.03)

print()
token = input(f"{v}Token{w}: ")
