import os
import urllib.request
import uuid

import requests
from bs4 import BeautifulSoup


def save_pic(url, path):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36 '
    }
    request = urllib.request.Request(url, None, header)
    response = urllib.request.urlopen(request)
    filename = path + '/' + str(uuid.uuid1()) + '.jpg'
    with open(filename, "wb") as f:
        f.write(response.read())


def get_pic_list(url):
    web_data = requests.get(url)
    web_data.encoding = 'gb2312'
    soup = BeautifulSoup(web_data.text, 'lxml')
    info_list = soup.select("body div ul li a img")
    return info_list


def DuoWanSpider(url):
    pic_list = get_pic_list(url)
    for pic in pic_list:
        pic_url = pic.get("src")
        print("图片链接>>>" + pic_url)
        save_pic(pic_url, root_folder)


root_folder = 'DUOWAN/'
base_url = 'http://tu.duowan.com/tag/5037.html/'

if __name__ == "__main__":
    if os.path.isdir(root_folder):
        pass
    else:
        os.mkdir(root_folder)
    DuoWanSpider(base_url)
