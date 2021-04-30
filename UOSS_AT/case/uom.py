# -*-coding:utf-8-*-

import pytest
import requests

headers = {"device-uuid": "a16c50f1-7f40-3ac4-9343-b47114455300",
           "device-type": "MAC",
           "product-code": "TR-EMM-FREE-MAC",
           "product-version-code": "1.0.0",
           "Content-Type": "application/json; charset=UTF-8",
           "Accept": "application/json"
           }

params = {"locale": "en", "pattern": "msg", "last_at": "1614746473"}
url = 'http://test.uom.com'


def test_msg():
    url_path = url + "/api/message"
    r = requests.get(url_path, headers=headers, params=params)
    assert r.status_code == 200
    print(r.json())


if __name__ == "__main__":
    pytest.main(['-s', '-v', './case/test_uom.py'])
