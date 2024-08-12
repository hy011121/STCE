import subprocess
import sys
import time
import os
import random
import string
import requests
import pyfiglet
from fake_useragent import UserAgent
from termcolor import colored

ascii_banner = pyfiglet.figlet_format("STCE")
colored_banner = colored(ascii_banner, color='magenta')

RESET = "\033[0m"
GREEN_TEXT = "\033[32m"
BLACK_BG = "\033[40m"

required_modules = [
    "fake_useragent",
    "requests",
    "termcolor",
    "pyfiglet"
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    print_with_delay(GREEN_TEXT + "Welcome to the Spammer Telegram Complaint Engine setup wizard.\nWe will now install all necessary dependencies for the program to work correctly.\nThe installation will take no more than 3 minutes.\n3\n2\n1\n" + RESET)
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"{module} is already installed.")
        except ImportError:
            print(f"Installing {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + f"Module {module} has been installed." + RESET)

    print_with_delay(GREEN_TEXT + "Starting Spammer Telegram Complaint Engine program..." + RESET)
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')

check_and_install_modules()
os.system('cls' if os.name == 'nt' else 'clear')

def generate_phone_number():
    country_codes = ['+7', '+380', '+375']
    country_code = random.choice(country_codes)
    phone_number = ''.join(random.choices('0123456789', k=10))
    formatted_phone_number = f'{country_code}{phone_number}'
    return formatted_phone_number

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)
    email = f"{username}@{domain}"
    return email

def load_proxies(file_path):
    try:
        with open(file_path, 'r') as file:
            proxies = file.read().splitlines()
        return proxies
    except Exception as e:
        print(f"Failed to load proxies: {str(e)}")
        return []

def send_complaint(username, telegram_id, number, email, repeats, complaint_choice, proxies=None):
    url = 'https://telegram.org/support'
    user_agent = UserAgent().random
    headers = {'User-Agent': user_agent}
    complaints_sent = 0

    if complaint_choice == "1":
        text = f'Hello Telegram support! The account {username}, {telegram_id} uses a virtual number purchased from a website for number activation. The number is unrelated to the account. Please investigate. Thank you!'
    elif complaint_choice == "2":
        text = f'The account {username}, {telegram_id} purchased premium service on your platform to bypass penalties for spam and sends spam messages to users and chats. Please check the information!'
    elif complaint_choice == "3":
        text = f"Hello. The account {username}, id {telegram_id} is insulting me and my mother. I am very uncomfortable, so I am writing to you. Please investigate and block this user as it violates the service's policy. Thank you."
    elif complaint_choice == "4":
        text = f"Hello. The account {username}, id {telegram_id} frequently violates Telegram's policies by insulting users, leaking personal data, and selling various services. Please investigate and take action against this account."
    elif complaint_choice == "5":
        text = f"Hello, I lost my Telegram account due to hacking. I fell for a phishing link, and now someone else is using my account. They set a cloud password so I can't access my account. Please reset the sessions or delete this account as I have important data there. My username is {username}, and my ID if the hacker changed the username is {telegram_id}."
    elif complaint_choice == "6":
        text = f"Hello, while browsing Telegram, I noticed a user who is sending spam messages. It is very annoying to me and other users. Their account is: {username}, ID {telegram_id}. Please investigate and block this user. Thank you."
    elif complaint_choice == "7":
        text = f"Hello, I discovered a user on Telegram inflating reactions, subscriptions, and views on their channel. The link to the posts with inflation and the admin account: {username}, admin ID in case the username changes: {telegram_id}. Please investigate and block the user as it violates Telegram's rules."
    elif complaint_choice == "8":
        text = f"I discovered a user on Telegram inflating reactions, subscriptions, and views on their channel. The link to the posts with inflation and the admin account: {username}, admin ID in case the username changes: {telegram_id}. Please investigate and block the user as it violates Telegram's rules."

    payload = {'text': text, 'number': number, 'email': email}

    try:
        for _ in range(int(repeats)):
            proxy = random.choice(proxies) if proxies else None
            proxy_dict = {'http': proxy, 'https': proxy} if proxy else None
            response = requests.post(url, headers=headers, data=payload, proxies=proxy_dict)
            if response.status_code == 200:
                print(colored(f"Complaint successfully sent", 'green'))
                print(colored(f"From: {email} {number}", 'cyan'))
            else:
                print("Failed to send. Code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

def complaint():
    print(colored_banner)
    print("by pr0xit and dark snos")
    print("ReCode by tls123")
    print(colored("[1] Virtual Number", "magenta"))
    print(colored("[2] Premium", "magenta"))
    print(colored("[3] Insult", "magenta"))
    print(colored("[4] Policy Violation", "magenta"))
    print(colored("[5] Session Deletion", "magenta"))
    print(colored("[6] Spam", "magenta"))
    print(colored("[7] Prices", "magenta"))
    print(colored("[8] Inflation", "magenta"))
    complaint_choice = input(colored("Enter the reason for the complaint-> ", "magenta"))

    proxies = load_proxies('proxy.txt')

    if complaint_choice in ["1", "2", "3", "4", "6", "7", "8"]:
        username = input("Enter @username: ")
        telegram_id = input("Enter Telegram ID: ")
        repeats = int(input("Enter the number of complaints: "))
        for _ in range(repeats):
            number = generate_phone_number()
            email = generate_random_email()
            send_complaint(username, telegram_id, number, email, 1, complaint_choice, proxies)
    elif complaint_choice == '5':
        username = input("Enter username: ")
        telegram_id = input("Enter Telegram ID: ")
        repeats = int(input("Enter the number of complaints: "))
        number = input("Enter the account phone number: ")
        email = generate_random_email()
        send_complaint(username, telegram_id, number, email, repeats, complaint_choice, proxies)
    else:
        print("Invalid reason")
    
    user_choice = input(colored("Enter '1' to return to the menu or '0' to exit: ", "magenta"))
    if user_choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        complaint()
    elif user_choice == '0':
        print("Exiting the program.")
        exit(0)

complaint()
