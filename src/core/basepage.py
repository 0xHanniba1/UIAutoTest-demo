#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from loguru import logger
import time


class BasePage:
    """基础页面类"""
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        """查找单个元素"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            raise NoSuchElementException(f"Element not found: {locator}")

    def find_elements(self, locator):
        """查找多个元素"""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            logger.error(f"Elements not found: {locator}")
            return []

    def click(self, locator):
        """点击元素"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        logger.info(f"Clicked element: {locator}")

    def input_text(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        logger.info(f"Input text '{text}' to element: {locator}")

    def get_text(self, locator):
        """获取元素文本"""
        element = self.find_element(locator)
        text = element.text
        logger.info(f"Got text '{text}' from element: {locator}")
        return text

    def get_attribute(self, locator, attribute):
        """获取元素属性"""
        element = self.find_element(locator)
        value = element.get_attribute(attribute)
        logger.info(f"Got attribute '{attribute}' value '{value}' from element: {locator}")
        return value

    def is_element_visible(self, locator, timeout=None):
        """检察元素是否可见"""
        timeout = timeout or self.timeout
        print(timeout)
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator):
        """检察元素是否存在"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def wait_for_element_visible(self, locator, timeout=None):
        """等待元素可见"""
        timeout = timeout or self.timeout
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=None):
        """等待元素可点击"""
        timeout = timeout or self.timeout
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        """滚动到元素"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(ture);", element)
        logger.info(f"Scrolled to element: {locator}")

    def hover_over_element(self, locator):
        """鼠标悬停"""
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        logger.info(f"Hovered over element: {locator}")

    def select_dropdown_by_text(self, locator, text):
        """通过文本选择下拉选项"""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)
        logger.info(f"Selected dropdown option '{text}' for element: {locator}")

    def select_dropdown_by_value(self, locator, value):
        """通过值选择下拉选项"""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)
        logger.info(f"Selected dropdown value '{value}' for element: {locator}")


    def navigate_to(self, url):
        """导航到页面"""
        self.driver.get(url)
        self.wait_for_page_load()
        logger.info(f"Navigated to: {url}")


    def wait_for_page_load(self, timeout=30):
       """等待页面加载完成"""
       self.wait.until(
           lambda driver: driver.execute_script("return document.readyState") == "complete"
       )
       logger.info("Page loaded completely")