# -*- coding: UTF-8 -*-
import chardet
import requests
import os
import codecs
from bs4 import BeautifulSoup
import re
import time
import random

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 '
                  'Safari/537.36',  # 模拟真实用户
    # 'Connection': 'keep-alive',  # 存在大量TCP连接时 服务器会因资源被占用而停止接受客户端请求
    'Connection': 'close',  # 拿到网页内容后关闭连接 一击脱离
}

kw = 'pokemon'  # 在此次可以修改搜索关键词
limit = 3  # 设置图片数量-保护眼睛-后面的壁纸质量简直没法看...

root_path = r'.\imgout\\' + str(kw)
j = 1  # 全局计数器

# 构造6页循环 主界面查找循环 按照喜欢的排列
for i in range(1, 50):
    url = 'https://wallhaven.cc/search?q=' + kw + '&categories=111&purity=100&sorting=favorites&order=desc&page=' + str(
        i)
    # url参数 按热度排序 降序
    html = requests.get(url, headers=header)
    html.encoding = chardet.detect(html.content)['encoding']
    text = html.text
    soup = BeautifulSoup(html.text, "html.parser")
    data = soup.findAll(name='a', attrs={"href": re.compile(r'^https://.*(w\/).*')})
    # 首次循环 获取所有图片的链接
    if data == '[]':
        continue  # 为了省时 没有搜索的话此次循环会被直接跳过

    for sn in data:
        time.sleep(random.randint(1, 5))  # 随机延迟
        url1 = str(sn['href'])
        html1 = requests.get(url1, headers=header)
        html1.encoding = chardet.detect(html1.content)['encoding']
        text1 = html1.text
        soup1 = BeautifulSoup(html1.text, "html.parser")
        data1 = soup1.findAll(name='img', attrs={"src": re.compile(r'^https://.*jpg$')})
        # 根据之前的url构造进入二级链接的url 获取图片的详细地址
        if data1 == '[]':
            continue
        for sn1 in data1:
            url2 = sn1["src"]
            if os.path.exists(root_path + '\\'):
                os.popen('del /f ' + root_path + '\\default-avatar.jpg')
            else:
                pass
            if j == (limit + 1):
                quit(1)
            print '正在保存' + str(url2) + '页面的图片'
            j += 1
            img_name = url2.split('/')[-1]
            img_path = root_path + r'\{0}'.format(img_name)
            try:
                # 如果根目录不存在就创建该根目录
                if not os.path.exists(root_path):
                    os.makedirs(root_path)

                if not os.path.exists(img_path):

                    r = requests.get(url2)  # 获取并保存图片

                    with open(img_path, 'wb') as f:
                        f.write(r.content)
                        f.close()
                        print("文件保存成功")
                else:
                    print("文件已存在")
            except:
                print("执行出错")

quit(0)
