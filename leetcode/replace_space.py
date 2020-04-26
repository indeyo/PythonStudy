# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : PythonStudy
@File    : replace_space.py
@Time    : 2020-04-26  14:47:16
@Author  : indeyo_lin
"""


class ReplaceSpace:
    """
        面试题05. 替换空格
        请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

        示例 1：
        输入：s = "We are happy."
        输出："We%20are%20happy."

        限制：0 <= s 的长度 <= 10000
    """

    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 转换成列表，方便对每个字符进行操作
        array = list(s)
        # python里面数组的赋值操作，实际上相当于引用，而没有开辟一个新的存储空间
        # 如果不copy，直接赋值，那么对array_new进行修改会影响到array
        array_new = array.copy()
        p_head, p_tail = 0, len(array) - 1
        p_search = 0

        for i in array:
            if i == ' ':
                array_new[p_head+3:p_tail+3] = array[p_search+1:len(array)+1]
                array_new[p_head:p_head+3] = "%20"
                p_head += 3
                p_tail += 3
                p_search += 1
                continue
            p_head += 1
            p_search += 1
        return "".join(array_new)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = ['l', 'o', 'v', 'e']
    #
    # print(a[:-5:2])
    # a[1:3] = [9, 9]
    # print(a)
    # b[2:4] = "abc"
    # print(b)
    #
    # for i in range(5):
    #     print(i)
    # print(a.index(3))

    s = ReplaceSpace()
    print(s.replaceSpace("hello world arthinking"))

    # a = []
    # q = queue.Queue()
    # q.put(a)
    # q.put(0)
    # # print(q.get())
    # print(q.get())