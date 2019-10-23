# -*- coding: UTF-8 -*-

from urllib import unquote
import requests
from bs4 import BeautifulSoup
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
rooturl1 = 'https://thwiki.cc/东方求闻史纪'
rooturl2 = 'https://thwiki.cc/东方求闻口授'
saveturl = './thout/ThouhouImage'
# 求闻史纪部分
html = requests.get(rooturl1, headers=header)
html.encoding = chardet.detect(html.content)['encoding']
soup = BeautifulSoup(html.text, "html.parser")

data = soup.findAll(name='a', attrs={"href": re.compile(r'\/(\%\w{2})+\/(\%\w{2})+')})
# 获取子网页链接

for k in data:
    pichtml = requests.get(root + k.get('href'), headers=header)

    pichtml.encoding = chardet.detect(pichtml.content)['encoding']
    souphtml = BeautifulSoup(pichtml.text, "html.parser")
    datahtml = souphtml.findAll(name='img', attrs={"src": re.compile(r'c(/\w{1,2}){2}/(%\w{2})+.jpg')})
    # 简化正则 东方求闻史纪用的是jpg格式的文件

    if str(datahtml) == '[]':
        datahtmlset = souphtml.findAll(name='img', attrs={"srcset": re.compile(r'c(/\w{1,2}){2}/(%\w{2})+.jpg')})
        if str(datahtmlset) == '[]':
            continue
        else:
            time.sleep(random.randint(0, 2))
            # 随机休眠 模拟真实用户
            for i in datahtmlset:
                picurl = i.get('srcset')
                picurl = picurl.split(' ')[-2]
                # 构建url 取倒数第二个
                img_name = picurl.split('/')[-1]
                img_name = unquote(str(img_name.split('.')[-2])) + '.' + str(img_name.split('.')[-1])
                # url格式化回中文
                img_path = (saveturl + '/' + str(img_name)).decode('utf-8')
                try:
                    # 如果根目录不存在就创建该根目录
                    if not os.path.exists(saveturl):
                        os.makedirs(saveturl)

                    if not os.path.exists(img_path):

                        r = requests.get(picurl)  # 获取并保存图片

                        with open(img_path, 'wb') as f:
                            f.write(r.content)
                            f.close()
                            print("文件保存成功")
                    else:
                        print("文件已存在")
                        continue
                except:
                    print("执行出错")

    else:
        time.sleep(random.randint(0, 2))
        # print datahtml
        for i in datahtml:
            picurl = i.get('src')
            img_name = picurl.split('/')[-1]
            img_name = unquote(str(img_name.split('.')[-2])) + '.' + str(img_name.split('.')[-1])
            # url格式化回中文
            img_path = (saveturl + '/' + str(img_name)).decode('utf-8')
            try:
                # 如果根目录不存在就创建该根目录
                if not os.path.exists(saveturl):
                    os.makedirs(saveturl)

                if not os.path.exists(img_path):

                    r = requests.get(picurl)  # 获取并保存图片

                    with open(img_path, 'wb') as f:
                        f.write(r.content)
                        f.close()
                        print("文件保存成功")
                else:
                    print("文件已存在")
                    continue
            except:
                print("执行出错")

# 求闻口授部分

html = requests.get(rooturl2, headers=header)
html.encoding = chardet.detect(html.content)['encoding']
soup = BeautifulSoup(html.text, "html.parser")

data = soup.findAll(name='a', attrs={"href": re.compile(r'\/(\%\w{2})+\/(\%\w{2})+')})

for k in data:
    pichtml = requests.get(root + k.get('href'), headers=header)
    pichtml.encoding = chardet.detect(pichtml.content)['encoding']
    souphtml = BeautifulSoup(pichtml.text, "html.parser")
    datahtml = souphtml.findAll(name='img', attrs={"src": re.compile(r'c(/\w{1,2}){2}/(%\w{2})+.png')})  # 简化正则
    # 求闻口授用的是png的图片文件
    if str(datahtml) == '[]':
        datahtmlset = souphtml.findAll(name='img', attrs={"srcset": re.compile(r'c(/\w{1,2}){2}/(%\w{2})+.png')})
        if str(datahtmlset) == '[]':
            continue
        else:
            time.sleep(random.randint(0, 2))
            for i in datahtmlset:
                picurl = i.get('srcset')
                picurl = picurl.split(' ')[-2]
                img_name = picurl.split('/')[-1]
                img_name = unquote(str(img_name.split('.')[-2])) + '.' + str(img_name.split('.')[-1])
                # url格式化回中文
                img_path = (saveturl + '/' + str(img_name)).decode('utf-8')
                try:
                    # 如果根目录不存在就创建该根目录
                    if not os.path.exists(saveturl):
                        os.makedirs(saveturl)

                    if not os.path.exists(img_path):

                        r = requests.get(picurl)  # 获取并保存图片

                        with open(img_path, 'wb') as f:
                            f.write(r.content)
                            f.close()
                            print("文件保存成功")
                    else:
                        print("文件已存在")
                        continue
                except:
                    print("执行出错")

    else:
        time.sleep(random.randint(0, 2))
        for i in datahtml:
            picurl = i.get('src')
            img_name = picurl.split('/')[-1]
            img_name = unquote(str(img_name.split('.')[-2])) + '.' + str(img_name.split('.')[-1])
            # url格式化回中文
            img_path = (saveturl + '/' + str(img_name)).decode('utf-8')
            try:
                # 如果根目录不存在就创建该根目录
                if not os.path.exists(saveturl):
                    os.makedirs(saveturl)

                if not os.path.exists(img_path):

                    r = requests.get(picurl)  # 获取并保存图片

                    with open(img_path, 'wb') as f:
                        f.write(r.content)
                        f.close()
                        print("文件保存成功")
                else:
                    print("文件已存在")
                    continue
            except:
                print("执行出错")

quit(0)
