#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.pages.inventory_page import InventoryPage
from loguru import logger
import pytest
import allure

SORT_TEST_DATA = [
    ("Name (A to Z)", "get_product_names", False),
    ("Name (Z to A)", "get_product_names", True),
    ("Price (low to high)", "get_product_prices", False),
    ("Price (high to low)", "get_product_prices", True),
]


@allure.feature("产品排序功能")
@allure.story("产品排序测试")
@pytest.mark.parametrize("option, method, reverse", SORT_TEST_DATA)
def test_product_sorting(login, option, method, reverse):
    """参数化测试所有排序选项"""
    with allure.step(f"创建库存页面并选择排序选项: 「{option}」"):
        inventory = InventoryPage(login)
        inventory.select_sort_option(option)

    with allure.step("获取页面数据"):
        # 动态调用获取数据的方法
        actual = getattr(inventory, method)()
        expected = sorted(actual, reverse=reverse)

    with allure.step("记录测试数据"):
        logger.info(f"排序选项: 「{option}」")
        logger.info(f"实际数据: 「{actual}」")
        logger.info(f"预期数据: 「{expected}」")

        # 添加到 allure 报告中
        allure.attach(str(actual), "实际获取的数据", allure.attachment_type.TEXT)
        allure.attach(str(expected), "预期获取的数据", allure.attachment_type.TEXT)

    # 断言
    assert actual == expected
