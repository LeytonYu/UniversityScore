# -*- coding:utf-8 -*-
from util.util import str_to_json
import requests
from lxml import etree
from util.util import get_json


def deal_province():

    raw = '[{\"provinceId\":\"911\",\"provinceName\":\"北京\",\"status\":\"0\"},{\"provinceId\":\"912\",\"provinceName\":\"天津\",\"status\":\"0\"},{\"provinceId\":\"913\",\"provinceName\":\"河北\",\"status\":\"0\"},{\"provinceId\":\"914\",\"provinceName\":\"山西\",\"status\":\"0\"},{\"provinceId\":\"915\",\"provinceName\":\"内蒙古\",\"status\":\"0\"},{\"provinceId\":\"921\",\"provinceName\":\"辽宁\",\"status\":\"0\"},{\"provinceId\":\"922\",\"provinceName\":\"吉林\",\"status\":\"0\"},{\"provinceId\":\"923\",\"provinceName\":\"黑龙江\",\"status\":\"0\"},{\"provinceId\":\"931\",\"provinceName\":\"上海\",\"status\":\"0\"},{\"provinceId\":\"932\",\"provinceName\":\"江苏\",\"status\":\"0\"},{\"provinceId\":\"933\",\"provinceName\":\"浙江\",\"status\":\"0\"},{\"provinceId\":\"934\",\"provinceName\":\"安徽\",\"status\":\"0\"},{\"provinceId\":\"935\",\"provinceName\":\"福建\",\"status\":\"0\"},{\"provinceId\":\"936\",\"provinceName\":\"江西\",\"status\":\"0\"},{\"provinceId\":\"937\",\"provinceName\":\"山东\",\"status\":\"0\"},{\"provinceId\":\"941\",\"provinceName\":\"河南\",\"status\":\"0\"},{\"provinceId\":\"942\",\"provinceName\":\"湖北\",\"status\":\"0\"},{\"provinceId\":\"943\",\"provinceName\":\"湖南\",\"status\":\"0\"},{\"provinceId\":\"944\",\"provinceName\":\"广东\",\"status\":\"0\"},{\"provinceId\":\"945\",\"provinceName\":\"广西\",\"status\":\"0\"},{\"provinceId\":\"946\",\"provinceName\":\"海南\",\"status\":\"0\"},{\"provinceId\":\"950\",\"provinceName\":\"重庆\",\"status\":\"0\"},{\"provinceId\":\"951\",\"provinceName\":\"四川\",\"status\":\"0\"},{\"provinceId\":\"952\",\"provinceName\":\"贵州\",\"status\":\"0\"},{\"provinceId\":\"953\",\"provinceName\":\"云南\",\"status\":\"0\"},{\"provinceId\":\"954\",\"provinceName\":\"西藏\",\"status\":\"0\"},{\"provinceId\":\"961\",\"provinceName\":\"陕西\",\"status\":\"0\"},{\"provinceId\":\"962\",\"provinceName\":\"甘肃\",\"status\":\"0\"},{\"provinceId\":\"963\",\"provinceName\":\"青海\",\"status\":\"0\"},{\"provinceId\":\"964\",\"provinceName\":\"宁夏\",\"status\":\"0\"},{\"provinceId\":\"965\",\"provinceName\":\"新疆\",\"status\":\"0\"},{\"provinceId\":\"966\",\"provinceName\":\"港澳台联招\",\"status\":\"0\"}]'
    raw.replace('\\', '')
    after = str_to_json(raw)
    return after


def common(param):
    headers = {
        'cookies': 'JSESSIONID=3104598F5E57B6CB2AF43EA227859023; JSESSIONID=3104598F5E57B6CB2AF43EA227859023',
        'user-agent': "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    base_url = 'https://zsb.ecnu.edu.cn/webapp/scoreSearch-new2.jsp?'
    response = requests.get(url=base_url, params=param, headers=headers)
    html = response.text
    element = etree.HTML(html)
    content = []
    table_head = element.xpath('//*[@id="score-table"]/thead/tr/td/text()')
    content.append(table_head)
    table_body = element.xpath('//*[@id="score-table"]/tr')
    for tbj in table_body:
        line = tbj.xpath('./td/text()')
        print(line)
        content.append(line)

    return content


def get_data():
    provinces = deal_province()
    head = {
        1: '省分数线',
        2: '专业分数',
        3: '艺体类分数',
        4: '计划'
    }
    # 省分数线
    for obj in provinces:
        param = {
            'id': 1,
            'pid': obj['provinceId'],
            'moduleId': 31
        }
        content = common(param)
        file_name = f"华东师范大学/省分数线_{obj['provinceName']}"
        with open(file_name, 'wb') as f:
            f.write(get_json(content).encode())

    # 专业分数线
    for obj in provinces:
        for year in range(2017, 2021):
            param = {
                'id': 2,
                'pid': obj['provinceId'],
                'year': year,
                'moduleId': 31
            }
            content = common(param)
            file_name = f"华东师范大学/专业分数_{year}_{obj['provinceName']}"
            with open(file_name, 'wb') as f:
                f.write(get_json(content).encode())

    # 艺体类分数
    for year in range(2017, 2021):
        param = {
            'id': 3,
            'year': year,
            'moduleId': 31
        }
        content = common(param)
        file_name = f"华东师范大学/艺体类分数_{year}"
        with open(file_name, 'wb') as f:
            f.write(get_json(content).encode())

    # 计划
    for obj in provinces:
        for year in range(2018, 2022):
            param = {
                'id': 4,
                'pid': obj['provinceId'],
                'year': year,
                'moduleId': 31
            }
            content = common(param)
            file_name = f"华东师范大学/计划_{year}_{obj['provinceName']}"
            with open(file_name, 'wb') as f:
                f.write(get_json(content).encode())


if __name__ == '__main__':
    get_data()