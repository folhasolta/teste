import os
from colorama import init, Fore

init(autoreset=True)

# Exemplo de cor rosa claro e branco no meio da ASCII art
rosabosta = '\033[38;2;255;182;193m'  # Rosa claro
branco = '\033[97m'  # Branco padrão
reset = '\033[0m'    # Reset da cor

ascii_art = f"""{rosabosta}

              a          a
             aaa        aaa
            aaaaaaaaaaaaaaaa
           aaaaaaaaaaaaaaaaaa  {branco}  _____                  {rosabosta}
          aaaaaaaaaaaaaaaaaaaa {branco} / ____|                {rosabosta}
          aaaaaaaaaaaaaaaaaaaa {branco}| (___  _   _ ___ _   _ {rosabosta}
           aaaaaaaaaaaaaaaaaa  {branco} \___ \| | | / __| | | |{rosabosta}
            aaaaaaaaaaaaaaa    {branco} ____) | |_| \__ \ |_| |{rosabosta}   
             aaaaaaaaaaaaaa    {branco}|_____/ \____|___/\____|{rosabosta}
  a         aaaaaaaaaaaaaaaa            
 aaa       aaaaaaaaaaaaaaaaaa                           {branco} _____      {rosabosta}
 aaa      aaaaaaaaaaaaaaaaaaaa                          {branco}|  __ \     {rosabosta}
 aaa     aaaaaaaaaaaaaaaaaaaaaa                         {branco}| |  | | ___  {rosabosta}
 aaa    aaaaaaaaaaaaaaaaaaaaaaaa                        {branco}| |  | |/ _ \  {rosabosta}
  aaa   aaaaaaaaaaaaaaaaaaaaaaaa                        {branco}| |__| |  __/           {rosabosta}
  aaa   aaaaaaaaaaaaaaaaaaaaaaaa           {branco} _           {branco}|_____/ \___|    {rosabosta}  
  aaa    aaaaaaaaaaaaaaaaaaaaaa            {branco}| |                     {rosabosta}
   aaa    aaaaaaaaaaaaaaaaaaaa             {branco}| | ___  ___ _   _ ___  {rosabosta}
    aaaaaaaaaaaaaaaaaaaaaaaaaa       {branco}  _   | |/ _ \/ __| | | / _ \   {rosabosta}
     aaaaaaaaaaaaaaaaaaaaaaaaa        {branco}{branco}| |__| |  __/\__ \ |_| \__ \ {rosabosta}
                                       {branco}\____/ \___||___/\__,_|___/   {rosabosta}
"""
# Função principal
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ascii_art)

if __name__ == '__main__':
    main()
