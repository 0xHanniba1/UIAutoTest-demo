#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class Config:
    """测试配置类"""

    BASE_URL = "https://www.saucedemo.com/"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    # 根据环境扩展
    ENVIRONMENTS = {
        'dev': "https://dev.saucedemo.com/",
        'staging': "https://staging.saucedemo.com/",
        'prod': "https://www.saucedemo.com/"
    }

    @classmethod
    def get_url(cls, env=None):
        """获取对应环境的 URL"""
        if env and env in cls.ENVIRONMENTS:
            return cls.ENVIRONMENTS[env]
        return cls.BASE_URL
