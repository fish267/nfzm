# coding: utf-8
# 爬南方周末网站的社会评论模块
# 文章信息保存到details_list中，包括标题，作者，发布时间，摘要，内容, 原地址
# 2013.10.16 
# author: fish
from bs4 import BeautifulSoup
import urllib2
import socket

url = "http://www.infzm.com/contents/8"
socket.setdefaulttimeout(6)
soup = BeautifulSoup(urllib2.urlopen(url).read())
title = soup.find_all('div', 'articleTitle')
href_list = []
for href in title:
# damn it !
	href_list.append(href.a.get('href'))
	print href.a.get('href')

#  filtering the contents of article 
details_list = []

for href in href_list:
	sub_details_list = []
	
	detail_soup = BeautifulSoup(urllib2.urlopen(href).read())

	article_title = detail_soup.find('h1', 'articleHeadline clearfix').contents[0]
	article_author = detail_soup.find('span', 'authorName').contents[0]
	article_pub_date = detail_soup.find('em', 'pubTime').contents[0].strip()[5:]
	article_abridgement = detail_soup.find_all('meta')[2].get('content')
	article_contents = detail_soup.find('section', id = 'articleContent')
	article_source_address = href

	sub_details_list.append(article_title)
	sub_details_list.append(article_author)
	sub_details_list.append(article_pub_date)
	sub_details_list.append(article_abridgement)
	sub_details_list.append(article_contents)
	sub_details_list.append(article_source_address)

	print sub_details_list

	details_list.append(sub_details_list)
# 以下是测试用的，注意转码！！
f = open('test.html', 'w')
f.write('<meta charset = "utf-8"/>')
for articles in details_list:
	for i in range(6):
		f.write(articles[i].encode('utf-8'))
		f.write('<hr><br>')	
