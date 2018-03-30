import os, sys
sys.path.append(os.getcwd())
from base.base_action import BaseAction
from selenium.webdriver.common.by import By

class NetwrokPage(BaseAction):
    # 更多
    more_button = By.XPATH, ("text", "更多")
    # 移动网络
    network_button = By.XPATH, ("text", "移动网络")
    # 首选类型
    first_network_button = By.XPATH, ("text", "首选网络类型")
    # 2g
    network_2g_button = By.XPATH, ("text", "2G")
    # 3g
    network_3g_button = By.XPATH, ("text", "3G")

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click(self.more_button)
        self.click(self.network_button)

    def click_first_network(self):
        self.click(self.first_network_button)

    def click_network_2g(self):
        self.click(self.network_2g_button)

    def click_network_3g(self):
        self.click(self.network_3g_button)