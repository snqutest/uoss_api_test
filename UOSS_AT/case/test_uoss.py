# -*-coding:utf-8-*-
"""
Author:ytx
Date:2021.4.8
API Test
"""

import requests
import pytest

# API域名和请求头
url_base = 'http://test.uoss.com'
headers = {
    "device-uuid": "S-1-5-21-2741510373-4127265800-2134946134-1000",
    "device-type": "MAC",
    "product-code": "RE-DRW-FREE-MAC",
    "product-version-code": "5.5.5",
    "geo-country": "China",
    "geo-language": "Simplified Chinese",
    "geo-timezone": "GMT+08:00",
    "Accept": "application/json"
}

# 正确的用户名和密码
data_list = {"email": "kim.tom2050@gmail.com", "password": "test123456"}
# 错误的密码集合,参数化准备
data_list2 = [{"email": "kim.tom2050@gmail.com", "password": "test123xxx"},
              {"email": "kim.tom2050@gmail.com", "password": "test1234560"}]
# 输入邮箱或密码为空
data_list3 = [{"email": "kim.tom2050@gmail.com", "password": ""},
              {"email": "", "password": "test123456"}]


class Test_Uoss:

    # 输入正确的用户名和密码,返回登录token
    def test_login(self):
        url = url_base + '/api/vis/login'
        r = requests.post(url=url, headers=headers, data=data_list)
        # 添加断言
        assert r.status_code == 200
        assert r.json()['message'] == "success"
        tmp_token = r.json()['result']['access_token']
        token = "bearer" + tmp_token
        return token

    # 输入错误的密码，返回错误提示
    @pytest.mark.parametrize('data', data_list2)
    def test_login_fail_01(self, data):
        url = url_base + '/api/vis/login'
        r = requests.post(url=url, headers=headers, data=data)
        # 添加断言
        assert r.json()['message'] == "Password Error."
        print(r.json())

    # 输入邮箱或密码为空,返回错误提示
    @pytest.mark.parametrize('data', data_list3)
    def test_login_fail_02(self, data):
        url = url_base + '/api/vis/login'
        r = requests.post(url=url, headers=headers, data=data)
        # 添加断言
        assert r.json()['message'] in "邮箱 不能为空。|密码 不能为空。"
        print(r.json())

    # 产品列表接口,未传递product_license
    def test_product_01(self):
        url = url_base + '/api/product'
        # 传递token
        headers['Authorization'] = Test_Uoss.test_login(self)
        r = requests.get(url=url, headers=headers)
        print(r.json())

    # 产品列表接口,传递product_license
    def test_product_02(self):
        url = url_base + '/api/product'
        # 传递token
        headers['Authorization'] = Test_Uoss.test_login(self)
        self.params = {"product_license": "123123123123"}
        r = requests.get(url=url, headers=headers, params=self.params)
        print(r.json())


if __name__ == "__main__":
    pytest.main(['-s', './case/test_uoss.py'])
