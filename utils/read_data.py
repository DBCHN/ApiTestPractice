import os

import yaml

# f = open("../config/data.yaml", encoding="utf-8")
# data = yaml.safe_load(f)
# print(data)
# print(data["hero"])
# print(data["hero_name"])
# print(data["heros"])
# print(data["hero_name_list"])
# print(data["mobile_params"])

# g = open("../data/data.yaml", encoding="utf-8")
# data = yaml.safe_load(g)
# print(data)
# print(data["mobile_params"])

# def get_data():
#     g = open("../data/data.yaml", encoding="utf-8")
#     data = yaml.safe_load(g)
#     # print(data)
#     print(data["mobile_params"])
#     return data
#     # return None

path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
# def read_data():
#     g = open("../config/data.yaml", encoding="utf-8")
#     data = yaml.safe_load(g)
#     return data
path_02 = os.path.join((os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'config', 'data.yaml')
def read_data_01():
    f = open(path_02, encoding="utf8")
    data_01 = yaml.safe_load(f)
    return data_01

def read_data():
    g = open(path, encoding="utf-8")
    data = yaml.safe_load(g)
    return data

get_data = read_data()
get_data_01 = read_data_01()
print(get_data["mobile_params"])
print(get_data_01["hero_name"])