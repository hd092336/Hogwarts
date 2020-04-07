from selenium import webdriver


class One:
    @classmethod
    def __init__(cls):
        cls._dr = webdriver.Chrome()


class Two(One):
    def __init__(self):
        self._dr = One()._dr

    def click(self):
        return Three()


class Three(One):
    def __init__(self):
        self._dr = One()._dr


if __name__ == "__main__":
    index = Two()
    contact = index.click()
