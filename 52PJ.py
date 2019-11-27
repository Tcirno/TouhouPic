# -*- coding: UTF-8 -*-
# 使用爬虫实现树形循环多页面数据的收集
import requests
import chardet
from bs4 import BeautifulSoup
import codecs
import time
import random
##
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
##格式化 将中文unicode码解码回中文
url = 'https://www.52pojie.cn/forum-2-1.html'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 '
                  'Safari/537.36',  # 模拟真实用户
    # 'Connection': 'keep-alive',#存在大量TCP连接时 服务器会因资源被占用而停止接受客户端请求
    'Connection': 'close',  # 拿到网页内容后关闭连接 一击脱离
}
filename = './output/te4.html'
filename1 = './output/te4.out.html'

f = open(filename, 'w')
f.write('\n')
f.close()

url1 = url
f = open(filename, 'a')

for i in range(1, 8):
    if i == 1:
        sn = '主界面'
        continue
    elif i == 2:
        sn = '原创发布区'
    elif i == 3:
        sn = '空页面'
        continue
    elif i == 4:
        sn = '逆向资源区'
    elif i == 5:
        sn = '脱壳破解区'
    elif i == 6:
        sn = '动画发布区'
    elif i == 7:
        sn = '空页面'
        continue
    elif i == 8:
        sn = '悬赏问答区'
    else:
        continue

    print '开始爬取' + sn + '页面所有有效帖子的信息'

    for j in range(1, 200):
        url1 = 'https://www.52pojie.cn/forum-' + str(i) + '-' + str(j) + '.html'
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        print('正在爬取' + url1 + '页面上的数据')
        html = requests.get(url1, headers=header)
        html.encoding = chardet.detect(html.content)['encoding']
        text = html.text
        soup = BeautifulSoup(html.text, "html.parser")
        data = unicode(soup.select('.new>.xst'))
        if data == '[]':
            print '该页面是空页面'
            continue
        f = open(filename, 'a')
        f.write(data.decode("unicode_escape"))
        time.sleep(random.randint(1, 3))  # 这个是按照秒算的 不是毫秒 取一到四秒之间的随机数
f.close()

f = open(filename, 'r')

# 打开新文件
f_new = open(filename1, 'w')

# 循环读取旧文件
for line in f:
    # 进行判断
    if "thread" in line:
        line = line.replace('thread', '52pojie.cn/thread')
        # 如果不符合就正常的将文件中的内容读取并且输出到新文件中
        line = line.replace('<a', '\n <a')
        line = line.replace(',', ',</br>\n')
    f_new.write(line)

f.close()
f_new.close()

quit(0)
