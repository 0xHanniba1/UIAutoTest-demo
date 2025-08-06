#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from loguru import logger


class Waits:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element_present(self, locator, timeout=None):
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        logger.info(f"Element found: {locator}")
        return element
