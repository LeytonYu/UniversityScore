# -*- coding:utf-8 -*-

import requests
from lxml import etree

from util.util import get_json


def get_province():
    raw = r'<option value="上海" selected="selected">上海</option><option value="云南">云南</option><option value="内蒙古">内蒙古</option><option value="北京">北京</option><option value="吉林">吉林</option><option value="四川">四川</option><option value="天津">天津</option><option value="宁夏">宁夏</option><option value="安徽">安徽</option><option value="山东">山东</option><option value="山西">山西</option><option value="广东">广东</option><option value="广西">广西</option><option value="新疆">新疆</option><option value="本科">本科</option><option value="江苏">江苏</option><option value="江西">江西</option><option value="河北">河北</option><option value="河南">河南</option><option value="浙江">浙江</option><option value="海南">海南</option><option value="湖北">湖北</option><option value="湖南">湖南</option><option value="甘肃">甘肃</option><option value="省份">省份</option><option value="福建">福建</option><option value="西藏">西藏</option><option value="贵州">贵州</option><option value="辽宁">辽宁</option><option value="重庆">重庆</option><option value="陕西">陕西</option><option value="黑龙江">黑龙江</option>'

    element = etree.HTML(raw)
    f = element.xpath('//option/@value')
    return f


def get_data():
    province = get_province()
    headers = {
        'user-agent': "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    base_url = 'https://admission.shmtu.edu.cn/score'
    base_province = {}
    for year in range(2017, 2021):
        pass


if __name__ == '__main__':
    get_data()
