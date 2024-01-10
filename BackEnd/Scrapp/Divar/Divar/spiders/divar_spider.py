import time
import scrapy
import json
import pandas as pd
from scrapy.crawler import CrawlerProcess
from unidecode import unidecode

url = 'https://api.divar.ir/v8/posts-v2/web/{token}'


class DivarSpider(scrapy.Spider):
    name = 'divar'

    def __init__(self, *args, **kwargs):
        super(DivarSpider, self).__init__(*args, **kwargs)

        # Read the token file and define start_urls
        self.token_df = pd.read_csv('tokens.csv', encoding='utf-8')
        self.start_urls = [url.format(token=token) for token in self.token_df['token']]

    def parse(self, response, **kwargs):
        try:
            decoded_data = response.text.encode().decode('utf-8')
            data = json.loads(decoded_data)

            section = next(section for section in data['sections'] if section['section_name'] == 'LIST_DATA')

            widgets = section['widgets']
            items = widgets[0]['data']['items']

            area = unidecode(items[0]['value'])
            construction_year = unidecode(items[1]['value'])
            rooms = unidecode(items[2]['value'])

            total_price = unidecode(widgets[1]['data']['value'])

            floor = widgets[4]['data']['value']
            if 'از' in floor:
                seg = floor.split()
                floor = unidecode(seg[0])
            elif 'همکف' in floor:
                floor = 0
            else:
                floor = unidecode(floor)

            facilities = widgets[6]['data']['items']

            elevator = False if 'ندارد' in facilities[0]['title'] else True
            parking = False if 'ندارد' in facilities[1]['title'] else True
            warehouse = False if 'ندارد' in facilities[2]['title'] else True

            title = data['share']['title']

            price = data['webengage']['price']
            token = data['webengage']['token']

            yield {
                'title': title,
                'area': area,
                'construction_year': construction_year,
                'rooms': rooms,
                'total_price': total_price,
                'floor': floor,
                'elevator': elevator,
                'parking': parking,
                'warehouse': warehouse,
                'price': price,
                'token': token
            }
            time.sleep(0.5)
        except Exception as e:
            self.logger.error(f"Error in parsing: {e}")



if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "infos.csv": {"format": "csv", 'encoding': 'utf8', 'jl': 'divar.error.Web'},
        }
    })
    process.crawl(DivarSpider)
    process.start()

    infos_df = pd.read_csv('infos.csv')
    final_output = infos_df.merge(right=token_df, how='left', on='token')
    final_output.to_csv('final_output.csv', encoding='utf-8')
