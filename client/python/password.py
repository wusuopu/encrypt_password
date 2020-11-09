#!/usr/bin/env python
#-*- coding:utf-8 -*-

import hashlib
import getpass
import sys


def ensure_bytes(value):
    if sys.version_info.major == 3:
        if isinstance(value, (str)):
           value = value.encode('utf8')
    return value


def md5(str1, str2):
    m = hashlib.md5()
    new_str = ensure_bytes(str1) + ensure_bytes(str2)
    m.update(new_str)
    return m.hexdigest()


def count_code(passowrd, key, version=1):
    if not passowrd or not key:
        return

    length = 14 if version == 2 else 16     # 新的逻辑密码长度为14

    md5_one = md5(passowrd, key)
    md5_two = md5(md5_one, 'long')
    md5_three = md5(md5_one, 'chang')

    rule = list(md5_three)
    source = list(md5_two)

    if version == 1:
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
        code16 = code32[:length]
    else:
        code16 = "L" + code32[1:length]

    if version == 2:
        # 新的逻辑，密码需要包含大写字母、小写字母、数字、特殊符号
        code16 = list(code16)
        i = 0
        flags = {'lower': False, 'num': False}
        while i < len(code16):
            if code16[i].islower() and not flags['lower']:
                # 将第1个小写字母转成大写字母
                code16[i] = code16[i].upper()
                flags['lower'] = True
            if code16[i].isdigit() and not flags['num']:
                # 将第1个数字转成特殊符号
                code16[i] = '#'
                flags['num'] = True
            if flags['lower'] and flags['num']:
                break
            i += 1
        code16 = "".join(code16)
    return code16

if __name__ == '__main__':
    pswd = getpass.getpass('passowrd:')
    if sys.version_info.major == 2:
        identify = raw_input('identify:')
    else:
        identify = input('identify:')
    version = 2 if len(sys.argv) > 1 and sys.argv[1] == '-v2' else 1
    print('result: %s' % count_code(pswd, identify, version))
