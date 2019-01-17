import requests
import time
from pyquery import PyQuery as pq
import re
import os
import csv

csv_file = open('saledata.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["title", "review", "homepage", "discount",
                     "original_price", "publish_date", "image"])


def get_sale_games(page):
    url = 'http://store.steampowered.com/search/?specials=1&page='
    for i in range(page):
        newurl = url+str(i)
        print(newurl)
        html = requests.get(newurl).content.decode('utf-8')
        doc = pq(html)
        items = doc('#search_result_container a').items()
        for item in items:
            if item.find('.search_discount.responsive_secondrow').text():
                product = {
                    'title': item.find('.title').text(),
                    'review': item.find('.search_review_summary').attr('data-tooltip-html'),
                    'homepage': item.attr('href'),
                    'discount': item.find('.search_discount.responsive_secondrow').text(),
                    'original_price': item.find('.search_price.discounted.responsive_secondrow span').text(),
                    'publish_date': item.find('.search_released.responsive_secondrow').text(),
                    'image': item.find('img').attr('src'),
                }
                csv_writer.writerow([
                    product['title'], product['review'], product['homepage'], product['discount'], product['original_price'], product['publish_date'], product['image']])
                print(product)  # 将结果打印


if __name__ == '__main__':
    get_sale_games(5)  # 页数可以自定义
    csv_file.close()
