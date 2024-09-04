from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class inflow():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
    
    def get_info(self, query):
        self.query = query
        self.driver.get(url='https://www.wikipedia.org')
        search = self.driver.find_element("xpath",'//*[@id="searchInput"]')
        
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath",'//*[@id="search-form"]/fieldset/button')
        enter.click()


# assist = inflow()
# assist.get_info('hello')

