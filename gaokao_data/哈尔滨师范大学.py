import requests
from lxml import etree

from util.util import get_json

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

base_url = 'http://zsb.hrbnu.edu.cn/'


def get_url():
    res = []
    url = 'http://zsb.hrbnu.edu.cn/index_lnlqcj.php?year=2020&province=1'
    response = requests.get(url, headers)
    html = response.content
    elements = etree.HTML(html)
    provinces = elements.xpath(
        '//*[@class="province-h-100"] and contains(@style,"margin-top:15px;min-width:800px;height:50px;line-height:30px")/ul/li')
    print(provinces)
    for obj in provinces:
        href = obj.xpath('./a/@href')[0]
        name = obj.xpath('./a/text()')[0]
        res.append({href: name})
    return res


if __name__ == '__main__':
    print(get_url())
