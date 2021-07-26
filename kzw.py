import math

import requests
import openpyxl


def catch_save_data(panme):
    """
    爬取岗位工资信息
    :param panme:
    :return:
    """
    url = 'https://www.kanzhun.com/search/salary.json'
    param = dict(query=panme,
                 type=0,
                 cityCode=0,
                 industryCodes=0,
                 pageNum=1,
                 limit=15, )
    headers = {
        "cookie": "W_CITY_S_V=42; ac=15857590552; __t=mPmIrEksgcHwgYC; R_SCH_CY_V=15392|21941|73377|22486106; acw_tc=0bcb2f1816237503473457494e30c142424b2a29d8f6bdbb1e6d3de3a20c86; AB_T=abvb; __c=1623750349; __g=-; __l=l=%2Fwww.kanzhun.com%2Fmsh%2F&r=; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1623750349; JSESSIONID=""; __a=65581123.1616397757.1619060800.1623750349.36.4.2.36; t=mPmIrEksgcHwgYC; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1623750359; lastMessageId=54323558",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        # ":authority": "www.kanzhun.com",
        # ":method": "GET",
        # ":path": "/search/salary.json?query=%E6%95%99%E6%8E%88&type=0&cityCode=0&industryCodes=&pageNum=2&limit=15",
        # ":scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Host": "www.kanzhun.com",
        "referer": "https://www.kanzhun.com/search/?pageCurrent=2&q=%E6%95%99%E6%8E%88&type=salary",
        "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }

    iwant = {
        '学校': '',
        '职位': '',
        '样本数': 0,
        '平均值': 0,
        '最小值': 0,
        '最大值': 0
    }
    sheet_headers = tuple(iwant.keys())
    res = []
    print('单独测试')
    content = requests.get(url=url, headers=headers, params=param)
    tp = content.json()
    try:
        total_count = math.ceil(int(tp['resdata']['totalCount']) / 15)
    except:
        total_count = int(tp['resdata']['pageCount'])
    print(content.json())
    for i in range(1, total_count+1):
        print(f'爬取第{i}页')
        param['pageNum'] = i
        # print(param)
        try:
            content = requests.get(url=url, headers=headers, params=param)
            temp = content.json()
            ggj = temp.get('resdata').get('salarys')
            print(ggj)
            if ggj:
                for obj in ggj:
                    res.append({
                        '学校': obj.get('companyName'),
                        '职位': obj.get('positionName'),
                        '样本数': obj.get('count'),
                        '平均值': obj.get('avg'),
                        '最小值': obj.get('min'),
                        '最大值': obj.get('max')
                    })
        except Exception as e:
            print(e.__str__())

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(sheet_headers)
    for line_dict in res:
        sheet.append([
            line_dict.get(k)
            for k in sheet_headers
        ])
    wb.save(f'{panme}工资.xlsx')


def get_diff_pos_data():
    # pos_type = ['讲师', '博士后', '助理教授', '助理研究员', '大学辅导员', '科研助理']
    # pos_type = ['科研助理', '研究院研究员']
    pos_type = ['研究员', '副研究员', '助理研究员']

    for pname in pos_type:
        catch_save_data(pname)


def test_sth():
    a = math.ceil(17 / 4)
    print(a)


if __name__ == '__main__':
    get_diff_pos_data()
