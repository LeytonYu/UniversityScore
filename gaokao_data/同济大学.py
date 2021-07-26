import requests
from lxml import etree

from util.util import get_json


def get_province():
    raw = '''<option selected="selected" value="安徽省">安徽省</option><option value="北京市">北京市</option><option value="福建省">福建省</option><option value="甘肃省">甘肃省</option><option value="广东省">广东省</option><option value="广西壮族自治区">广西壮族自治区</option><option value="贵州省">贵州省</option><option value="海南省">海南省</option><option value="河北省">河北省</option><option value="河南省">河南省</option><option value="黑龙江省">黑龙江省</option><option value="湖北省">湖北省</option><option value="湖南省">湖南省</option><option value="吉林省">吉林省</option><option value="江苏省">江苏省</option><option value="江西省">江西省</option><option value="辽宁省">辽宁省</option><option value="内蒙古自治区">内蒙古自治区</option><option value="宁夏回族自治区">宁夏回族自治区</option><option value="青海省">青海省</option><option value="山东省">山东省</option><option value="山西省">山西省</option><option value="陕西省">陕西省</option><option value="上海市">上海市</option><option value="四川省">四川省</option><option value="天津市">天津市</option><option value="西藏自治区">西藏自治区</option><option value="新疆维吾尔自治区">新疆维吾尔自治区</option><option value="云南省">云南省</option><option value="浙江省">浙江省</option><option value="重庆市">重庆市</option>'''
    element = etree.HTML(raw)
    f = element.xpath('//option/text()')
    print(f)


def get_data():
    province = ['安徽省', '北京市', '福建省', '甘肃省', '广东省', '广西壮族自治区', '贵州省', '海南省', '河北省', '河南省',
                '黑龙江省', '湖北省', '湖南省', '吉林省', '江苏省', '江西省', '辽宁省', '内蒙古自治区', '宁夏回族自治区',
                '青海省', '山东省', '山西省', '陕西省', '上海市', '四川省', '天津市', '西藏自治区',
                '新疆维吾尔自治区', '云南省', '浙江省', '重庆市']
    headers = {
        'user-agent': "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    base_url = 'https://bkzs.tongji.edu.cn/index.php?classid=3394&action=search'
    for year in range(2017, 2021):
        for p in province:
            param = f'year={year}&province={p}'
            print(param)
            response = requests.post(url=base_url, data=param.encode(), headers=headers)
            html = response.text
            element = etree.HTML(html)
            lst = element.xpath('//*[@class="admissions_table"]/tr')
            data_all = []
            for tr in lst:
                dd = tr.xpath('./th/text()')
                if not dd:
                    dd = tr.xpath('./td/text()')
                data_all.append(dd)
            with open(f'同济大学/{p}{year}年录取分数.json', 'wb') as f:
                f.write(get_json(data_all).encode())


if __name__ == '__main__':
    # get_province()
    get_data()
