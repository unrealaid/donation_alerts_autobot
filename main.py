import datetime
import time
from RPA.Browser.Selenium import Selenium

""" WARNING!!! TESTED ONLY VIA GERMAN VPN. TO ADJUST BOT TO YOUR REGIONAL DONATIONALERTS - PING @UNREALAID"""
da_link = ''                    # link to donation page
your_username = ''
payments_delay = 30
card_details = {
    'card_number': '',
    'card_expiration': '',
    'card_cvv': ''              # recommended to use static cvv at least for bot running period
}


def wait_element(browser: Selenium, locator: str, timeout: int = 60, is_need_screen: bool = True):
    is_success = False
    timer = datetime.datetime.now() + datetime.timedelta(0, timeout)

    while not is_success and timer > datetime.datetime.now():
        if browser.does_page_contain_element(locator):
            try:
                elem = browser.find_element(locator)
                is_success = elem.is_displayed()
            except:
                time.sleep(1)
        if not is_success:
            if browser.does_page_contain_element(
                    "//div[@id='select2-drop']/ul[@class='select2-results']/li[@class='select2-no-results']"
            ):
                elem = browser.find_element(
                    "//div[@id='select2-drop']/ul[@class='select2-results']/li[@class='select2-no-results']"
                )
                if elem.is_displayed():
                    break
    if not is_success and is_need_screen:
        print('Element \'{}\' not available'.format(locator), 'ERROR')


browser: Selenium = Selenium()
d_dick = {
    'Ну что, стартуем ви-ви-ви пати?': '1',
    'donate text': 'donate amount',             #example
    'Золотой дождь окончен) (дождь из монет, а не то что вы подумали):': '1'
}
for key, value in d_dick.items():
    print(key)
    print(value)
    browser.open_available_browser(da_link, headless=True)
    wait_element(browser, '//input[@id="donatorName"]')
    browser.input_text('//input[@id="donatorName"]', your_username)
    browser.input_text('//div[@id="editable-area"]', key)
    browser.input_text_when_element_is_visible('//input[@id="amount"]', value)
    browser.click_element_when_visible('//div[@class="input-submit"]//a/span[text()="Поддержать"]')
    wait_element(browser, '//a[@class="hide-button"]')
    browser.click_element_when_visible('//a[@class="hide-button"]')
    browser.click_element_when_visible('//div[@class="b-pay__system-item_icon"]//span[text()="Bankkarte USD"]')
    browser.input_text_when_element_is_visible('//input[@name="email"]', 'gamer.man.orginal@gmail.com')
    time.sleep(1)
    browser.click_element_when_visible('//span[text()="Weiter zur Kasse"]')
    wait_element(browser, '//input[@id="cardnumber"]')
    browser.input_text_when_element_is_visible('//input[@id="cardnumber"]', card_details['card_number'])
    browser.input_text_when_element_is_visible('//input[@id="expdate"]', card_details['card_expiration'])
    browser.input_text_when_element_is_visible('//input[@id="cvc2"]', card_details['card_cvv'])
    browser.click_element_when_visible('//button[@type="submit"]')
    print('Check your bank application to confirm payment')
    time.sleep(payments_delay)
    browser.close_browser()
print('end')
