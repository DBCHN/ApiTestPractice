import pytest

# 多次循环
# 列表的形式
# @pytest.mark.parametrize("name,word",[["安琪拉","火烧屁屁喽"],["后羿","周日被我射熄火了"],["鲁班","智商二百五"]])
# def test_parametrize_02(name,word):
#     print(f'{name}的台词是{word}')

# 元组的形式
# @pytest.mark.parametrize("name,word",[("安琪拉","火烧屁屁喽"),("后羿","周日被我射熄火了"),("鲁班","智商二百五")])
# def test_parametrize_02(name,word):
#     (print(f'{name}的台词是{word}')

@pytest.mark.parametrize("name,word",[["安琪拉","火烧屁屁喽"]])
def test_parametrize_02(name,word):
    print(f'{name}的台词是{word}')