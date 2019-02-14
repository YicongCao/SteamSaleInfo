# encoding:utf-8
import os
import sys
import requests
import json


def upload(imgpath):
    name = str(os.path.basename(imgpath)).replace("\n", "").replace("截图", "")
    print(name)
    url = "https://sm.ms/api/upload"
    files = {'smfile': ("%s" % name, open(
        imgpath.replace("\n", ""), 'rb'), 'image/png')}
    print(files)
    sdata = {'ssl': 1}
    res = requests.post(url=url, data=sdata, files=files)
    the_json = res.text
    the_json = json.loads(the_json)
    # print the_json["data"]["delete"]  #删除图片链接
    print("got img url: " + the_json["data"]["url"])  # 图片链接
    print("got img filename: " + the_json["data"]["filename"])  # 文件名
    return the_json["data"]["url"]


def download(imgurl):
    import urllib.request
    import uuid
    filename = uuid.uuid4().hex + '.jpg'
    urllib.request.urlretrieve(imgurl, filename)
    print("got file " + filename + "from " + imgurl)
    return filename


def thumb_to_header(imgurl):
    # 把游戏缩略图的URL转换成标题图的（提升清晰度）
    return str(imgurl).replace("capsule_sm_120.jpg", "header.jpg")


def steam_pic_to_smms(imgurl):
    # 把steam的标题图上传到图床（提升客户端加载速度）
    steamimgurl = thumb_to_header(imgurl)
    # localimgpath = download(steamimgurl)
    # smmsimgurl = upload(localimgpath)
    # os.remove(localimgpath)
    # return smmsimgurl
    return steamimgurl


if __name__ == '__main__':
    testurl = steam_pic_to_smms(
        "https://media.st.dl.bscstorage.net/steam/apps/8190/capsule_sm_120.jpg?t=1543946597")
    print("smms url: " + testurl)
