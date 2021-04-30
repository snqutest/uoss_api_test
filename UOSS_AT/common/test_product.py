#-*-coding:utf-8-*-

import pytest
import requests
import sys

sys.path.append(r"D:\APT_AT\UOSS_AT")
from test_login import test_Login



url_base = 'http://test.uoss.com'
headers = {"device-uuid":"S-1-5-21-2741510373-4127265800-2134946134-1000",\
    "device-type":"MAC",\
    "product-code":"RE-DRW-FRAD-MAC",\
    "product-version-code":"5.5.5",\
    "Accept":"application/json"}

headers['Authorization'] = 'bearer'+ test_Login.test_login_ok()


params = {"product_license":"AGX3I-KN2TZ-7EIMF-2HG5C-3ZTDT"}

class test_Product:
    def setup(self):
        self.url = url_base + '/api/product'

    def test_getproduct_01(self):
        r = requests.get(url=self.url,params=params,headers=headers,)
        print (r.json())


if __name__ == "__main__":
    pytest.main(['-s','./case/test_product.py'])
