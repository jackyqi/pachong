#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2015-12-27
百度新闻：热搜新闻词
@author: 鑫
'''
import re
import urllib2
url = 'http://news.baidu.com/'
reg_str = r'button-slide">\s*?<a href="(.*?)".*?hotwords_li_a" title="(.*?)" mon='

request = urllib2.Request(url)
response = urllib2.urlopen(request)

pattern = re.compile(reg_str, re.S)
result = re.findall(pattern, response.read())
print len(result)
for  item in result:
    print item[0],'>>',item[1].decode('gbk') 