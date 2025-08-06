#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from src.pages.login_page import LoginPage
from config.conf import Config


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


testdata = [
    ("standard_user", "wrong_password", False, "do not match"),
    ("standard_user", "secret_sauce", True, None)

]


@pytest.mark.parametrize("username, password, tag, error_msg", testdata)
def test_login(driver, username, password, tag, error_msg):
    driver.get(Config.BASE_URL)
    page = LoginPage(driver)
    page.login(username, password)
    if tag:
        assert page.wait_for_url("/inventory.html", timeout=5)
    else:
        msg = page.get_error() or ""
        assert error_msg in msg
