#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from src.core.base_page import BasePage


class InventoryPage(BasePage):
    """产品列表页面"""

    # 定位器
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ACTIVE_OPTION = (By.CSS_SELECTOR, ".product_sort_container option:checked")

    def select_sort_option(self, option_text):
        """选择排序选项"""
        self.select_dropdown_by_text(self.SORT_DROPDOWN, option_text)

    def get_product_names(self):
        """获取所有产品名称列表"""
        elements = self.find_elements(self.PRODUCT_NAME)
        return [elem.text for elem in elements]

    def get_product_prices(self):
        """获取所有产品价格列表"""
        elements = self.find_elements(self.PRODUCT_PRICE)
        # 移除$符号并转换为浮点数
        return [float(elem.text.replace('$', '')) for elem in elements]



# from selenium import webdriver
# from src.pages.login_page import LoginPage
# from config.conf import Config
# driver = webdriver.Chrome()
# driver.get(Config.BASE_URL)
# login = LoginPage(driver)
# login.login("standard_user", "secret_sauce")
# a = InventoryPage(driver)
# print(a.get_product_prices())
#
# driver.quit()
