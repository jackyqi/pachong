#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2015-12-27
百度新闻的所有链接
@author: 鑫
'''
import re
import urllib2
url = 'http://news.baidu.com/'
reg_str = r'<a href="(.*?)".*?target="_blank" .*?>(.*?)\s*</a>'

request = urllib2.Request(url)
response = urllib2.urlopen(request)

pattern = re.compile(reg_str, re.S)
result = re.findall(pattern, response.read())

f1 = open('e:/a1.txt','w')
print len(result)
for item in result:
    f1.write( item[1]+'\n')
    
f1.close()
# print str(result).decode('utf8')


    