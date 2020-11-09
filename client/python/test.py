#!/usr/bin/env python
# encoding: utf-8

import unittest
import password


class PasswordTest(unittest.TestCase):
    def test_v1(self):
        """v1版本的逻辑"""
        assert password.count_code('123456', 'qq') == 'd77206DAB902407a'
        assert password.count_code('123456', '163') == 'L8711c4ee781eFCD'

    def test_v2(self):
        """v2版本的逻辑"""
        assert password.count_code('123456', 'qq', 2) == 'D#7206dab90240'
        assert password.count_code('123456', '163', 2) == 'L#711C4ee781ef'

if __name__ == '__main__':
    unittest.main()
