import pytest
import requests

# 类级 setup_class/teardown_class 只能在类中前后运行一次（在类中）

class TestMoblie:

    def setup_class(self):
        print("准备测试数据")

    def teardown_class(self):
        print("清理测试数据")

    def test_mobile_get(self):
        print("测试手机归属地get请求")
        r = requests.get('http://sellshop.5istudy.online/sell/shouji/query',
                         params={"shouji":"13456755448","appkey":"0c818521d38759e1"})
        assert r.status_code == 200
        result = r.json()
        assert result["status"] == 0
        assert result["msg"] == "ok"
        assert result["result"]["shouji"] == "13456755448"
        assert result["result"]["province"] == "北京"
        assert result["result"]["city"] == "北京"
        assert result["result"]["company"] == "中国移动"
        assert result["result"]["areacode"] == "0571"

    def test_mobile_post(self):
        print("测试手机归属地post请求")
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
