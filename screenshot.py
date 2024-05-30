import time
import datetime

from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

SCREENSHOT_DELAY_SECONDS=60


def screenshot_url(page: Page, url: str, screenshot_path: str):
    print(f'Screenshotting {url} to {screenshot_path}')
    page.goto(url)
    page.screenshot(path=screenshot_path, full_page=True)


def read_sites():
    sites = []
    with open('sites.txt') as f:
        sites = f.readlines()
    return sites


def get_hostname(url: str):
    return url.split("/")[2]


def save_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        sites = read_sites()
        date_time_string = datetime.datetime.now().isoformat().split(".")[0]

        for site in sites:
            hostname = get_hostname(site)
            screenshot_url(page, site, f'screenshots/{hostname}/{date_time_string}.png')

        browser.close()

print("Starting screenshot scraper")
while True:
    save_screenshots()
    print("Next run in " + str(SCREENSHOT_DELAY_SECONDS) + "seconds")
    time.sleep(SCREENSHOT_DELAY_SECONDS)