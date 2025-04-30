# NGGAK USAH DI RENAME YAH KONTOL
# HARGAI DEVELOPER ASLINYA
# UDAH DI KASIH GRATIS, MASIH DI RENAME

import os, sys, time
from time import sleep

def main():
    port = 3000
    menu = '''
▭▬▭▬▭▬▭▬▭▬▭▬[ FEATUR LIST ]▭▬▭▬▭▬▭▬▭▬▭▬  ||  ▭▬▭▬▭▬▭▬▭▬▭▬[ TOOLS IMFO ]▭▬▭▬▭▬▭▬▭▬▭▬
\033[31m[ 1 ]\033[0m. START SERVER                      ||  DEVELOPER : \033[41m./Bio404Xploit\033[0m
\033[31m[ 2 ]\033[0m. DEVELOPER CONTACT                 ||  VERSION   : \033[41mBETA TEST\033[0m
\033[31m[ 3 ]\033[0m. GET TOKEN                         ||  TELEGRAM  : \033[41mt.me/Bio404X\033[0m
\033[31m[ 4 ]\033[0m. EXIT      	       	         ||  HITHUB    : \033[41mDikz-droid\033[0m
▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭  ||  ▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭
    '''

    os.system('clear')
    os.system('figlet -f small "SERVER CONTROL" | lolcat')
    print ('\n')
    print (menu)
    print ('\n')
    pilih = int(input('CHOOSE [ NUMBER ONLY ] : '))
    if pilih == 1:
       print ('\n')
       print (f'WEB INTERFACE IS HOSTED IN : \033[31mhttp://localhost:{port}\033[0m')
       os.system(f'php -S localhost:{port} > /dev/null 2>&1')
    elif pilih == 2:
       os.system('xdg-open https://t.me/@io404X')
       os.system('python run.py')
    elif pilih == 3:
       print ('\nSabar icibos')
       sleep(3)
       os.system('xdg-open https://sfl.gl/7Z3h')
       sleep(1)
       os.system('python run.py')
    elif pilih == 4:
       print ('\nSABAR YA KONTOL')
       exit()
    else:
       print ('PILIH YANG BENER GOBLOK')
       sleep(3)
       os.system('python run.py')
main()
