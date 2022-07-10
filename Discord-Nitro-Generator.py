import string    
import random
import requests
import time
import colorama
import os
import ctypes
from dhooks import Webhook
import datetime

#Log
now = (datetime.datetime.now())

log_txt = open("DNG-Log.txt","w")
log_txt.write(now.strftime("German Timezone  |  Start: %d-%m-%y %H:%M:%S") + "\n")


proxy = '185.21.217.8:3128'
nogc = 0 # Number of generated Codes
nogcv = 0 # Number of generated Vaild Codes
nogci = 0 # Number of generated Invalid Codes
nogcf = 0 # Number of generated Failed to Check Codes

S = 10  # number of characters in the string.

print(f"{colorama.Fore.WHITE}")
print("  _                              _     ")
print(" | |                            | |    ")
print(" | |     __ ___  ____      _____| |__  ")
print(" | |    / _` \ \/ /\ \ /\ / / _ \ '_ \ ")
print(" | |___| (_| |>  <  \ V  V /  __/ |_) |")
print(" |______\__,_/_/\_\  \_/\_/ \___|_.__/ ")
print("                                       ")

#EULA
print(f"{colorama.Fore.CYAN}")
print("This project was created only for good purposes and personal use.")
print("By using Laxweb-Discord-Nitro-Generator, you agree that you hold responsibility and accountability of any consequences caused by your actions.")
print("Do not pass this programme off as yours. When using the programme for social media content, link my Discord profile (LennyMaxMine).")
print("By pressing Enter you agree the EULA of Laxweb-Discord-Nitro-Generator, Discord-TOS and Github-Eula.")
if input(f"{colorama.Fore.LIGHTCYAN_EX}(Press Enter)") == "":
    log_txt.write("Accepted EULA = True\n")
else:
    log_txt.write("Accepted EULA = True\n")
print(f"{colorama.Fore.WHITE}")



# check if user is connected to internet
print(f"{colorama.Fore.YELLOW}Checking Internet Connection...")
urlgoogle = "https://google.com"
try:
    response = requests.get(urlgoogle)  # Get the response from the url
    print(f"{colorama.Fore.GREEN}...Internet connection found")
    log_txt.write("Internet Connection = Found  |  Status Code: " + str(response.status_code))
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    # Tell the user
    input(f"{colorama.Fore.RED}...You are not connected to internet, check your connection and try again.\nPress enter to exit")
    log_txt.write("Internet Connection = Not Found  |  Status Code: " + str(response.status_code))
    exit()  # Exit program
print("")
log_txt.write("\n")


print(f"{colorama.Fore.YELLOW}Checking Discord-Web-Server Connection...")
urldiscord = "https://discord.com"
try:
    response = requests.get(urldiscord)  # Get the response from the url
    print(f"{colorama.Fore.GREEN}...Discord-Web-Server connection found")
    log_txt.write("Discord-Web-Server Connection = Found  |  Status Code: " + str(response.status_code))
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    # Tell the user
    input(f"{colorama.Fore.RED}...Failed to connect to the Discord-Web-Servers.")
    log_txt.write("Discord-Web-Server Connection = Found  |  Status Code: " + str(response.status_code))
print("")
log_txt.write("\n")


print(f"{colorama.Fore.YELLOW}Checking if banned from the Discord-Web-Servers...")
urldiscord2 = "https://discord.com"
response = requests.get(urldiscord2)  # Get the response from the url
if response.status_code == 401 or 403 or 429:
    print(f"{colorama.Fore.GREEN}...not banned Discord-Web-Servers.")
    log_txt.write("Discord-Web-Servers Maybe Banned = False  |  Status Code: " + str(response.status_code))
    time.sleep(.4)
else:
    # Tell the user
    log_txt.write("Discord-Web-Servers Maybe Banned = True  |  Status Code: " + str(response.status_code))
    input(f"{colorama.Fore.RED}...maybe banned  |  on the Discord-Web-Servers cannot check if the codes are valid. You can use a VPN and then try again...\n...Press Enter to Continue")
print(f"{colorama.Fore.WHITE}")
log_txt.write("\n")

inputwebhook = input(f"{colorama.Fore.YELLOW}If you want to use a webhook paste the link in here. Otherwise leave it empty. (This will slow down the generating!): ")
print(f"{colorama.Fore.WHITE}")
print("")

