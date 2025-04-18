import requests

url = 'https://www.bilibili.com/video/BV1Pa411u7Mq'
params ={
    "p":"12",
    "spm_id_from" : "pageDriver",
    "vd_source":"09e7cb2e7bcbf1eba4c6ba188c80342e"
}
headers = {
    "user-agent":"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
r = requests.get(url=url, params=params, headers=headers)
print(r.status_code)
print(r.json())