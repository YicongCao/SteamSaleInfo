# -*- coding: utf-8 -*-
import os
import csv
import json
import sqlite3

QUERY_BY_PROP = '''
select name, discount, oriprice, curprice, pos, pop, date, url, img
from games order by {prop} {order} limit 3
'''

# {
#     "msgtype": "news",
#     "chatid": "wrkSFfCgAALFgnrSsWU38puiv4yvExuw",
#     "news": {
#         "articles": [
#             {
#                "title": "中秋节礼品领取",
#                "description": "今年中秋节公司有豪礼相送",
#                "url": "URL",
#                "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
#             }
#         ]
#     }
# }


def do_query(filterstr):
    conn = sqlite3.connect('salesqlite.db')
    cursor = conn.cursor()
    articles = []
    if filterstr == 'price':
        # 最大折扣
        query = {'prop': 'discount', 'order': 'desc'}
        cursor.execute(QUERY_BY_PROP.format(**query))
        result = cursor.fetchall()
        if len(result) > 0:
            title = "[最折扣] " + result[0][0]
            desc = ""
            for game in result:
                desc += "{0},降价{1},折后{2}元\r\n".format(
                    game[0], game[1], game[3])
            article = {'title': title, 'description': desc,
                       'url': result[0][7], 'picurl': result[0][8]}
            articles.append(article)
    if filterstr == 'pop':
        # 最高人气
        query = {'prop': 'pop', 'order': 'desc'}
        cursor.execute(QUERY_BY_PROP.format(**query))
        result = cursor.fetchall()
        if len(result) > 0:
            title = "[最人气] " + result[0][0]
            desc = ""
            for game in result:
                desc += "{0},热度{1},折后{2}元\r\n".format(
                    game[0], game[5], game[3])
            article = {'title': title, 'description': desc,
                       'url': result[0][7], 'picurl': result[0][8]}
            articles.append(article)
    if filterstr == 'pos':
        # 最高评价
        query = {'prop': 'pos', 'order': 'desc'}
        cursor.execute(QUERY_BY_PROP.format(**query))
        result = cursor.fetchall()
        if len(result) > 0:
            title = "[最好评] " + result[0][0]
            desc = ""
            for game in result:
                desc += "{0},好评率{1}%,折后{2}元\r\n".format(
                    game[0], game[4], game[3])
            article = {'title': title, 'description': desc,
                       'url': result[0][7], 'picurl': result[0][8]}
            articles.append(article)

    cursor.close()
    conn.commit()
    # 准备信息
    data = {}
    data['msgtype'] = 'news'
    data['news'] = {}
    data['news']['articles'] = articles
    pushdata = json.dumps(data)
    print(pushdata)
    return data


if __name__ == '__main__':
    do_query('pop')
