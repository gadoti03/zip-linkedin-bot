import sys, tty, termios
import requests
from bs4 import BeautifulSoup

def wait_a_press():
    input("Press Enter to unlock...")

def check_arguments(argv):
    if len(argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]

        return username, password
    return None, None



