#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from src.pages.login_page import LoginPage
from config.conf import Config
import allure

testdata = [
    ("standard_user", "wrong_password", False, "do not match"),
    ("standard_user", "secret_sauce", True, None),
    ("locked_out_user", "secret_sauce", False, "locked out"),
    ("", "secret_sauce", False, "Username is required"),
    ("standard_user", "", False, "Password is required"),
]


@allure.feature("登录功能")
@pytest.mark.parametrize("username, password, tag, error_msg", testdata)
def test_login(driver, username, password, tag, error_msg):
    """测试登录功能"""
    with allure.step("登录"):
        driver.get(Config.BASE_URL)
        page = LoginPage(driver)
        page.login(username, password)

    with allure.step("验证结果"):
        if tag:
            assert page.wait_for_url("/inventory.html", timeout=5)
        else:
            msg = page.get_error() or ""
            assert error_msg in msg
