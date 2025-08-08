#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from selenium import webdriver
from src.pages.login_page import LoginPage
from config.conf import Config


@pytest.fixture
def driver():
    """全局的 driver fixture"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    """执行登录操作的 fixture"""
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(Config.USERNAME, Config.PASSWORD)
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """失败自动截图"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="失败截图",
                attachment_type=allure.attachment_type.PNG
            )
