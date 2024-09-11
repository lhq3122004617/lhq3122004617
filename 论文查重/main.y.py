import pandas as pd
import jieba#用于中文的分词
import numpy as np#用于方便进行计算
import string
import sys

import unittest


def add_numb(a, b):
    return a + b


def division_numb(a, b):
    return a / b


class Test(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(add_numb(1, 1), 2)

    def test_add_2(self):
        self.assertEqual(add_numb(2, 0), 1)

    def test_division_1(self):
        self.assertEqual(division_numb(2, 1), 2)

    def test_division_2(self):
        self.assertEqual(division_numb(2, 0), 2)


if __name__ == "__main__":
    main()