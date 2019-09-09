import os
import sys

import requests

import json



headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) '
                  'AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer': 'http://image.baidu.com/search/index' #  ?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=美女'
    #  http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=美女
}


def get_cookie():
    return requests.get('https://m.baidu.com/sf/vsearch?').cookies
# print(cookies)
# url = 'https://m.baidu.com/sf/vsearch/image/search/wisesearchresult?&word=性感真空美女'


def get_first_page(url, cookies):
    # url = 'https://m.baidu.com/sf/vsearch/image/search/wisesearchresult?rn=10&word=男装&pn=10'
    resp = requests.get(url, cookies=cookies)
# print(json.loads(resp.content.decode('utf-8')))
# print(resp.text)
    for i in json.loads(resp.text)['linkData']:
        link = i['hoverUrl']
        title = i['oriTitle']
        yield (title, link)


def save_image(ky, title, url):
    if not os.path.exists(ky):
        os.mkdir(ky)
    path = os.path.join(ky, title) + '.jpg'

    print(path)
    with open(path, 'wb') as f:
        f.write(requests.get(url).content)


def main(keyword):
    cookies = get_cookie()
    for offset in range(10, sys.maxsize, 10):
        if offset % 90 == 0:
            cookies = get_cookie()
        url = 'https://m.baidu.com/sf/vsearch/image/search/wisesearchresult?rn=10&word=%s&pn=%s' % (keyword, offset)
        for i in get_first_page(url, cookies):
            save_image(keyword, i[0], i[1])


if __name__ == '__main__':
    choice = input('please input you choice:>>').strip()  # 性感真空美女
    print('开始下载%s' % choice)
    main(choice)
    # try:
    #     for offset in range(10, sys.maxsize, 10):
    #         main(choice, offset)
    # except Exception as e:
    #     print(e)
    #     pass
        # print(e) 





