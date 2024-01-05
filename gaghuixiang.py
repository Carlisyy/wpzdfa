import requests
import re
import time
import random
import hashlib
from translate import Translator
import json
import pymysql
import time
import re
import random
import hashlib
import urllib.parse
from bs4 import BeautifulSoup
import lxml


def t_release(title,link_match,extraction_code_match):
    article_content = """
文章内容
    """
    url = 'https://www.goodszy.xyz/Locoy.php?action=save'
    article_dict = {
        'post_title': title,  # 必选  标题
        'post_content': title+'[rihide]'+link_match+extraction_code_match+'[/rihide]',  # 必选  内容
        'tag': '',  # 可选  标签
        'post_category': 1,  # 可选 分类
        'post_date': '',  # 可选  时间
        'post_excerpt': '',  # 可选  摘要
        'post_author': 'admin',  # 可选  作者
        'category_description': '',  # 可选  分类信息
        'post_cate_meta[name]': '',  # 可选 自定义分类信息
        'post_meta[name]': '',  # 可选  自定义字段
        'post_type': 'post',  # 可选    文章类型  默认为'post', page
        'post_taxonomy': '',  # 可选   自定义分类方式
        'post_format': '',  # 可选    文章形式

    }
    try:
        r = requests.post(url, data=article_dict, timeout=10)
    except requests.Timeout:
        print('发布超时！！！')
    except requests.RequestException as e:
        print('发布出错：', e)
    r.encoding = 'utf-8'
    print('发布结果', r.text)



def urls(id):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'cookie': 'PHPSESSID=am8i9fd0blgtrhvovprp4cdtuq; Hm_lvt_c0218990958cc58e9c1e26f1d6c03369=1701261800,1701706860,1701938464,1703055153; cao_notice_cookie=1; Hm_lpvt_c0218990958cc58e9c1e26f1d6c03369=1703055165; wordpress_logged_in_1b2e26e5ee015c2c1a730f0d65d7cb39=criysb%7C1703228033%7CtP1C1fkQtH4X9g1jHDt9SeZHdQlMfwanvu5re0mY6WY%7C76fc51659d2ba4c8698082017178306632312d7aee7047dad4108d0d0d925fad',

    }

    url = 'https://www.gagahuixiang.com/{}/'.format(id)
    response = requests.get(url, headers=headers).content.decode('utf-8')


    # print(content_hide_tips_text) https://pan.baidu.com/s/(\w+)(\?pwd=(\w+))?
    try:
        jiexi = BeautifulSoup(response, 'lxml')
        title = jiexi.select('.entry-title')[0].text
        print(title)
        entry_content_div = jiexi.find('div', class_='entry-content u-text-format u-clearfix')

        # 提取 img 标签
        img_tags = entry_content_div.find_all('img')

        # 提取文本内容
        text_content = entry_content_div.get_text()

        # 提取 class 为 "content-hide-tips" 的内容
        content_hide_tips = entry_content_div.find('div', class_='content-hide-tips')
        if content_hide_tips:
            content_hide_tips_text = content_hide_tips.get_text()
        else:
            content_hide_tips_text = ""
        link_pattern = re.compile(r'(https://pan\.baidu\.com/s/[a-zA-Z0-9-_]+)(\?pwd=(\w+))?')
        extraction_code_pattern = re.compile(r'提取码：([a-zA-Z0-9]+)')
        link_match = link_pattern.search(content_hide_tips_text).group()
        extraction_code_match = extraction_code_pattern.search(content_hide_tips_text).group()
        print(link_match)
        print(extraction_code_match)
        t_release(title,link_match,extraction_code_match)
    except Exception as e:
        return None

#3400 -20295
for i in range(19556,20296,1):
    urls(i)