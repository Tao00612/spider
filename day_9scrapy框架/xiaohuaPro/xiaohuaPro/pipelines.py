# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class XiaohuaproPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123', db='spidernew',charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        title = item['title']
        try:
            sql = 'insert into xiaohuao values("%s")'
            self.cursor.execute(sql, title)
            self.conn.commit()
        except Exception:
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()