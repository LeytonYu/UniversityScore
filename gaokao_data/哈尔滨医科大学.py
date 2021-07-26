import requests
from lxml import etree

from util.util import get_json


def get_province():
    url = 'http://www.hrbmu.edu.cn/zhaosheng/lnfs.htm'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    html = response.content
    element = etree.HTML(html)
    lst = element.xpath('//*[@class="list_rightB2 fl"]/ul/li')
    province = []
    for i in range(len(lst)):
        name = lst[i].xpath('./a/@href')[0]
        province.append(name)
        print(name)
    return province


def get_data():
    base_url = 'http://www.hrbmu.edu.cn/zhaosheng/{}'
    province = ['lnfs/gs.htm', 'lnfs/xj.htm', 'lnfs/tj.htm', 'lnfs/hb.htm', 'lnfs/sx.htm', 'lnfs/jl.htm', 'lnfs/zj.htm',
                'lnfs/ah.htm', 'lnfs/fj.htm', 'lnfs/jx.htm', 'lnfs/hb1.htm', 'lnfs/hn.htm', 'lnfs/gd.htm',
                'lnfs/hn1.htm', 'lnfs/sc.htm', 'lnfs/yn.htm', 'lnfs/gx.htm', 'lnfs/ln.htm', 'lnfs/hn2.htm',
                'lnfs/hlj.htm', 'lnfs/bj.htm', 'lnfs/nmg.htm', 'lnfs/js.htm', 'lnfs/sd.htm', 'lnfs/zq.htm',
                'lnfs/gz.htm', 'lnfs/sx1.htm', 'lnfs/sh.htm']
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    f_url = []
    for p in province:
        url = base_url.format(p)
        response = requests.get(url=url, headers=headers)
        html = response.content
        element = etree.HTML(html)
        lst = element.xpath('//*[@class="list_rightB fl"]/ul/li')
        for i in range(len(lst)):
            url_end: str = lst[i].xpath('./a/@href')[0]
            name = lst[i].xpath('./a/text()')[0]
            f_url.append({url_end.lstrip('..'): name})
            url_end_plus = base_url.format(url_end.lstrip('..'))
            print(url_end_plus)
            response = requests.get(url=url_end_plus, headers=headers)
            html_plus = response.content
            # print(html_plus)
            element_plus = etree.HTML(html_plus)
            lst_plus = element_plus.xpath('//*[@class="v_news_content"]/table/tbody/tr')
            lines = []
            for j in range(len(lst_plus)):
                sb = './td/text()' if '2020' in name else './td/*/text()'
                td = lst_plus[j].xpath(sb)
                lines.append(td)

            with open(f"哈尔滨医科大学/{name}.json", 'wb') as f:
                f.write(get_json(lines).encode())
            print(f'{name}分数写入完毕')


if __name__ == '__main__':
    get_data()
