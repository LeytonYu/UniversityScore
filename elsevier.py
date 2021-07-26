import math
import json
import requests
import time


def cacth_data():
    url = "http://elsevier.2020mostcited.blue-dot.cn/index.php?m=index&a=getuserlist"
    my_data = ['机械工程', '神经科学', '药理学', '化学工程', '经济', '土木', '免疫', '地球', '工业', '商业', '生化', '计算机科学', '农业', '材料科学', '环境科学',
               '数学', '航天工程', '社会科学', '生物医学工程', '化学', '心理学', '能源', '物理学', '通用工程', '电气', '医学', '决策科学', '建设', '计算力学',
               '材料力学',
               '控制', '海洋工程', '牙医学', '安全', '护理学', '汽车工程', '兽医学', '艺术', '数学 ', '哲学', '理论经济学', '应用经济学', '法学', '政治学', '社会学',
               '教育学', '体育学', '外国语言文学', '新闻传播学', '化学工程与技术', '天文学', '地理学', '生态学', '大气科学', '海洋科学', '地球物理学', '地质学', '生物学',
               '口腔医学',
               '食品科学与工程', '临床医学', '系统科学', '计算机科学与技术', '统计学', '力学', '光学工程', '仪器科学与技术', '材料科学与工程', '冶金工程', '基础医学',
               '动力工程及工程热物理', '土木工程', '电气工程', '交通运输工程', '船舶与海洋工程', '电子科学与技术', '信息与通信工程', '控制科学与工程', '软件工程', '建筑学',
               '水利工程', '农业工程', '测绘科学与技术', '环境科学与工程', '林业工程', '地质资源与地质工程', '管理科学与工程', '矿业工程', '石油与天然气工程', '纺织科学与工程',
               '轻工技术与工程',
               '航空宇航科学与技术', '兵器科学与技术', '核科学与技术', '风景园林学', '生物工程', '安全科学与工程', '网络空间安全', '作物学', '园艺学', '农业资源与环境', '植物保护',
               '畜牧学', '林学', '水产', '草学', '公共卫生与预防医学', '中医学', '中西医结合', '药学', '中药学', '工商管理', '农林经济管理', '公共管理', '图书情报与档案管理',
               '毒理学', '经济计量学', '管理', '遗传', '风险', '可靠性', '药剂学', '金融', '结构工程', '微生物学', '行星科学', '制造工程', '会计', '分子生物学',
               '生物科学', '电子工程', '建造', '系统工程', '质量', '人文']
    for key in my_data:
        data = f"area={key}&years=2020"
        file_name = f'2020-{key}.json'
        headers = {
            "Connection": "keep-alive",
            "Content-Length": "28",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Origin": "http://elsevier.2020mostcited.blue-dot.cn",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045537 Mobile Safari/537.36 MMWEBID/6811 MicroMessenger/8.0.2.1860(0x2800023D) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://elsevier.2020mostcited.blue-dot.cn/index.php?m=index&a=downloadseach&years=2020&keywords=%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%E4%B8%8E%E6%8A%80%E6%9C%AF",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "PHPSESSID=6gnp6l0gki2fdkuvctlh2dk6fu; gaobeiyin_openid=oZWUvuDxSZCkYqqGGs-24hWZEXxg"
        }
        try:
            res = requests.post(url, headers=headers, data=data.encode('utf8'))
            dd = res.json()
            bb = json.dumps(dd, ensure_ascii=False)
            print(dd)
            with open(file_name, 'wb') as f:
                f.write(bb.encode())
            if dd:
                print('休眠3秒')
                time.sleep(3)

        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    cacth_data()
