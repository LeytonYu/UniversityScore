import requests
from lxml import etree

from util.util import get_json

ggj = '''<option value="北京" selected="">
																															北京
																														</option>
																													
																														<option value="天津">
																															天津
																														</option>
																													
																														<option value="河北">
																															河北
																														</option>
																													
																														<option value="山西">
																															山西
																														</option>
																													
																														<option value="内蒙古">
																															内蒙古
																														</option>
																													
																														<option value="辽宁">
																															辽宁
																														</option>
																													
																														<option value="吉林">
																															吉林
																														</option>
																													
																														<option value="黑龙江">
																															黑龙江
																														</option>
																													
																														<option value="上海">
																															上海
																														</option>
																													
																														<option value="江苏">
																															江苏
																														</option>
																													
																														<option value="浙江">
																															浙江
																														</option>
																													
																														<option value="安徽">
																															安徽
																														</option>
																													
																														<option value="福建">
																															福建
																														</option>
																													
																														<option value="江西">
																															江西
																														</option>
																													
																														<option value="山东">
																															山东
																														</option>
																													
																														<option value="河南">
																															河南
																														</option>
																													
																														<option value="湖北">
																															湖北
																														</option>
																													
																														<option value="湖南">
																															湖南
																														</option>
																													
																														<option value="广东">
																															广东
																														</option>
																													
																														<option value="广西">
																															广西
																														</option>
																													
																														<option value="海南">
																															海南
																														</option>
																													
																														<option value="重庆">
																															重庆
																														</option>
																													
																														<option value="四川">
																															四川
																														</option>
																													
																														<option value="贵州">
																															贵州
																														</option>
																													
																														<option value="云南">
																															云南
																														</option>
																													
																														<option value="西藏">
																															西藏
																														</option>
																													
																														<option value="陕西">
																															陕西
																														</option>
																													
																														<option value="甘肃">
																															甘肃
																														</option>
																													
																														<option value="青海">
																															青海
																														</option>
																													
																														<option value="宁夏">
																															宁夏
																														</option>
																													
																														<option value="新疆">
																															新疆
																														</option>
																													
																														<option value="港澳台侨联招">
																														港澳台侨联招
																													</option>'''


def get_province():
    raw = ggj
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
    base_url = 'https://wsbm.ecust.edu.cn/lqfs.htm'
    base_province = {}
    for year in range(2017, 2021):
        for p in province:
            param = f'nf={year}&province={p}'
            print(param)
            response = requests.post(url=base_url, data=param.encode(), headers=headers)
            html = response.text
            element = etree.HTML(html)
            if not base_province.get(p):

                lst = element.xpath('//*[@id="TB_Ztqk"]/tr')
                base_p_data = []
                for i, obj in enumerate(lst):
                    if i == 0:
                        sb = './td/font/strong/text()'
                    elif i == 1:
                        continue
                    else:
                        sb = './td/text()'
                    tp = obj.xpath(sb)
                    tpp = [pig.strip('\r\n\t') for pig in tp]
                    base_p_data.append(tpp)
                base_province[p] = 1
                with open(f'华东理工大学/{p}历年分数概览.json', 'wb') as f:
                    f.write(get_json(base_p_data).encode())

            fish = element.xpath('//*[@id="TB_Lqfs"]/tr')

            data_name = f'{year}{p}专业录取分数'
            data_lst = []
            for i, obj in enumerate(fish):
                if i == 0:
                    sb = './td/font/strong/text()'
                elif i == 1:
                    continue
                else:
                    sb = './td/text()'
                tp = obj.xpath(sb)
                tpp = [pig.strip('\r\n\t') for pig in tp]
                data_lst.append(tpp)
            with open(f'华东理工大学/{data_name}', 'wb') as f:
                f.write(get_json(data_lst).encode())


if __name__ == '__main__':
    get_data()
