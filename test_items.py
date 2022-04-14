import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exists(browser):
    browser.implicitly_wait(10)
    browser.get(link)

    time.sleep(10)  # ждем 10 сек чтобы увидеть смену языка
    buttons = browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(buttons) > 0
