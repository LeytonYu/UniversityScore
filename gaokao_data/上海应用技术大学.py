import base64
import requests
from util.util import get_json
import random

a = '安徽'
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "26",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Cookie": "ASP.NET_SessionId=55azck0gyqmwgkgyvbxtieua",
    "Host": "enroll.sit.edu.cn",
    "Origin": "https://enroll.sit.edu.cn",
    "Referer": "https://enroll.sit.edu.cn/SysEnroll/SrhScoreLine.aspx",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "sec-ch-ua-mobile": "?0"
}


def get_base64(s):
    return base64.b64encode(s.encode()).decode()


def get_province(year):
    url = 'https://enroll.sit.edu.cn/SysEnroll/SrhScoreLine.aspx?action=GetDropScoreLineProvince'
    param = f'scorelineyear={year}'
    response = requests.post(url=url, headers=headers, data=param.encode())
    return response.json()


def get_data():
    url = 'https://enroll.sit.edu.cn/SysEnroll/SrhScoreLine.aspx?action=SrhScoreLine&random={}'
    for year in range(2018, 2021):
        o_year = year
        year = get_base64(str(year))
        province = get_province(year)
        for obj in province:
            p = obj.get('ScoreLineProvince')
            param = f'NF={year}&SS={get_base64(p)}'
            res = requests.post(url=url, headers=headers, data=param.encode())
            try:
                data = res.json()
                with open(f'上海应用技术大学/{o_year}{p}分数线.json', 'wb') as f:
                    f.write(get_json(data).encode())
                print(f'上海应用技术大学/{o_year}{p}分数线.json 爬取完成')
            except Exception as e:
                print(str(e))
                print(res, res.text)


if __name__ == '__main__':
    get_data()
