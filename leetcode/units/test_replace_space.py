# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : test_replace_space.py
@Time    : 2020-04-26  21:38:59
@Author  : indeyo_lin
"""
import pytest

from leetcode.replace_space import ReplaceSpace


class TestReplaceSpace:
    def setup(self):
        self.s = ReplaceSpace()

    @pytest.mark.parametrize("s", [
        "hello world",
        "We are happy.",
        "love&peace"
    ])
    def test_success(self, s):
        print(self.s.replaceSpace(s))

    @pytest.mark.parametrize("s", [
        " ",
        "",
        "   ",
        "1234 222"
    ])
    def test_fail(self, s):
        print(self.s.replaceSpace(s))