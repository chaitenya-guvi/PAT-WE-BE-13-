import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f} seconds")
        return result
    return wrapper




class JQueryFilterTablePractice:

    def __init__(self):
        self.url = "https://www.w3schools.com/jquery/jquery_filters.asp"
        self.options = Options()
        # self.options.add_argument("--headless=new")
        self.options.add_argument("--incognito")
        # self.options.add_argument("--window-size=1080,720")
        self.driver = webdriver.Chrome(options=self.options)

    @timer
    def open_site(self):
        self.driver.get(self.url)
        # self.driver.maximize_window()
        time.sleep(2)

    @timer
    def filter_table(self, value):
        """Type text inside filter box and print only visible rows"""

        search_box = self.driver.find_element(By.ID, "myInput")
        search_box.clear()
        search_box.send_keys(value)

        time.sleep(2)  # wait to see filtered result

        # Locate table rows
        rows = self.driver.find_elements(By.XPATH, "//table/tbody/tr")

        print(f"\n Filter applied: '{value}'")
        print("Visible Rows:")

        for row in rows:
            if row.is_displayed():  # shows only visible rows after filtering
                print(" -", row.text)

    def close(self):
        time.sleep(2)
        self.driver.quit()



obj = JQueryFilterTablePractice()
obj.open_site()

obj.filter_table("john")
obj.filter_table("2014")
obj.filter_table("Mary")
obj.filter_table("j")

obj.close()
