# -*- coding: utf-8 -*-
import os
import csv
import json
import sqlite3

CLEAR_TABLE = '''
drop table if exists games;
'''

CREATE_TABLE = '''
create table games
(
    name varchar(255) default 'noname',
    discount varchar(255) default 'nodiscount',
    oriprice int default -1,
    curprice int default -1,
    pos int default -1,
    pop int default -1,
    date varchar(255) default '1 Jan, 1970',
    url varchar(255) default 'nohomepage',
    img varchar(255) default 'noimg'
);
'''

INSERT_DATA = '''
insert into games (name, discount, oriprice, curprice, pos, pop, date, url, img)
values ("{name}", "{discount}", "{oriprice}", "{curprice}",
        "{pos}", "{pop}", "{date}", "{url}", "{img}")
'''

QUERY_BY_NAME = '''
select *
from games where name LIKE "%{name}%" or nickname LIKE "%{name}%" order by pop desc
'''


def do_convert():
    conn = sqlite3.connect('salesqlite.db')
    cursor = conn.cursor()
    cursor.execute(CLEAR_TABLE)
    cursor.execute(CREATE_TABLE)
    gameset = set()
    with open('saledata.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            if line['title'] in gameset:
                continue
            columns = {}
            columns['name'] = line['title']
            columns['url'] = line['homepage']
            columns['discount'] = line['discount']
            oriprice = line['original_price'].replace(
                ",", "")
            oriprice = oriprice.replace("¥", "").replace(" ", "")
            discount = line['discount'].replace("-", "").replace("%", "")
            discount = float(discount)
            curprice = float(oriprice) * (100 - discount) / 100
            columns['curprice'] = int(curprice)
            columns['oriprice'] = int(oriprice)
            columns['date'] = line['publish_date']
            columns['img'] = line['image']
            review = str(line['review'])
            if (review.find("<br>") != -1):
                columns['pos'] = review[review.find(
                    "<br>") + 4: review.find("%")]
                columns['pop'] = review[review.find(
                    "the ") + 4: review.find(" user")].replace(",", "")
            else:
                columns['pos'] = -1
                columns['pop'] = -1
            cursor.execute(INSERT_DATA.format(**columns))
            gameset.add(line['title'])

    print('insert {0} lines'.format(cursor.rowcount))
    cursor.close()
    conn.commit()


if __name__ == '__main__':
    do_convert()
