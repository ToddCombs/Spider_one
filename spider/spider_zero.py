# author:ToddCombs
import requests
import json
import re


# r = requests.get('https://api.github.com/events')  # 基础的不带参数的get请求，获取资源
rp = requests.get(url='https://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的get请求，获取资源
# p = requests.post('https://httpbin.org/post', data={'key': 'value'})  # 向浏览器邮寄一些封装的数据包获取资源
# u = requests.put('https://httpbin.org/put', data={'key': 'value'})  # 向服务器上传资源
# d = requests.delete('https://httpbin.org/delete')  # 向服务器请求删除指定url的资源
# h = requests.head('https://httpbin.org/get')  # 与get请求类似，单不返回消息体。主要用于检查资源的有效性，检查链接有效性，检查网页是否被篡改
# o = requests.options('https://httpbin.org/get')  # 允许客户端查看服务器的性能。

# payload = {'key1': 'value1', 'key2': 'value2'}
# pr = requests.get('https://httpbin.org/get', params=payload)
#
#
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# urlr = requests.get(url, headers=headers)

# print(rp.status_code)  获取响应码
# print(rp.text)  # 输出获取的文本
# print(rp.encoding)  # 将获取的内容编码成可阅读文字
# print(rp.headers)  # 获取响应头

# 正则表达式	描述
# \d	代表任意数字，就是阿拉伯数字 0-9 这些玩意。
# \D	大写的就是和小写的唱反调，\d 你代表的是任意数字是吧？那么我 \D 就代表不是数字的。
# \w	代表字母，数字，下划线。也就是 a-z、A-Z、0-9、_。
# \W	跟 \w 唱反调，代表不是字母，不是数字，不是下划线的。
# \n	代表一个换行。
# \r	代表一个回车。
# \f	代表换页。
# \t	代表一个 Tab 。
# \s	代表所有的空白字符，也就是上面这个：\n、\r、\t、\f。
# \S
# 跟 \s 唱反调，代表所有不是空白的字符。
#
# \A	代表字符串的开始。
# \Z	代表字符串的结束。
# ^	匹配字符串开始的位置。
# $	匹配字符创结束的位置。
# .	代表所有的单个字符，除了 \n \r
# [...]	代表在 [] 范围内的字符，比如 [a-z] 就代表 a到z的字母
# [^...]	跟 [...] 唱反调，代表不在 [] 范围内的字符
# {n}
# 匹配在 {n} 前面的东西，比如: o{2} 不能匹配 Bob 中的 o ，但是能匹配 food 中的两个o。
# {n,m}	匹配在 {n,m} 前面的东西，比如：o{1,3} 将匹配“fooooood”中的前三个o。
# {n，}	匹配在 {n,} 前面的东西，比如：o{2,} 不能匹配“Bob”中的“o”，但能匹配“foooood”中的所有o。
# *	和 {0,} 一个样，匹配 * 前面的 0 次或多次。 比如 zo* 能匹配“z”、“zo”以及“zoo”。
# +	和{1，} 一个样，匹配 + 前面 1 次或多次。 比如 zo+”能匹配“zo”以及“zoo”，但不能匹配“z”。
# ？	和{0,1} 一个样，匹配 ？前面 0 次或 1 次。
# a|b	匹配 a 或者 b。
# （）	匹配括号里面的内容。
#  正则表达式，用.*?匹配下面数据里的数字100
content = 'Toddcombs has 100 bananas'
res = re.match('^To.*?(\d+)\s.*s$', content)
# .*? 这个组合代表非贪婪匹配，直接把数字100匹配出来, .*表示贪婪匹配，尽可能多的匹配数据
print(res.group(1))

#  正则表达式匹配换行的数据，re.S
content_one = """Toddcombs has 200
              bananas"""
res_one = re.match('^To.*?(\d+)\s.*s$', content_one, re.S)
print(res_one.group(1))

#  re.search直接扫描字符串，把匹配成功的第一个结果返回给用户
content_two = """Toddcombs has 300
              bananas"""
res_two = re.search('To.*?(\d+)\s.*s', content_two, re.S)
print(res_two.group(1))

# 用正则表达式匹配所有数字，以列表形式返回，使用re.findall
content_three = """Toddcombs has 400 bananas;
Toddcombs has 400 bananas;
Toddcombs has 400 bananas;
Toddcombs has 400 bananas;"""
res_three = re.findall('To.*?(\d+)\s.*?s;', content_three, re.S)
print(res_three)

# 正则表达式匹配所有数字并替换为500，使用re.sub
content_four = """Toddcombs has 400 bananas;
Toddcombs has 400 bananas;
Toddcombs has 400 bananas;
Toddcombs has 400 bananas;"""
res_four = re.sub('\d+', '500', content_four)
print(res_four)

# re.compile封装匹配符
content_five = 'Toddcombs has 10 bananas'
pattern = re.compile('To.*?(\d+)\s.*s', re.S)
res_five = re.match(pattern, content_five)
print(res_five.group(1))