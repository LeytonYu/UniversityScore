import re

raw_data = """
            <option value="机械工程"   >机械工程</option>
            <option value="神经科学"   >神经科学</option>
            <option value="药理学"   >药理学</option>
            <option value="化学工程"   >化学工程</option>
            <option value="经济"   >经济</option>
            <option value="土木"   >土木</option>
            <option value="免疫"   >免疫</option>
            <option value="地球"   >地球</option>
            <option value="工业"   >工业</option>
            <option value="商业"   >商业</option>
            <option value="生化"   >生化</option>
            <option value="计算机科学"   >计算机科学</option>
            <option value="农业"   >农业</option>
            <option value="材料科学"   >材料科学</option>
            <option value="环境科学"   >环境科学</option>
            <option value="数学"   >数学</option>
            <option value="航天工程"   >航天工程</option>
            <option value="社会科学"   >社会科学</option>
            <option value="生物医学工程"   >生物医学工程</option>
            <option value="化学"   >化学</option>
            <option value="心理学"   >心理学</option>
            <option value="能源"   >能源</option>
            <option value="物理学"   >物理学</option>
            <option value="通用工程"   >通用工程</option>
            <option value="电气"   >电气</option>
            <option value="医学"   >医学</option>
            <option value="决策科学"   >决策科学</option>
            <option value="建设"   >建设</option>
            <option value="计算力学"   >计算力学</option>
            <option value="材料力学"   >材料力学</option>
            <option value="控制"   >控制</option>
            <option value="海洋工程"   >海洋工程</option>
            <option value="牙医学"   >牙医学</option>
            <option value="安全"   >安全</option>
            <option value="护理学"   >护理学</option>
            <option value="汽车工程"   >汽车工程</option>
            <option value="兽医学"   >兽医学</option>
            <option value="艺术"   >艺术</option>
            <option value="数学 "   >数学 </option>
            <option value="哲学"   >哲学</option>
            <option value="理论经济学"   >理论经济学</option>
            <option value="应用经济学"   >应用经济学</option>
            <option value="法学"   selected  >法学</option>
            <option value="政治学"   >政治学</option>
            <option value="社会学"   >社会学</option>
            <option value="教育学"   >教育学</option>
            <option value="体育学"   >体育学</option>
            <option value="外国语言文学"   >外国语言文学</option>
            <option value="新闻传播学"   >新闻传播学</option>
            <option value="化学工程与技术"   >化学工程与技术</option>
            <option value="天文学"   >天文学</option>
            <option value="地理学"   >地理学</option>
            <option value="生态学"   >生态学</option>
            <option value="大气科学"   >大气科学</option>
            <option value="海洋科学"   >海洋科学</option>
            <option value="地球物理学"   >地球物理学</option>
            <option value="地质学"   >地质学</option>
            <option value="生物学"   >生物学</option>
            <option value="口腔医学"   >口腔医学</option>
            <option value="食品科学与工程"   >食品科学与工程</option>
            <option value="临床医学"   >临床医学</option>
            <option value="系统科学"   >系统科学</option>
            <option value="计算机科学与技术"   >计算机科学与技术</option>
            <option value="统计学"   >统计学</option>
            <option value="力学"   >力学</option>
            <option value="光学工程"   >光学工程</option>
            <option value="仪器科学与技术"   >仪器科学与技术</option>
            <option value="材料科学与工程"   >材料科学与工程</option>
            <option value="冶金工程"   >冶金工程</option>
            <option value="基础医学"   >基础医学</option>
            <option value="动力工程及工程热物理"   >动力工程及工程热物理</option>
            <option value="土木工程"   >土木工程</option>
            <option value="电气工程"   >电气工程</option>
            <option value="交通运输工程"   >交通运输工程</option>
            <option value="船舶与海洋工程"   >船舶与海洋工程</option>
            <option value="电子科学与技术"   >电子科学与技术</option>
            <option value="信息与通信工程"   >信息与通信工程</option>
            <option value="控制科学与工程"   >控制科学与工程</option>
            <option value="软件工程"   >软件工程</option>
            <option value="建筑学"   >建筑学</option>
            <option value="水利工程"   >水利工程</option>
            <option value="农业工程"   >农业工程</option>
            <option value="测绘科学与技术"   >测绘科学与技术</option>
            <option value="环境科学与工程"   >环境科学与工程</option>
            <option value="林业工程"   >林业工程</option>
            <option value="地质资源与地质工程"   >地质资源与地质工程</option>
            <option value="管理科学与工程"   >管理科学与工程</option>
            <option value="矿业工程"   >矿业工程</option>
            <option value="石油与天然气工程"   >石油与天然气工程</option>
            <option value="纺织科学与工程"   >纺织科学与工程</option>
            <option value="轻工技术与工程"   >轻工技术与工程</option>
            <option value="航空宇航科学与技术"   >航空宇航科学与技术</option>
            <option value="兵器科学与技术"   >兵器科学与技术</option>
            <option value="核科学与技术"   >核科学与技术</option>
            <option value="风景园林学"   >风景园林学</option>
            <option value="生物工程"   >生物工程</option>
            <option value="安全科学与工程"   >安全科学与工程</option>
            <option value="网络空间安全"   >网络空间安全</option>
            <option value="作物学"   >作物学</option>
            <option value="园艺学"   >园艺学</option>
            <option value="农业资源与环境"   >农业资源与环境</option>
            <option value="植物保护"   >植物保护</option>
            <option value="畜牧学"   >畜牧学</option>
            <option value="林学"   >林学</option>
            <option value="水产"   >水产</option>
            <option value="草学"   >草学</option>
            <option value="公共卫生与预防医学"   >公共卫生与预防医学</option>
            <option value="中医学"   >中医学</option>
            <option value="中西医结合"   >中西医结合</option>
            <option value="药学"   >药学</option>
            <option value="中药学"   >中药学</option>
            <option value="工商管理"   >工商管理</option>
            <option value="农林经济管理"   >农林经济管理</option>
            <option value="公共管理"   >公共管理</option>
            <option value="图书情报与档案管理"   >图书情报与档案管理</option>
            <option value="毒理学"   >毒理学</option>
            <option value="经济计量学"   >经济计量学</option>
            <option value="管理"   >管理</option>
            <option value="遗传"   >遗传</option>
            <option value="风险"   >风险</option>
            <option value="可靠性"   >可靠性</option>
            <option value="药剂学"   >药剂学</option>
            <option value="金融"   >金融</option>
            <option value="结构工程"   >结构工程</option>
            <option value="微生物学"   >微生物学</option>
            <option value="行星科学"   >行星科学</option>
            <option value="制造工程"   >制造工程</option>
            <option value="会计"   >会计</option>
            <option value="分子生物学"   >分子生物学</option>
            <option value="生物科学"   >生物科学</option>
            <option value="电子工程"   >电子工程</option>
            <option value="建造"   >建造</option>
            <option value="系统工程"   >系统工程</option>
            <option value="质量"   >质量</option>
            <option value="人文"   >人文</option>
"""

