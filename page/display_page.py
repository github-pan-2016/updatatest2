import os, sys
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):

    # 显示按钮
    # display_button = By.XPATH, "//*[contains(@text,'显示')]"
    display_button = By.XPATH, ("text", "显示")

    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"

    # 文本框
    text_view = By.ID, "android:id/search_src_text"

    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click(self.display_button, time=30, poll=5)

    def click_search(self):
        self.click(self.search_button)

    def input_text_view(self, text):
        self.input_text(self.text_view, text)

    def click_back(self):
        self.click(self.back_button)