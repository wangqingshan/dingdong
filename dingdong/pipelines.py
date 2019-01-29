# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import urllib


class DingdongPipeline(object):
    def __init__(self):
        #在初始化方法中打开文件
        self.fileName = open("dingdong.json","wb")

    def process_item(self, item, spider):
        #把数据转换为字典再转换成json
        text = json.dumps(dict(item),ensure_ascii=False)+"\n"
        #写到文件中编码设置为utf-8
        self.fileName.write(text.encode("utf-8"))

        #这里进行图片处理
        imgurl=item['imgurl']
        # 截图图片链接
        list_name = imgurl.split('/')
        # 获取图片名称
        file_name = list_name[len(list_name) - 1]  # 图片名称
        currentPath = "E:/resource"
        if not os.path.exists(currentPath):
            os.makedirs(currentPath)

        #定义图片路径
        path_name = os.path.join(currentPath,file_name)
        print("https:"+imgurl)
        # 图片保存
        with open(path_name, 'wb') as file_writer:
            conn = urllib.request.urlopen("https:"+imgurl)  # 下载图片
            # 保存图片
            file_writer.write(conn.read())
        file_writer.close()
        # 图片处理结束
        #返回item
        return item

    def close_spider(self,spider):
        #关闭时关闭文件
        self.fileName.close()
