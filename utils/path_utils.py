#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

class PathNamespace(dict):
    """字典 + 属性两种访问方式"""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(f"No such path: {name}")

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        try:
            del self[name]
        except KeyError:
            raise AttributeError(f"No such path: {name}")

def create_paths(base_file=__file__):
    """创建项目路径命名空间（项目根 = 当前文件的上一级目录）"""
    root = Path(base_file).resolve().parents[1]
    names = ['config', 'data', 'logs', 'reports', 'tests', 'src', 'utils']
    return PathNamespace({n: root / n for n in names})

paths = create_paths()

if __name__ == "__main__":
    print(paths['config'])
    print(paths.config)
