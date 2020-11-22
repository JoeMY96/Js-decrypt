import requests
import execjs


def get_sign(word):
    with open('百度翻译/bdfy.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    sign = execjs.compile(js_code).call('get_sign', word)
    return sign


def fanyi(word):
    POST_URL = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
    data = {
        'from': 'en',
        'to': 'zh',
        'query': word,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': get_sign(word),
        'token': '54dbb35bfcd8a5a28d4fc3efe678b7bc',
        'domain': 'common',
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'cookie': 'BAIDUID=41748C4ECC9FBAF880A6875BDCC88D55:FG=1',
    }
    resp = requests.post(POST_URL, data=data, headers=headers)
    print(resp.text.encode('utf-8').decode('unicode_escape'))


if __name__ == '__main__':
    fanyi('interval')