if inputwebhook != "":
    hook = Webhook(inputwebhook)
    rando = ''.join(random.choices(string.digits, k = 6))   
    hook.send("Your authentication code: " + rando)
    inputauth = input(f"{colorama.Fore.YELLOW}Please Insert your authentication code: ")
    log_txt.write("Used Webhook = True  |  Webhook ID: " + "'" + inputwebhook + "'")
    if inputauth == rando:
        print(f"{colorama.Fore.GREEN}Linked succesfull!{colorama.Fore.WHITE}")
        log_txt.write("  |  Authentication code = '" + rando + "'\n")
    else:
        input(f"{colorama.Fore.RED}Failed to Link...\n...Press Enter to exit{colorama.Fore.WHITE}")
        exit()
else:
    log_txt.write("Used Webhook = False\n")


try:
    howmanydcnlinks = int(input(f'{colorama.Fore.YELLOW}How many Discord-Nitro Links to generate?: '))  # Ask the user for the amount of codes
    log_txt.write("Asked for: '" + str(howmanydcnlinks) + "' Link(s) to generate  |  howmanydcnlinks = '" + str(howmanydcnlinks) + "'\n")
except ValueError:
    input(f"{colorama.Fore.RED}Specified input wasn't a number.\nPress enter to exit{colorama.Fore.WHITE}")
    log_txt.write("howmanydcnlinks wasnt a number  |  howmanydcnlinks = '" + str(howmanydcnlinks) + "'\n")
    exit()  # Exit program
print("")



for i in range(howmanydcnlinks):
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = S))   
    # print the random data  
    final_code = "discord.gift/" + str(ran)


    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/" + str(ran) + "?with_application=false&with_subscription_plan=true"

    r = requests.get(url)


    if r.status_code == 200:
        nogc = nogc + 1
        nogcv = nogcv + 1
        print(f"{colorama.Fore.YELLOW}NogC " + str(nogc) + f"{colorama.Fore.MAGENTA} |" + f"{colorama.Fore.BLUE} Status-Code " + str(r.status_code) + f"{colorama.Fore.MAGENTA} |" f"{colorama.Fore.GREEN} Valid{colorama.Fore.MAGENTA} | {colorama.Fore.WHITE}" + final_code) #Valid
        
        if inputwebhook != "":
            hook.send(final_code)
            time.sleep(0.1)

        valid_codestxt = open("DNG-Valid-Codes.txt","w")
        valid_codestxt.write(" Valid | " + final_code)
        valid_codestxt.close()

    elif r.status_code == 429:
        nogc = nogc + 1
        nogcf = nogcf + 1
        print(f"{colorama.Fore.YELLOW}NogC " + str(nogc) + f"{colorama.Fore.MAGENTA} |" + f"{colorama.Fore.BLUE} Status-Code " + str(r.status_code) + f"{colorama.Fore.MAGENTA} |" + f"{colorama.Fore.LIGHTRED_EX} Failed to Check{colorama.Fore.MAGENTA} | {colorama.Fore.WHITE}" + final_code) #Invalid

        if inputwebhook != "":
            hook.send(final_code)
            time.sleep(0.1)

    else:
        nogc = nogc + 1
        nogci = nogci + 1
        print(f"{colorama.Fore.YELLOW}NogC " + str(nogc) + f"{colorama.Fore.MAGENTA} |" + f"{colorama.Fore.BLUE} Status-Code " + str(r.status_code) + f"{colorama.Fore.MAGENTA} |" + f"{colorama.Fore.RED} Invalid{colorama.Fore.MAGENTA} | {colorama.Fore.WHITE}" + final_code) #Invalid

        if inputwebhook != "":
            hook.send(final_code)
            time.sleep(0.1)


#Log

print(f"{colorama.Fore.LIGHTMAGENTA_EX}")
print("Succesfully generated!")
print("")
print(f"{colorama.Fore.WHITE}Generated Codes: {colorama.Fore.WHITE}" + str(nogc))
print(f"{colorama.Fore.GREEN}Generated Valid Codes: {colorama.Fore.WHITE}" + str(nogcv))
print(f"{colorama.Fore.RED}Generated Invalid Codes: {colorama.Fore.WHITE}" + str(nogci))
print(f"{colorama.Fore.LIGHTRED_EX}Generated Failed to Check Codes: {colorama.Fore.WHITE}" + str(nogcf))
print(f"{colorama.Fore.LIGHTMAGENTA_EX}Press enter to Exit")
input("")
print(f"{colorama.Fore.WHITE}")

log_txt.write("Generated Codes: " + str(nogc) + "\n")
log_txt.write("Generated Valid Codes: " + str(nogcv) + "\n")
log_txt.write("Generated Invalid Codes: " + str(nogci) + "\n")
log_txt.write("Generated Failed to Check Codes: " + str(nogcf) + "\n")

now2 = (datetime.datetime.now())
log_txt.write(now2.strftime("German Timezone  |  End: %d-%m-%y %H:%M:%S"))
log_txt.close
