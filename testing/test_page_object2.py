from selenium import webdriver


class One:
    def __init__(self):
        if not hasattr(One, 'dr'):
            One.dr = webdriver.Chrome()

    def quit(self):
        self.dr.quit()
        delattr(One, 'dr')


class Two(One):
    def click(self):
        return Three()


class Three(One):
    pass


if __name__ == "__main__":
    index = Two()
    contact = index.click()
    contact.click()
    contact.quit()
    print("Case 1 is done.")
    index2 = Two()
    print('yes')
    index2.click()
    index2.quit()