my_data = ['机械工程', '神经科学', '药理学', '化学工程', '经济', '土木', '免疫', '地球', '工业', '商业', '生化', '计算机科学', '农业', '材料科学', '环境科学', '数学',
           '航天工程', '社会科学', '生物医学工程', '化学', '心理学', '能源', '物理学', '通用工程', '电气', '医学', '决策科学', '建设', '计算力学', '材料力学', '控制',
           '海洋工程', '牙医学', '安全', '护理学', '汽车工程', '兽医学', '艺术', '数学 ', '哲学', '理论经济学', '应用经济学', '法学', '政治学', '社会学', '教育学',
           '体育学', '外国语言文学', '新闻传播学', '化学工程与技术', '天文学', '地理学', '生态学', '大气科学', '海洋科学', '地球物理学', '地质学', '生物学', '口腔医学',
           '食品科学与工程', '临床医学', '系统科学', '计算机科学与技术', '统计学', '力学', '光学工程', '仪器科学与技术', '材料科学与工程', '冶金工程', '基础医学',
           '动力工程及工程热物理', '土木工程', '电气工程', '交通运输工程', '船舶与海洋工程', '电子科学与技术', '信息与通信工程', '控制科学与工程', '软件工程', '建筑学', '水利工程',
           '农业工程', '测绘科学与技术', '环境科学与工程', '林业工程', '地质资源与地质工程', '管理科学与工程', '矿业工程', '石油与天然气工程', '纺织科学与工程', '轻工技术与工程',
           '航空宇航科学与技术', '兵器科学与技术', '核科学与技术', '风景园林学', '生物工程', '安全科学与工程', '网络空间安全', '作物学', '园艺学', '农业资源与环境', '植物保护',
           '畜牧学', '林学', '水产', '草学', '公共卫生与预防医学', '中医学', '中西医结合', '药学', '中药学', '工商管理', '农林经济管理', '公共管理', '图书情报与档案管理',
           '毒理学', '经济计量学', '管理', '遗传', '风险', '可靠性', '药剂学', '金融', '结构工程', '微生物学', '行星科学', '制造工程', '会计', '分子生物学', '生物科学',
           '电子工程', '建造', '系统工程', '质量', '人文']

pattern = re.compile(r'>(.*?)<')
res = pattern.findall(raw_data)
# print(res)
print(len(my_data))
