# coding: utf-8
# 爬huxiu
# 文章信息保存到details_list中，包括标题，作者，发布时间，摘要，内容, 原地址
# 2013.10.16 
# author: fish
from bs4 import BeautifulSoup
import urllib2

url = "http://www.huxiu.com"
soup = BeautifulSoup(urllib2.urlopen(url).read())
href_list = []
title = soup.find_all('div', 'article-box-ctt')
for detail_href in title:
	try:
		href_list.append('http://www.huxiu.com/' + detail_href.h4.a.get('href'))
	except:
		AttributeError
details_list = []

for href in href_list:
	sub_details_list = []
	
	detail_soup = BeautifulSoup(urllib2.urlopen(href).read())

	article_title = detail_soup.title.string
	article_author = detail_soup.find('span', 'recommenders').a.contents[0]
	article_pub_date = detail_soup.find('time').string
	article_abridgement = detail_soup.find_all('meta')[3].get('content')
	article_contents = detail_soup.find('div', 'neirong-box')

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
