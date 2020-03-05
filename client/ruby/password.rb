#!/usr/bin/env ruby
#-*- coding:utf-8 -*-

require "digest/md5"


def md5(str1, str2)
  m = Digest::MD5.new
  m.update str1+str2
  m.hexdigest
end


def is_alpha(char)
    char.to_i.to_s != char
end


def count_code(password, key)
  if password != "" and key != ""
    md5_one = md5 password, key
    md5_two = md5 md5_one, 'long'
    md5_three = md5 md5_one, 'chang'

    rule = md5_three
    source = md5_two
    i = 0
    while i < 32
      if is_alpha source[i]
          const_str = "longchang1990def"
          if const_str.index(rule[i])
              source[i] = source[i].upcase
          end
      end
      i += 1
    end

    code32 = source
    code1 = code32[0]
    if is_alpha(code1)
        code16 = code32[0,16]
    else
        code16 = "L" + code32[1,16]
    end
    code16
  end
end


if caller.length == 0 then
  puts count_code("123456", "qq")
  puts count_code("123456", " ")
end
