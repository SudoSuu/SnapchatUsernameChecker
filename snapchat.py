import requests
from colorama import Fore
import time
import pyfiglet
ascii_banner = pyfiglet.figlet_format("SudoSuu")
print(ascii_banner)
print("Snapchat Username Checker")
print("By: SudoSuu")
print('\n')

url = "https://accounts.snapchat.com:443/accounts/get_username_suggestions"
# DONT CHANGE
headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
           "Accept": "*/*", "Origin": "https://accounts.snapchat.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "same-origin", "Sec-Fetch-Dest": "empty", "Referer": "https://accounts.snapchat.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
xsrf_token = "JxVkpuY3VbHfOFagfT0csQ"
cookies = {"xsrf_token": xsrf_token}


def single_request(username):
    data = {"requested_username": username,
            "xsrf_token": xsrf_token}
    res = requests.post(url, headers=headers,
                        cookies=cookies, data=data)
    if "TAKEN" in res.text:
        print(username + Fore.LIGHTBLUE_EX +
              " > Used not available" + Fore.WHITE)
    elif "DELETED" in res.text:
        print(username + Fore.RED +
              " > this account has been closed or deleted" + Fore.WHITE)
    elif "OK" in res.text:
        print(username + Fore.GREEN +
              " > Available " + Fore.WHITE + " - saved in availables.txt" + Fore.WHITE)
        with open('availables.txt', 'a+') as f:
            f.write("\n"+username)
            f.close()
    elif "TOO_LONG" in res.text:
        print(username + Fore.RED + " : Username is too long" + Fore.WHITE)
    elif "TOO_SHORT" in res.text:
        print(username + Fore.RED + " : Username is too short" + Fore.WHITE)
    elif "INVALID_BEGIN" in res.text:
        print(username + Fore.RED +
              " : Usernames must start with a letter" + Fore.WHITE)
    elif "INVALID_CHAR" in res.text:
        print(username + Fore.RED +
              " : Usernames can only include latin letters, numbers, and one of -, _, or . but no special characters" + Fore.WHITE)
    else:
        print(res.text)


def checksingel(singel_request):
    username = input("Enter a username: ")
    singel_request(username)


def checklist(singel_request):
    path = input("Enter path file: ")
    f = open(path, 'r+')
    Lines = f.readlines()
    count = 0
    for line in Lines:
        username = line.strip()
        singel_request(username)
        time.sleep(2)  # DO NOT decrease it
        count += 1
    f.close()


print(Fore.YELLOW + "[1] " + Fore.WHITE + "Check a single username")
print(Fore.YELLOW + "[2] " + Fore.WHITE + "Check from list")
option = input("Select an option: ")
if option == "1":
    while option == "1":
        checksingel(single_request)
elif option == "2":
    while option == "2":
        checklist(single_request)
else:
    print(Fore.RED+'invaild options!')
