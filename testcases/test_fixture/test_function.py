import pytest
import requests

# 在括号里加上(autouse=True）即可全局生效function方法，不用在方法
# 不填的话默认scop是function
# @pytest.fixture(scop="function",autouse=True)
@pytest.fixture()
def func():
    print("我是前置步骤~")

def test_mobile_get(func):
    r = requests.get('http://sellshop.5istudy.online/sell/shouji/query',
                     params={"shouji":"13456755448","appkey":"0c818521d38759e1"})
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result["status"] == 0
    assert result["msg"] == "ok"
    assert result["result"]["shouji"] == "13456755448"
    assert result["result"]["province"] == "北京"
    assert result["result"]["city"] == "北京"
    assert result["result"]["company"] == "中国移动"
    assert result["result"]["areacode"] == "0571"

def test_mobile_post(func):
    params = {
        "shouji":"13456755448",
        "appkey":"0c818521d38759e1"
    }
    r = requests.post(url="http://sellshop.5istudy.online/sell/shouji/query",params=params)
    assert r.status_code == 200
    result = r.json()
    assert result["status"] == 0
    assert result["msg"] == "ok"
    assert result["result"]["shouji"] == "13456755448"
    assert result["result"]["province"] == "北京"
    assert result["result"]["city"] == "北京"
    assert result["result"]["company"] == "中国移动"
    assert result["result"]["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()
