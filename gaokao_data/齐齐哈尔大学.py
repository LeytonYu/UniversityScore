import requests
from lxml import etree

from util.util import get_json

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "Cache-Control": "no-cache",
    # "Connection": "keep-alive",
    # "Host": "zs.qqhru.edu.cn",
    # "Referer": "http://zs.qqhru.edu.cn/fenshuxian.aspx?y=2018&pageid=01",
    # "Pragma": "no-cache",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def get_data():
    start_id = 639
    end_id = 667
    base_url = 'http://zs.qqhru.edu.cn/fenshuxiandetails.aspx?id={}'
    for i in range(start_id, end_id+1):
        url = base_url.format(i)
        print(url)
        response = requests.get(url, headers=headers)
        html = response.text
        element = etree.HTML(html)
        file_name: str = element.xpath('//*[@class="infodetails_title"]/text()')[0]
        file_name = file_name.strip('\n\r')
        print(file_name)
        # lst = element.xpath('//*[@id="infodetails_body"]/table/tbody/tr')
        lst = element.xpath('//*[@id="infodetails_body"]/div/table/tbody/tr')
        data_store = []
        for j in range(len(lst)):
            sb = './td/p/*/text()'
            sp = './td/p/*/*/text()'
            temp = lst[j].xpath(sb)
            if not temp:
                temp = lst[j].xpath(sp)
            # print(temp)
            data_store.append(temp)
        with open(f"齐齐哈尔大学/{file_name}.json", 'wb') as f:
            f.write(get_json(data_store).encode())
        print(f'{file_name}分数写入完毕')


if __name__ == '__main__':
    get_data()
