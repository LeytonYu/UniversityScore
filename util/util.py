import json


def gen_headers(s):
    ls = s.split('\n')
    lsl = []
    # ls = ls[1:-1]
    headers = {}
    for l in ls:
        l = l.split(': ')
        lsl.append(l)

    for x in lsl:
        headers[str(x[0]).strip(' ')] = x[1]

    return headers


def print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))


def get_json(data):
    return json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)


def json_to_str(value):
    if value:
        try:
            return json.dumps(value, ensure_ascii=False)
        except:
            return []
    else:
        return []


if __name__ == '__main__':
    s = """Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Content-Length: 26
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Cookie: ASP.NET_SessionId=55azck0gyqmwgkgyvbxtieua
Host: enroll.sit.edu.cn
Origin: https://enroll.sit.edu.cn
Referer: https://enroll.sit.edu.cn/SysEnroll/SrhScoreLine.aspx
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
X-Requested-With: XMLHttpRequest"""
    res = gen_headers(s)
    print_json(res)
