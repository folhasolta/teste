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

os.system("cls" if os.name == "nt" else "clear")
print()

ascii = [
    f"{k}     ██████  ██▓     ▒█████   ██▒   █▓ ▄▄▄       ▄████▄   ██ ▄█▀{ww}    ▄▄▄▄    ▒█████ ▓██   ██▓  ██████ ",
    f"{k}   ▒██    ▒ ▓██▒    ▒██▒  ██▒▓██░   █▒▒████▄    ▒██▀ ▀█   ██▄█▒ {ww}   ▓█████▄ ▒██▒  ██▒▒██  ██▒▒██    ▒ ",
    f"{k}  ░  ▓██▄   ▒██░    ▒██░  ██▒ ▓██  █▒░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░  {ww}  ▒██▒ ▄██▒██░  ██▒ ▒██ ██░░ ▓██▄   ",
    f"{k}     ▒   ██▒▒██░    ▒██   ██░  ▒██ █░░░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄  {ww}  ▒██░█▀  ▒██   ██░ ░ ▐██▓░  ▒   ██▒",
    f"{k}   ▒██████▒▒░██████▒░ ████▓▒░   ▒▀█░   ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄ {ww}  ░▓█  ▀█▓░ ████▓▒░ ░ ██▒▓░▒██████▒▒",
    f"{k}   ▒ ▒▓▒ ▒ ░░ ▒░▓  ░░ ▒░▒░▒░    ░ ▐░   ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒{ww}   ░▒▓███▀▒░ ▒░▒░▒░   ██▒▒▒ ▒ ▒▓▒ ▒ ░",
    f"{k}    ░ ░▒  ░ ░░ ░ ▒  ░  ░ ▒ ▒░    ░ ░░    ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░{ww}   ▒░▒   ░   ░ ▒ ▒░ ▓██ ░▒░ ░ ░▒  ░ ░",
    f"{k}     ░  ░  ░    ░ ░   ░ ░ ░ ▒       ░░    ░   ▒   ░        ░ ░░ ░ {ww}    ░    ░ ░ ░ ░ ▒  ▒ ▒ ░░  ░  ░  ░  ",
    f"{k}          ░      ░  ░    ░ ░        ░        ░  ░░ ░      ░  ░   {ww}    ░          ░ ░  ░ ░           ░  ",
    f"{k}                                 ░             ░              {ww}         ░          ░ ░",
]

menu = [
    f"    {w}[ {v}1 {w}] {v}Deletar todos os canais              {w}[ {v}10 {w}] {v}Banir todos os membros",
    f"    {w}[ {v}2 {w}] {v}Mudar nome do servidor               {w}[ {v}11 {w}] {v}Criar vários cargos",
    f"    {w}[ {v}3 {w}] {v}Mudar foto do servidor               {w}[ {v}12 {w}] {v}Deletar todos os emojis",
    f"    {w}[ {v}4 {w}] {v}Criar vários canais                  {w}[ {v}13 {w}] {v}Deletar todos os stickers",
    f"    {w}[ {v}5 {w}] {v}Spammar mensagem em canais           {w}[ {v}14 {w}] {v}Deletar todos os sons",
    f"    {w}[ {v}6 {w}] {v}Renomear todos os canais             {w}[ {v}15 {w}] {v}Enviar DM em massa para os membros",
    f"    {w}[ {v}7 {w}] {v}Kickar todos os membros              {w}[ {v}16 {w}] {v}Apagar todos cargos",
    f"    {w}[ {v}8 {w}] {v}Criar call no topo                   {w}[ {v}17 {w}] {v}Mudar apelido de todos membros",
    f"    {w}[ {v}9 {w}] {v}Spammar fotos                        {w}[ {v}18 {w}] {v}Destruir tudo",
]

for linha in ascii:
    slowprint(linha, delay=0.03)

print()

for linha in menu:
    slowprint(linha, delay=0.03)

print()
token = input(f"{v}Token{w}: ")
