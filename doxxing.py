import os
from colorama import Fore

os.system('Doxxing Tool V1 | Made By Fax')

print('')
print(f'''{Fore.RED}▓█████▄  ▒█████  ▒██   ██▒▒██   ██▒ ██▓ ███▄    █   ▄████ 
▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░▒▒ █ █ ▒░▓██▒ ██ ▀█   █  ██▒ ▀█▒
░██   █▌▒██░  ██▒░░  █   ░░░  █   ░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
░▓█▄   ▌▒██   ██░ ░ █ █ ▒  ░ █ █ ▒ ░██░▓██▒  ▐▌██▒░▓█  ██▓
░▒████▓ ░ ████▓▒░▒██▒ ▒██▒▒██▒ ▒██▒░██░▒██░   ▓██░░▒▓███▀▒
 ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
 ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░░░   ░▒ ░ ▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░ ░  ░ ░ ░ ░ ▒   ░    ░   ░    ░   ▒ ░   ░   ░ ░ ░ ░   ░ 
   ░        ░ ░   ░    ░   ░    ░   ░           ░       ░ 
 ░                                                       ''')

print('')


print(f'{Fore.RED}           ╔══════════════════════════╗')
print(f'{Fore.RED}           ║' + '   [1] Name and state'+ f'{Fore.WHITE}     ║')
print(f'{Fore.RED}           ║' + '   [2] Phone number'+ f'{Fore.WHITE}       ║' )
print(f'{Fore.RED}           ║' + '   [3] Address' + f'{Fore.WHITE}            ║')
print(f'{Fore.RED}           ║' + '   [4] IP' + f'{Fore.WHITE}                 ║')
print(f'{Fore.WHITE}           ╚══════════════════════════╝')
print('')
menu = input(f'{Fore.RED}[?]>')

if menu == "1":
    firstname = input("[?] Whats there fist name? > ")
    lastname = input("[?] whats there last name? > ")
    state = input("[?] What city, State, or zip Do they live in? >")
    print(f"[+] https://www.fastpeoplesearch.com/name/{firstname}-{lastname}_{state}\nhttps://www.whitepages.com/name/{firstname}-{lastname}/{state}?fs=1&searchedName={firstname}%20{lastname}&searchedLocation={state}")

elif menu == "2":
    first = input("[?] what is the numbers first 3 digits? > ")
    middle = input("[?] what are the numbers second 3 digits? > ")
    last = input("[?] What are the numbers last 4 digits? > ")
    print(f"[-] https://www.fastpeoplesearch.com/{first}-{middle}-{last}\nhttps://www.whitepages.com/phone/1-{first}-{middle}-{last}")

elif menu == "3":
    house = input("[?] whats the house number?")
    street = input("[?] Street > ")
    city = input("[?] City > ")
    state = input("[?] State > ")
    print(f"[-] https://www.fastpeoplesearch.com/address/{house}-{street}_{city}-{state}")

elif menu == "4":
    ip = input("[?] IP > ")
    print(f"[-] https://www.geolocation.com/?languageCode=en_US&ip={ip}#ipresult")


