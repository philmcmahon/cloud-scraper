import time
import datetime
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright


def screenshot_url(page: Page, url: str, screenshot_path: str):
    print("Screenshotting: " + url + " to " + screenshot_path)
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
        iso_time = datetime.datetime.now().isoformat().split(".")[0]

        for site in sites:
            hostname = get_hostname(site)
            screenshot_url(page, site, "screenshots/" + hostname + "/" + iso_time + ".png")

        browser.close()


while True:
    save_screenshots()
    time.sleep(60*60*24)