# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import mysql.connector
from itemadapter import ItemAdapter
from mysql.connector import errorcode
from scrapy.exceptions import DropItem
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JamaPipeline(object):
    def __init__(self):
        self.create_conn()
        self.create_table()

    def create_conn(self):
        try:
            self.conn = mysql.connector.connect(
                user='root',
                password='3425362@liAli',
                host='localhost',
                database='divar'
            )
        except mysql.Error as a:
            print(f"Errror connection :{a}")
            sys.exit(1)
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS jabama_tb""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS jabama_tb (
                     title VARCHAR(100) NOT NULL,
                     price VARCHAR(100),
                     description VARCHAR(200),
                     image_link VARCHAR(200)
                     )
                     """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        myquery = """INSERT into JabamaApp_jabama
             (
               title, 
               price,
               description,
             ) 
             values (%s,%s,%s,%s)
             """
        val = (
            item.get('title'),
            item.get('price'),
            item.get('description'),

        )
        self.curr.execute(myquery, val)
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

