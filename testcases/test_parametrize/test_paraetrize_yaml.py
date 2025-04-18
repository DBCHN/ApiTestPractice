import pytest
import requests

from utils.read_data import get_data, get_data_01


@pytest.mark.parametrize("shouji,appkey",get_data["mobile_params"])
def test_mobile(shouji,appkey):
    params = {"shouji": shouji, "appkey": appkey}
    print("测试手机归属地get请求")
    print(shouji,appkey)
    r = requests.get('http://sellshop.5istudy.online/sell/shouji/query',
                     params=params)
    assert r.status_code == 200
    result = r.json()
    assert result["status"] == 0
    assert result["msg"] == "ok"
    assert result["result"]["shouji"] == "13456755448"
    assert result["result"]["province"] == "北京"
    assert result["result"]["city"] == "北京"
    assert result["result"]["company"] == "中国移动"
    assert result["result"]["areacode"] == "0571"

# @pytest.mark.parametrize("name,word",get_data_01["hero_name_word"])
# def test_parametrize_02(name,word):
#     print(f"{name}的台词是{word}")

if __name__ == '__main__':
    pytest.main()