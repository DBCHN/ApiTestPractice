import pytest

# 单参数，单次循环
# @pytest.mark.parametrize("key",["value"])
# def test_parametrize_01(key):
#     print("我是" + key)

# 单参数，多次循环
# 运行时，将列表里的值分别复制给变量，每赋值一次，运行一次
# 一个参数，多个值，测试用例会把每个赋值给参数。进行测试用例的执行，有几个值，测试用例执行几次
# @pytest.mark.parametrize("name",["安琪拉","黄忠","小乔"])
# def test_parametrize_01(name):
#     assert name == "安琪拉"

# 参数值为字典
@pytest.mark.parametrize("hero",[{"name":"安琪拉","word":"火烧屁屁喽"}])
def test_parametrize_01(hero):
    print(hero["name"])
    print(hero["word"])