import requests
import execjs


POST_URL = "https://vipapi.qimingpian.com/DataList/productListVip"
data = {
    'time_interval': '',
    'tag': '',
    'tag_type': '',
    'province': '',
    'lunci': '',
    'page': '1',
    'num': '20',
    'unionid':''
}
resp = requests.post(url=POST_URL, data=data)
cipher_text = resp.json()['encrypt_data']
ctx = execjs.compile(open('企名片/qimingpian.js').read())
second_param = ctx.call("decode", cipher_text)
result = ctx.call('s', "5e5062e82f15fe4ca9d24bc5", second_param, 0, 0, "012345677890123", 1)
print(result.encode('utf-8').decode('unicode_escape'))
