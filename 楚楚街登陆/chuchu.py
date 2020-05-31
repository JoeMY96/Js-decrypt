import requests
import execjs

username = "13112341234"
password = '123456'
url = 'http://seller.chuchujie.com/sqe.php?s=/AccountSeller/login'

def getpwd(password):
    with open('chuchu.js', 'r') as f:
        js_code = f.read()
    pwd_encrypt = execjs.compile(js_code).call('getpwd', password)
    return pwd_encrypt


def login():
    pwd_encrypt = getpwd(password)
    print(pwd_encrypt)
    data = {
        'username': username,
        'password': pwd_encrypt,
        'login_type': '',
        'sms_code': '',
        'redirect_uri': '',
        'channle': ''
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '107',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'seller.chuchujie.com',
        'Origin': 'http://seller.chuchujie.com',
        'Referer': 'http://seller.chuchujie.com/sqe.php?s=/User/index',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    res = requests.post(url, headers=headers, data=data)
    print(res.status_code, res.text)


if __name__ == '__main__':
    login()
