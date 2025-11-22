"""
| Tag       | Meaning         |
| --------- | --------------- |
| `<table>` | Table container |
| `<thead>` | Header section  |
| `<tbody>` | Body section    |
| `<tr>`    | Table row       |
| `<th>`    | Header cell     |
| `<td>`    | Data cell       |


"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class W3TablePractice:

    def __init__(self):
        self.url = "https://www.w3schools.com/html/html_tables.asp"
        self.driver = webdriver.Chrome()

    def open_site(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)

    def read_table(self):
        table_xpath = "//table[@id='customers']//tr"
        rows = self.driver.find_elements(By.XPATH, table_xpath)

        print(f"Total Rows: {len(rows)}")

        for index, row in enumerate(rows):
            cols = row.find_elements(By.TAG_NAME, "td")
            cell_values = [col.text for col in cols]
            print(f"Row {index}: {cell_values}")


obj = W3TablePractice()
obj.open_site()
obj.read_table()
