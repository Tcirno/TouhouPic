# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import codecs
import chardet
import re
import time
import random
import os

# import sys
#
# reload(sys)
# sys.setdefaultencoding("utf-8")

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 '
                  'Safari/537.36',  # 构建用户代理
    'Connection': 'close',  # 拿到网页内容后关闭连接
}

root = 'https://thwiki.cc'
# root_url = 'https://thwiki.cc/%E6%96%87%E4%BB%B6:'
root_url = 'https://thwiki.cc/文件:'
root_save_url = './thout/TouhouMp3/'
save_url = './thout/TouhouMp3/'
th_name = ''

# 从touhouwiki上面获取所有mp3音乐
for i in range(6, 18):
    if i < 10:
        save_url = root_save_url + 'th0' + str(i) + '/'
        th_name = 'th0'
    else:
        save_url = root_save_url + 'th' + str(i) + '/'
        th_name = 'th'
    if not os.path.exists(save_url):
        os.makedirs(save_url)
    else:
        continue
    for j in range(1, 30):
        if j < 10:
            url = root_url + th_name + str(i) + '_' + '0' + str(j) + '.mp3'
            filename = th_name + str(i) + '_' + '0' + str(j) + '.mp3'
            html = requests.get(url, headers=header)
            html.encoding = chardet.detect(html.content)['encoding']
            soup = BeautifulSoup(html.text, "html.parser")
            my = save_url + th_name + str(i) + '0' + str(j) + '.html'
            data = soup.findAll(name='a', attrs={"href": re.compile(r'(/\w{1,2}){2}/')})
            if str(data) == '[]':
                continue
            mp3url = data[0].get('href')
            print('正在写入' + filename)
            f = open(save_url + filename, 'wb')
            f.write(requests.get(mp3url).content)
            f.close()

        else:
            url = root_url + th_name + str(i) + '_' + str(j) + '.mp3'
            filename = th_name + str(i) + '_' + str(j) + '.mp3'
            html = requests.get(url, headers=header)
            html.encoding = chardet.detect(html.content)['encoding']
            soup = BeautifulSoup(html.text, "html.parser")
            my = save_url + th_name + str(i) + str(j) + '.html'
            data = soup.findAll(name='a', attrs={"href": re.compile(r'(/\w{1,2}){2}/')})
            if str(data) == '[]':
                continue
            mp3url = data[0].get('href')
            print('正在写入' + filename)
            f = open(save_url + filename, 'wb')
            f.write(requests.get(mp3url).content)
            f.close()
        t = random.randint(2, 5)
        print('随机休眠' + str(t) + '秒')
        time.sleep(t)

quit(0)
