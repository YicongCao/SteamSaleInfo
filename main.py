from spider import get_sale_games
from csv2sqlite import do_convert
from query import do_query
import requests

BOT_HOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=yourkey"


if __name__ == '__main__':
    get_sale_games(5)
    do_convert()

    data_price = do_query('price')
    r = requests.post(
        BOT_HOOK, json=data_price)

    data_pop = do_query('pop')
    r = requests.post(
        BOT_HOOK, json=data_pop)

    data_pos = do_query('pos')
    r = requests.post(
        BOT_HOOK, json=data_pos)

    print(r.text + "\r\n")
    print(r.status_code, r.reason)
