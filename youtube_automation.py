from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(options= options)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element("xpath", '//*[@id="video-title"]')
        video.click()


assist = music()
assist.play('bye')