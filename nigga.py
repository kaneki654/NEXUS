import random
import pyfiglet
from fucksyon import *


class colors:
    whiteman = "\033[1;37m"
    blahdziheyl = "\033[91m"

a = 'THE NIGGA SQUAD'

print(colors.whiteman + a)

ascii_banner = pyfiglet.figlet_format('TNS')
print(ascii_banner)

print(colors.blahdziheyl + "[1]=={====PENTESTING=>")
print(colors.blahdziheyl + "[2]=={====NO=REDIRECT=FINDER=LINKS=>")
print(colors.blahdziheyl + "[3]=={====SETOOLKIT=>")
print(colors.blahdziheyl + "[4]=={====IP=GRABBER=>")

option = int(input(colors.whiteman + "=SELECT=PLEASE=: "))

if option == 1:
    clear()

    import subprocess

    ascii_banner = pyfiglet.figlet_format('PENTESTING')
    print(ascii_banner)
    
    time.sleep(2)
    print("type this")
    time.sleep(2)
    print("[./feroxbuster.exe]" "--url <target>")
    time.sleep(2)
    print("======= --help kapag gusto mo ng tulong niggar")
    time.sleep(2)

    print(colors.blahdziheyl + "DELETE KO NA FILES MO BYE:)")
    time.sleep(2)

    clear()
    ascii_banner = pyfiglet.figlet_format("3")
    print(ascii_banner)
    time.sleep(2)

    clear()
    ascii_banner = pyfiglet.figlet_format("2")
    print(ascii_banner)
    time.sleep(2)

    clear()
    ascii_banner = pyfiglet.figlet_format("1")
    print(ascii_banner)
    time.sleep(2)

    clear()
    print('░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░█░░█░░░░░░░░░░')
    print('░░░░░░░░░░░░░░█░░█░░░░░░░░░░')
    print('░░░░░░░░░░░░░░█░░█░░░░░░░░░░ ')
    print('░░░░░░░░░░░░░░█░░█░░░░░░░░░░ ')
    print('██████▄███▄████░░███▄░░░░░░░')
    print('▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░')
    print('▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░')
    print('▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░ ')
    print('▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░')
    print('▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░ ')
    print('▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░ ')
    ascii_banner = pyfiglet.figlet_format("SIKE!!")
    print(ascii_banner)


if option == 2:
    os.system("python Files/finder.py")
    time.sleep(0.3)
elif option == 3:
    clear()
    ascii_banner = pyfiglet.figlet_format("SETOOKIT")
    print(ascii_banner)

    print("[1]INSTALL SETOOLKIT")
    print("[2]SETUP")
    print("[3]SETOOLKIT")

    option = int(input("ROOT@TNS~$: "))

    if option == 1:
        os.system("git clone https://github.com/trustedsec/social-engineer-toolkit")
    if option == 2:
        os.system('python social-engineer-toolkit/setup.py')
    else:
        clear()
        print("pinundot mo naba ung install?")
        time.sleep(3)
        clear()
        print("oo?, tangina d ko alam problema mo sinasama mo pako haup ka")
        time.sleep(3)
        clear()
        exit()
    if option == 3:
        os.system('social-engineer-toolkit/setoolkit')
elif option == 4:
    clear()
    ascii_banner = pyfiglet.figlet_format('GRABBER')
    print(ascii_banner)

    print("[1]IP GRABBER")

    option = int(input('PILI KA ISA: '))

    if option == 1:
        os.system('python functions/iphack.py')       