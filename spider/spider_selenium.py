# author:ToddCombs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# find_element_by_id    获取form表单
# find_element_by_name  获取相应的输入框
# find_element_by_xpath 获取表单
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name  获取相应的输入框
# find_element_by_class_name    获取相应的元素
# find_element_by_css_selector

# 无头模式
# options = Options()
# options.add_argument('-headless') # 无头参数
# d = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
d = webdriver.Chrome()
d.get('https://www.baidu.com')

input = d.find_element_by_css_selector('#kw')
input.send_keys('小泽玛利亚照片')

button = d.find_element_by_css_selector('#su')
button.click()

d.current_url  # 获取请求链接
d.get_cookies()  # 获取cookies
d.page_source  # 获取页面源代码
input.text  # 获取文本的值

