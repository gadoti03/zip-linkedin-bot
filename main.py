from playwright_driver import PlaywrightDriver
from solver import solve
from grid_parser import parser
from utils import wait_a_press, check_arguments
import sys, tty, termios, getpass

def main():
    url_game = "https://www.linkedin.com/games/zip/"
    url_login = "https://www.linkedin.com/login/it?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

    # check arguments
    username, password = check_arguments(sys.argv)

    # start Playwright
    driver = PlaywrightDriver(headless=False)
    driver.start_browser()

    # login
    driver.go_to_page(url_login)
    if username and password:
        driver.login(username, password)

    wait_a_press()

    # go to game
    driver.go_to_page(url_game, 1)

    # get grid
    grid = parser(driver.page.content())
    print("Grid read:", grid)

    # compute the path
    path = solve(grid)
    print("Path computed:", path)

    # execute moves
    driver.perform_moves(path)

    # close browser
    driver.close_browser()

if __name__ == "__main__":
    main()
