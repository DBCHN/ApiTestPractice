import pytest
from utils.read_data import get_data_01


# 单参数
# heros_name是值，赋值给参数name
@pytest.mark.parametrize('name', get_data_01['hero_name'])
def test_parametrize_01(name):
    print(name)


# 多参数
@pytest.mark.parametrize('name,word', get_data_01['hero_name_word'])
def test_parametrize_02(name, word):
    print(f'{name}的台词是{word}')


if __name__ == '__main__':
    pytest.main(['s', 'test_parametrize_yaml.py'])

