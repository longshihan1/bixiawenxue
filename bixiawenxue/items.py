# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class BixiawenxueItem(scrapy.Item):
    mongodb_id = Field()
    name = Field()#书名
    url = Field()#链接
    author=Field()#作者
    downloadurl = Field()#下载链接
    img=Field()#图像
    type = Field()#类别
    count=Field()#字数
    introduction = Field()#简介
    bookstatus = Field()#文章状态
    bookitemlist=Field()#目录地址
    authoritem=Field()#作者主页
    pass
