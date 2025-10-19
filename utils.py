import sys, tty, termios
import requests
from bs4 import BeautifulSoup

def wait_a_press():
    input("Press Enter to unlock...")

def check_arguments(argv):
    if len(argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]

        '''
        url = "https://www.linkedin.com/checkpoint/lg/login-submit"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        payload = {
            "username": {username},
            "password": {password},
        }

        try:
            resp = requests.post(url, data=payload, headers=headers, timeout=10)
            print(resp)
        except requests.RequestException:
            return None, None

        # parse HTML e search for the div with id 'error-for-password'
        soup = BeautifulSoup(resp.text, "html.parser")
        if soup.find("div", id="error-for-password"):
            print("username or password are invalid")
            return None, None
        '''

        return username, password
    return None, None



