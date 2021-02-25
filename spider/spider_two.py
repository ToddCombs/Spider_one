# author:ToddCombs
import lxml
from bs4 import BeautifulSoup

html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.title.string)  # 获取title内容
print(soup.p.string)  # 获取P标签里的内容
print(soup.title.parent.name)  # 获取title的父级标签
print(soup.a)  # 获取超链接
print(soup.find_all('a'))  # 获取所有超链接
print(soup.find(id='link2'))  # 获取ID为link2的超链接
print(soup.get_text())  # 获取网页中的所有文本内容

print(soup.select('title'))  # 对css熟悉的，可以用select方法
print(soup.select('body a'))  # 获取网页中a标签
print(soup.select('p > #link1'))  # 获取ID为link1的p标签内容