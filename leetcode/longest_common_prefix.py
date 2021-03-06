# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : longest_common_prefix.py
@Time    : 2020-04-30  10:37:34
@Author  : indeyo_lin
"""
from typing import List


class LongestCommonPrefix:
    """
    14. 最长公共前缀
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。

    示例 1:
    输入: ["flower","flow","flight"]
    输出: "fl"
    示例 2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。

    说明:
    所有输入只包含小写字母 a-z 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/longest-common-prefix
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # 获取最短字符串的长度，防止越界问题
        min_str_len = min([len(x) for x in strs])

        for ch_index in range(min_str_len):
            char = strs[0][ch_index]
            for string in strs:
                if char != string[ch_index]:
                    return strs[0][:ch_index]
        return strs[0][:min_str_len]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        shortest = min(strs, key=len)
        for other in strs:
            while other.find(shortest) != 0:
                shortest = shortest[:-1]
                if shortest == "":
                    return ""
        return shortest


class LongestCommonPrefix1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        self.shortest = min(strs, key=len)
        left, right = 0, len(self.shortest) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if self.is_common_prefix(strs, mid):
                left += 1
            else:
                right -= 1

        # 无公共前缀，返回空
        if right == -1:
            return ""
        return self.shortest[:int((left + right) / 2) + 1]

    def is_common_prefix(self, strs, mid):
        for word in strs:
            if word.find(self.shortest[:mid + 1]) != 0:
                return False
        return True


if __name__ == '__main__':
    # l = [x*x for x in range(5)]
    # print(l)
    # print(max(l))

    prefix = LongestCommonPrefix()
    print(prefix.longestCommonPrefix(["aa", "aa"]))
    print(prefix.longestCommonPrefix(["flower", "flow", "flowing"]))
