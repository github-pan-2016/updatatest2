import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.display_page import DisplayPage


class TestDisplay:
    def setup(self):
        self.driver = init_driver()
        self.display = DisplayPage(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_display(self):
        self.display.click_search()
        self.display.click_back()
        self.display.click_search()
        self.display.input_text_view("hello")
        self.display.click_back()
