from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, dr=None):
        if dr is None:
            self.dr = webdriver.Chrome()
        else:
            self.dr = dr

    def click(self, locate):
        element = WebDriverWait(self.dr, 5).until(expected_conditions.element_to_be_clickable(locate))
        element.click()

    def type(self, locate, msg):
        self.dr.find_element(*locate).send_keys(msg)


class Index(BasePage):
    a_contacts = (By.ID, "menu_contacts")

    def goto_contact(self):
        self.click(self.a_contacts)
        return Contacts(self.dr)


class Contacts(BasePage):
    a_add_member = (By.CSS_SELECTOR, "div.js_operationBar_footer>.qui_btn.ww_btn.js_add_member")
    input_username = (By.CSS_SELECTOR, "#username")
    input_acctId = (By.CSS_SELECTOR, '#memberAdd_acctid')
    input_phone = (By.CSS_SELECTOR, "#memberAdd_phone")
    checkbox_sendInvite= (By.NAME, "sendInvite")
    button_save = (By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save")

    def add_member(self, username, acct_id, phone_number):
        sleep(10)
        self.click(self.a_add_member)
        self.type(self.input_username, username)
        self.type(self.input_acctId, acct_id)
        self.type(self.input_phone, phone_number)
        self.click(self.checkbox_sendInvite)
        self.click(self.button_save)


class TestWorkWeiChat:
    def setup_class(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugger_address = "127.0.0.1:9222"
        self.dr = webdriver.Chrome(options=chrome_opts)
        self.dr.implicitly_wait(5)

    def teardown_class(self):
        self.dr.quit()

    def test_add_member(self):
        index = Index(self.dr)
        contact = index.goto_contact()
        contact.add_member("Hogwarts", "1111", "13012345678")
