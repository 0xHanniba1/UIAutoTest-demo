#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.pages.inventory_page import InventoryPage
from loguru import logger
import pytest

SORT_TEST_DATA = [
    ("Name (A to Z)", "get_product_names", False),
    ("Name (Z to A)", "get_product_names", True),
    ("Price (low to high)", "get_product_prices", False),
    ("Price (high to low)", "get_product_prices", True),
]


@pytest.mark.parametrize("option, method, reverse", SORT_TEST_DATA)
def test_product_sorting(login, option, method, reverse):
    """参数化测试所有排序选项"""
    inventory = InventoryPage(login)
    inventory.select_sort_option(option)

    # 动态调用获取数据的方法
    actual = getattr(inventory, method)()
    expected = sorted(actual, reverse=reverse)
    logger.info(f"actual: 「{actual}」")

    # 断言
    assert actual == expected
