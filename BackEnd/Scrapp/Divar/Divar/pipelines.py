import sys
import mysql.connector
from itemadapter import ItemAdapter
from mysql.connector import errorcode
from scrapy.exceptions import DropItem

class DivarPipeline(object):
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
            print(f"Errror connection :{e}")
            sys.exit(1)
        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS divar_tb""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS divar_tb (
                    title VARCHAR(100) NOT NULL,
                    area VARCHAR(100),
                    construction_year VARCHAR(100),
                    rooms VARCHAR(100),
                    total_price VARCHAR(100),
                    floor VARCHAR(100),
                    elevator BOOLEAN,
                    parking BOOLEAN,
                    warehouse BOOLEAN,
                    price VARCHAR(100),
                    token VARCHAR(100)
                    )
                    """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        myquery = """INSERT into DivarApp_divar 
          (
            title, 
            area, 
            construction_year,
            rooms,
            total_price,
            floor,
            elevator,
            parking,
            warehouse,
            price,
            token
          ) 
          values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
          """
        val = (
            item.get('title'),
            item.get('area'),
            item.get('construction_year'),
            item.get('rooms'),
            item.get('total_price'),
            item.get('floor'),
            item.get('elevator'),
            item.get('parking'),
            item.get('warehouse'),
            item.get('price'),
            item.get('token')
        )
        self.curr.execute(myquery, val)
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()