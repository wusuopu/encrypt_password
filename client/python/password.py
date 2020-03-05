#!/usr/bin/env python
#-*- coding:utf-8 -*-

import hashlib


def md5(str1, str2):
    m = hashlib.md5()
    m.update(str1 + str2)
    return m.hexdigest()


def count_code(passowrd, key):
    if passowrd and key:
        md5_one = md5(passowrd, key)
        md5_two = md5(md5_one, 'long')
        md5_three = md5(md5_one, 'chang')

        rule = list(md5_three)
        source = list(md5_two)

        i = 0
        while i < 32:
            if source[i].isalpha():
                const_str = "longchang1990def"
                if const_str.find(rule[i]) > -1:
                    source[i] = source[i].upper()

            i += 1

        code32 = "".join(source)
        code1 = code32[0]
        if code1.isalpha():
            code16 = code32[:16]
        else:
            code16 = "L" + code32[1:16]
        return code16

if __name__ == '__main__':
    print(count_code('123456', 'qq'))
    print(count_code('123456', ' '))
