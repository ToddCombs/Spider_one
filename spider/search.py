# author:ToddCombs
# 微信网页版已经禁止该方法登录爬取表情包，脚本已无效。
import glob
import time

import itchat
from itchat.content import TEXT, PICTURE

imgs = []

def searchImage(text):
    """搜索关键词"""
    print('收到关键词： ' , text)
    for name in glob.glob('/static/*'+text+'*.jpg'):
        imgs.append(name)

@itchat.msg_register([PICTURE, TEXT])
def text_reply(msg):
    """发送表情包"""
    searchImage(msg.text)
    for img in imgs[:6]:
        msg.user.send_image(img)
        time.sleep(0,3)
        print('开始发送表情： ', img)
    imgs.clear()

itchat.auto_login(hotReload=True)
itchat.run()