import random
import time
from hashlib import md5
import requests

POST_URL = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '237',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'fanyi.youdao.com',
    'Cookie': '_ntes_nnid=c2e8b3889a4e492c6fe6e26e5b1cb8f8,1587784053558; OUTFOX_SEARCH_USER_ID_NCOO=187090278.2818206; OUTFOX_SEARCH_USER_ID="80931887@10.108.160.17"; JSESSIONID=aaayUM2imR3NY4nzCZBxx; ___rl__test__cookies=1605710527264',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_lts():
    return str(int(time.time() * 1000))


def get_sign(text):
    m = md5()
    m.update(text.encode())
    return m.hexdigest()


def yd_fanyi(word):
    lts = get_lts()
    salt = lts + str(int(10 * random.random()))
    payload = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': get_sign("fanyideskweb" + word + salt + "]BjuETDhU)zqSxf-=B#7m"),
        'lts': lts,
        'bv': 'c1c41987054d21b9b6b774b13ee78f5c',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    result = requests.post(url=POST_URL, data=payload, headers=HEADERS)
    return result.json()['translateResult'][0][0]['tgt']


if __name__ == '__main__':
    print(yd_fanyi('fuck'))