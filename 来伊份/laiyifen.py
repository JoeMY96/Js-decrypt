import base64
import requests
from Cryptodome.Cipher import AES


session = requests.Session()

def get_imgeKey(mobile_num):
    """
    获取网站返回的imgeKey
    :return:
    """
    url = "http://m.laiyifen.com/ouser-web/api/user/init.do"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'mobile': mobile_num,
        'initType': '2',
        'width': '160',
        'height': '60',
        'platformId': '3'
    }
    response = session.post(url, data=data, headers=headers).json()
    imageKey = response.get('data').get('imageKey')
    return imageKey


def send_sms(imageKey):
    """
    向手机号发送验证码
    :param imageKey:
    :return:
    """
    url = "http://m.laiyifen.com/ouser-web/mobileRegister/sendCaptchasCodeFormNew.do"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'mobile': '18511882793',
        'captchasType': '3',
        'checkImageCode': '',
        'imgeKey': imageKey,
        'platformId': '3'
    }
    response = session.post(url, data=data, headers=headers).json()
    print(response)


def pad(text):
    """
    填充函数，使被加密数据的字节码长度是block_size的整数倍
    """
    count = len(text)
    add = AES.block_size - (count % AES.block_size)
    entext = text + (chr(add) * add)
    return entext


def get_encrypted_mobile(mobile_num):
    """
    获取AES加密后的手机号
    :param mobile_num:
    :return:
    """
    key = b'1fi;qPa7utddahWy'
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_mobile = cipher.encrypt(pad(mobile_num).encode('utf-8'))
    return "@%^*" + str(base64.b64encode(encrypted_mobile), encoding='utf-8')


def main(mobie_num):
    """
    入口函数，输入手机号和验证码后成功获取响应
    :param mobie_num:
    :return:
    """
    imageKey = get_imgeKey(mobie_num)
    send_sms(imageKey)
    captchas = input('请输入验证码:')
    encrypted_mobile = get_encrypted_mobile(mobie_num)
    data = {
        'mobile': encrypted_mobile,
        'captchas': captchas,
        'companyId': '30',
        'shareCode': 'undefined',
        'platformId': '3'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = session.post(url='http://m.laiyifen.com/ouser-web/mobileLogin/loginForm.do', data=data, headers=headers)
    print(response.text)


if __name__ == '__main__':
    main(mobie_num='1xxxxxxxxxx')
