#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
