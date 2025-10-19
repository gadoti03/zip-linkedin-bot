from playwright.sync_api import sync_playwright
import time

URL = "https://www.linkedin.com/games/zip"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=False per vedere l'azione
    page = browser.new_page()
    page.goto(URL)
    print("inizio 10")

    time.sleep(10)
    print("fine 10")

    # Premi la freccia giù 5 volte
    for _ in range(5):
        page.keyboard.press("ArrowDown")
        time.sleep(0.5)

    time.sleep(2)
    browser.close()
