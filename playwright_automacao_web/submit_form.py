from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://aisweb.decea.mil.br/?i=notam')
    #page.locator('xpath=//*[@id="_form_1919_"]/div[1]/div[1]/div/input').click()
    page.fill('xpath=//*[@id="icaocode"]', 'sbgo')
    page.locator('xpath=//*[@id="a"]/form/div/div[3]/div/input[2]').click()
    time.sleep(15)
    