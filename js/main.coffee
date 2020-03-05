md5 = (str1, str2) ->
  $.md5(str1 + str2)

countCode = (password, key) ->
  if !password || !key
    return
  md5one = md5 password, key
  md5two = md5 md5one, 'long'
  md5three = md5 md5one, 'chang'
  # 计算大小写
  rule = md5three.split ""
  source = md5two.split ""

  i = 0
  while (i <= 31)
    if isNaN(source[i])
      str ="longchang1990def";
      if str.search(rule[i]) > -1
        source[i] = source[i].toUpperCase()
    i++

  code32 = source.join ""
  code1 = code32.slice 0, 1
  if isNaN(code1)
    code16 = code32.slice 0, 16
  else
    code16 = "L" + code32.slice 1, 16

  console.log code16
  return code16

input_pswd = $('#pswd')
input_ident = $('#ident')
result = $('#result')
old_pswd = input_pswd.val()
old_ident = input_ident.val()
timeout_int = 0

input_pswd.on "keyup", (ev) ->
  old_pswd = this.value
  if !!timeout_int
    clearTimeout timeout_int
  timeout_int = setTimeout () ->
      result.val(countCode(old_pswd, old_ident))
    ,10

input_ident.on "keyup", (ev) ->
  old_ident = this.value
  if !!timeout_int
    clearTimeout timeout_int
  timeout_int = setTimeout () ->
      result.val(countCode(old_pswd, old_ident))
    ,10
