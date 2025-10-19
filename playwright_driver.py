from playwright.sync_api import sync_playwright
import time
import random

class PlaywrightDriver:
    def __init__(self, headless=False):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.page = None

    def start_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.page = self.browser.new_page()
        return self.page

    def go_to_page(self, url, t=0):
        if not self.page:
            raise Exception("Browser not started")
        self.page.goto(url) # only once fully charged does it go forward
        time.sleep(t)

    def login(self, username, password):
        username_input = self.page.query_selector("input#username")
        password_input = self.page.query_selector("input#password")

        if not username_input or not password_input:
            raise ValueError("Username or password input not found")

        time.sleep(5 * random.random())
        username_input.fill(username)
        time.sleep(5 * random.random())
        password_input.fill(password)
        time.sleep(5 * random.random())

        submit_btn = self.page.query_selector("button[type='submit'], input[type='submit']")
        if submit_btn:
            submit_btn.click()

    def get_html_grid(self):
        # respect CSP: I am in https://www.linkedin.com/games/zip/ -> I think that https://www.linkedin.com would also be fine
        iframe = self.page.frame(url="https://www.linkedin.com/games/view/zip/desktop")
        if iframe is None:
            raise Exception("Impossibile trovare l'iframe del gioco!")
        return iframe.content()

    def perform_moves(self, path):
        print("strating performing")
        # click on the page
        self.page.mouse.click(100, 200)
        path = path[:-1] # keep the last move
        for move in path:
            if move == "right":
                self.page.keyboard.press("ArrowRight")
            if move == "down":
                self.page.keyboard.press("ArrowDown")
            if move == "left":
                self.page.keyboard.press("ArrowLeft")
            if move == "up":
                self.page.keyboard.press("ArrowUp")
            print(f"Eseguo mossa: {move}")

            time.sleep(0.005)
    def close_browser(self):
        time.sleep(10)
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
