import time
import requests
import execjs

user_name = 'yang'
password = '123456'


def get_time():
    localtime = int(round(time.time() * 1000))
    return localtime


def get_pwd():
    with open('sklm.js', 'r') as f:
        js_code = f.read()
    result = execjs.compile(js_code).call('getpwd', password)
    return result


def login():
    new_pwd = get_pwd()
    url = "http://login.shikee.com/check/?&_{}".format(get_time())
    data = {
        'username': user_name,
        'password': new_pwd,
        'vcode': '',
        'to': 'http://www.shikee.com/'
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '320',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',''
        'Host': 'login.shikee.com',
        'Origin': 'http://login.shikee.com',
        'Referer': 'http://login.shikee.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    res = requests.post(url, data=data, headers=headers)
    print(res.status_code, res.json())


if __name__ == '__main__':
    login()
