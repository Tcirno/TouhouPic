# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import codecs
import chardet
import re
import time
import random
import os

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 '
                  'Safari/537.36',  # 构建用户代理
    'Connection': 'close',  # 拿到网页内容后关闭连接
}


root = 'https://thwiki.cc'
# rooturl = 'https://thwiki.cc/%E6%96%87%E4%BB%B6:'
rootsaveturl = './thout/TouhouMp3/'
rooturl = 'https://thwiki.cc/文件:'
saveturl = './thout/thmid/'

#从touhouwiki上面获取所有midi音乐
for i in range(6, 9):
    if i < 10:
        saveturl = rootsaveturl + 'th0' + str(i) + '/'
    else:
        saveturl = rootsaveturl + 'th' + str(i) + '/'
    if not os.path.exists(saveturl):
        os.makedirs(saveturl)
    for j in range(1, 30):
        if j < 10:
            url = rooturl + 'th0' + str(i) + '_' + '0' + str(j) + '.mid'
            filename = 'th0' + str(i) + '_' + '0' + str(j) + '.mid'
            html = requests.get(url, headers=header)
            html.encoding = chardet.detect(html.content)['encoding']
            soup = BeautifulSoup(html.text, "html.parser")
            my = saveturl + 'th0' + str(i) + '0' + str(j) + '.html'
            data = soup.findAll(name='a', attrs={"href": re.compile(r'(\/\w{1,2}){2}\/')})
            if str(data) == '[]':
                continue
            midurl = data[0].get('href')
            print('正在写入' + filename)
            f = open(saveturl + filename, 'wb')
            f.write(requests.get(midurl).content)
            f.close()

        else:
            url = rooturl + 'th0' + str(i) + '_' + str(j) + '.mid'
            filename = 'th0' + str(i) + '_' + str(j) + '.mid'
            html = requests.get(url, headers=header)
            html.encoding = chardet.detect(html.content)['encoding']
            soup = BeautifulSoup(html.text, "html.parser")
            my = saveturl + 'th0' + str(i) + str(j) + '.html'
            data = soup.findAll(name='a', attrs={"href": re.compile(r'(\/\w{1,2}){2}\/')})
            if str(data) == '[]':
                continue
            midurl = data[0].get('href')
            print('正在写入' + filename)
            f = open(saveturl + filename, 'wb')
            f.write(requests.get(midurl).content)
            f.close()
        t = random.randint(5, 10)
        print('随机休眠' + str(t) + '秒')
        time.sleep(t)

quit(0)
