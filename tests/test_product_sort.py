#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.pages.inventory_page import InventoryPage
from loguru import logger


class TestProductSort:
    """产品排序功能测试"""

    def test_sort_by_name_ascending(self, login):
        """测试按名称升序排序"""
        inventory = InventoryPage(login)
        inventory.select_sort_option("Name (A to Z)")

        names = inventory.get_product_names()
        logger.info(f"product names: 「{names}」")
        assert names == sorted(names)

    def test_sort_by_name_descending(self, login):
        """测试按名称倒序排序"""
        inventory = InventoryPage(login)
        inventory.select_sort_option("Name (Z to A)")

        names = inventory.get_product_names()
        logger.info(f"product names: 「{names}」")
        assert names == sorted(names, reverse=True)

    def test_sort_by_price_low_to_high(self, login):
        """测试按价格从低到高排序"""
        inventory = InventoryPage(login)
        inventory.select_sort_option("Price (low to high)")

        prices = inventory.get_product_prices()
        logger.info(f"product prices: 「{prices}」")
        assert prices == sorted(prices)

    def test_sort_by_price_high_to_low(self, login):
        """测试按价格从高到低排序"""
        inventory = InventoryPage(login)
        inventory.select_sort_option("Price (high to low)")

        prices = inventory.get_product_prices()
        logger.info(f"product prices: 「{prices}」")
        assert prices == sorted(prices, reverse=True)