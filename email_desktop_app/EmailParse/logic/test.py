#
# """
# 第二场:卡戎
# 定义
# 	kjong是一种卡片游戏，包括三种类型的卡片，大，小和小丑。
# 	大卡片有8个不同的值，标记为A到H。
# 	小卡片有8个不同的值，用a到h标记。
# 	小丑牌标记为X。
# 规则
# 	5x8+5x8+3=83张牌。(大牌和小牌各值5张，小丑牌3张)
# 	通常有4个玩家围在一张桌子上玩kjong，每个人在游戏开始时分配10张牌，剩下43张牌放在堆里。
# 	每个玩家可以从牌堆的顶部插入一张新牌到他/她的手上，看看这11张牌是否会变成Katte，
# 	一种特殊形式的牌，以赢得游戏。
# Katte
# 	要想知道什么是凯特，我们首先必须知道这些牌是如何联系在一起的。
# 	有三种类型的连接:
# 	三倍
# 		具有相同不区分大小写值的3张卡是Triple，如AAA或BBb。
# 	直
# 		3张带有区分大小写的1偏移量的卡片是Straight，例如ABC或def。但是BcD不算数。
# 	一对
# 		具有相同区分大小写值的2张卡为Pair，如AA或BB。但是Dd不算。
#
# 	Katte是11张牌的一种特殊形式，其中2张为一对，其余9张为m三重(s)和n直(s)，当然m+n=3。
# 	Katte样品
# 		AAABBBCCCdd
# 		ABCBBbCCCFF
# 	百搭牌
# 		3张小丑牌中的任何一张都可以伪装成任何一张卡来组成Katte。因此下面所有的人都是凯特
# 		(X假装是A)
# 		(X假装是d)
# 		XAAABCEFgXX (X,X,X)可以假装为(D, G, G)或(G, G, G)或…)
# 问题
# 	一个10张牌的手是Kattable，当且仅当它将成为Katte插入一个适当的牌。
# 	例如，AABBBCCCdd是Kattable，至少有两个hooler, A和d。
# 	你能认出这个列表中所有的Kattable手(点击我)和每个Kattable的所有hooler吗?
# 预期的输出格式
# 提供了列表:
# 	1.AABBBCCCdd
# 	2.AABBBCCCde
# 	3.AgBBBCCCde
# 	4.AXBBBCCCde
# 预期的输出:
# 	1.ADad
# 	2. cf
# 	4.ABCbcf
# 请遵循:
# 	先输出手数，然后跟着a '。“如果是卡泰伯的话
# 	如果不是，跳过它
# 	按字典顺序输出Hooloers (A-Z，然后A-Z)
# 	所有输出应该打印到标准输出(不要输出任何其他信息，如调试跟踪，以方便验证)
# 为了快速验证，正确输出的前3行应该是:
# 	1.Bb
# 	7.Dd
# 	9.亚甲
# 请将您的代码(测试代码也必须提供)发送到code@rippletek.com
# 谢谢你！
# """

"""

"""
import datetime
import re

from logic.utils import re_date_parse

list_dic = [{'发件人： liuhaiqiang@zhunda.com\r\n发送时间： 2021-07-09 18': '37\r\n收件人： niekai\r\n抄送： renshiyu'},
            {'申请人': '党远洋', '工时周期': '3', '项目编号': 'TSC-2021020008', '项目名称': '乐山云计算项目', '日期': '2021/07/02'},
            {'申请人': '张麻子', '工时周期': '1', '项目编号': 'TSC-2021020008', '项目名称': '华山云计算项目', '日期': '2021/07/03'},
            {'申请人': '黄四郎', '工时周期': '2', '项目编号': 'TSC-2021020008', '项目名称': '华山云计算项目', '日期': '2021/07/04'}
            ]

dic = {'subject': '转发: 回复：南充市嘉陵区AI开放创新平台项目出差申请',
       'from_user': 'renshiyu@zhunda.com',
       'to_user': 'dangyuanyang@zhunda.com',
       'send_date': '2021:07:12-09:12:27',
       'content': '\r\n\r\n\r\n\r\n \r\n发件人： 王波\r\n发送时间： 2021-07-02 08:49\r\n收件人： liuhaiqiang@zhunda.com;'
                  ' 徐锐\r\n抄送： wangyang1; niekai; renshiyu\r\n主题： 回复：南充市嘉陵区AI开放创新平台项目出差申请\r\n同意！'
                  '\r\n\r\n\r\n-------- 原始邮件 --------\r\n发件人： liuhaiqiang@zhunda.com\r\n日期： 2021年7月1日周四 22:03\r\n'
                  '收件人： 王波 <wangbo1@sensetime.com>, 徐锐 <xurui1@sensetime.com>\r\n抄送： wangyang1 <wangyang1@zhunda.com>, '
                  'niekai <niekai@zhunda.com>, renshiyu <renshiyu@zhunda.com>\r\n'
                  '主 题： 南充市嘉陵区AI开放创新平台项目出差申请\r\n各位领导，南充嘉陵区AI开放创新平台项目需要支撑，申请出差，请审批！\r\n'
                  '出差申请单 \r\n申请单编号： \r\n所属公司名称： 四川准达信息技术有限公司 '
                  '申请人： 刘海强 申请日期： 2021/7/1 \r\n一级部门名称: 技术服务中心 直接主管： '
                  '王波 \r\n差旅计划 \r\n起始日期 结束日期 出发城市 目的城市 逗留天数 出行方式 事由（客户/同行同事姓名、目的等）'
                  ' 酒店名称（如须预订酒店）、到访地址 \r\n2021/6/29 2021/7/2 四川省南充市 四川省南充市  4  南充嘉陵区AI开放创新平台项目支撑 '
                  '\r\n连续出差天数：  14  \r\n审批意见 \r\n申请人签字： 刘海强 直接主管审批： 王波 \r\n申请日期： 2021.7.1 审批日期：'
                  ' \r\n以下供备案使用 \r\n人事部备案： 备案日期： \r\n财务部备案： 备案日期： \r\n#NAME? \r\n',
       'bytes_size': 332605}

# 匹配规则必须含有u,可以没有r
# 这里第一个分组的问号是懒惰匹配,必须这么做
def handle_travel_content(content):
    day, date, person, province = None, None, None, None
    con_list = content.split('\r\n')
    new_list = []
    flag = False
    for item in con_list:
        if '出差申请单' in item:
            flag = True
        if flag:
            new_list.append(item)
    count = 0
    for item in new_list:
        print(item)
        print(count, item)
        if count == 6:
            date = re_date_parse(item)
            province = item
        if count == 7:
            day = re.findall('\d+', item)
        if count == 9:
            person = item.split(' ')[1].strip()
        count += 1
    return day, date, person, province


# con = dic['content']
# res = handle_travel_content(con)
# print(res)
li = ['日报', '申请人', '党远洋', '工时周期', '3', '个工作日', '项目编号', 'TSC-2021020008', '项目名称', '乐山云计算项目', '日期', '2021/7/2', 'liguiyang@zhunda.com']
lis = ['', '日报', '', '', '申请人', '党远洋', '', '工时周期', '3', '个工作日', '', '项目编号', 'TSC-2021020008', '', '项目名称', '乐山云计算项目', '', '日期', '2021/7/2', '']

# liss = [item for item in lis if item]
# print(liss)


for i in range(1, 30):
    res ='%.2f' % ((i / 30) * 100)


res = [
    {'发件人：': 'liuhaiqiang@zhunda.com\r\n发送时间：', '2021-07-09': '18:37\r\n收件人：', 'niekai\r\n抄送：': 'renshiyu;', 'daiweixi\r\n主题：': '刘海强7月9号日报\r\n\r\n工号：3421\r\n公司：商汤科技\r\n工作时间：7月8号，9:05-21:05\r\n项目名称：昆明市公安局人像系统项目，智慧瑞丽项目\r\n工作地点：昆明市安康路201号\r\n\r\n\r\n\r\nliuhaiqiang@zhunda.com'},
    {'申请人:': '党远洋工时周期:', '3': '个工作日项目编号:', 'TSC-2021020008项目名称:': '乐山云计算项目日期:'},
    {'申请人:': '党远洋', '工时周期:': '3', '个工作日': '项目编号:', 'TSC-2021020008': '项目名称:', '乐山云计算项目': '日期:'},
    {'申请人:': '党远洋', '工时周期:': '3', '个工作日': '项目编号:', 'TSC-2021020008': '项目名称:', '乐山云计算项目': '日期:'},
    {'能恢复': '十八个复旦', '，客户给': '，他，客户机'},
    {'申请人:': '党远洋;', '工时周期:': '3', ';': '项目编号:', 'TSC-2021020008;': '项目名称:', '乐山云计算项目;': '日期:'},
    {'申请人:': '张麻子;', '工时周期:': '1;', '项目编号:': 'TSC-2021020008;', '项目名称:': '华山云计算项目;', '日期:': '2021/07/03;'},
    {'申请人:': '黄四郎;', '工时周期:': '2;', '项目编号:': 'TSC-2021020008;', '项目名称:': '华山云计算项目;', '日期:': '2021/07/04;'},
    {'申请人:': '黄四郎;', '工时周期:': '1;', '项目编号:': 'TSC-2021020008;', '项目名称:': '华为云备份项目;', '日期:': '2021/08/04;'},
    {'申请人:': '张麻子;', '工时周期:': '2;', '项目编号:': 'TSC-2021020008;', '项目名称:': '深信服项目包揽;', '日期:': '2021/07/10;'},
    {'申请人:': '党远洋;', '工时周期:': '3;', '项目编号:': 'TSC-2021020008;', '项目名称:': '奇安信渗透测试项目;', '日期:': '2021/07/12;'},
    {'申请人:': '党远洋;', '工时周期:': '23;', '项目编号:': 'TSC-2021020008;', '项目名称:': '深信服漏洞测试项目;', '日期:': '2021/07/13;项目内容:'},
    {'申请人:': '黄四郎;', '工时周期:': '1;', '项目编号:': 'TSC-2021020008;', '项目名称:': '华为云备份项目;', '日期:': '2021/08/04;'},
    {'日报': '申请人', '党远洋': '工时周期', '3': '个工作日', '项目编号': 'TSC-2021020008', '项目名称': '乐山云计算项目', '日期': '2021/7/2'},
    {'日报': '申请人', '党远洋': '工时周期', '3': '个工作日', '项目编号': 'TSC-2021020008', '项目名称': '乐山云计算项目', '日期': '2021/7/2'},
    {'申请人': '党远洋', '工时周期': '1900/1/3', '项目编号': 'TSC-2021020008', '项目名称': '乐山云计算项目', '日期': '2021/7/2'},
    {'申请人': '李贵阳', '工时周期': '3', '项目编号': 'TSC-2021020008', '项目名称': '乐山云计算项目', '日期': '2021/7/2'},
    {'申请人': '张麻子', '工时周期': '2', '项目编号': 'TSC-2021020008', '项目名称': '乐山云计算项目', '日期': '2021/7/3'}]



every_name_list = [['2021/7/2', '星期五', '中级', '750', '1900/1/3', 'TSC-2021020008', '乐山云计算项目', '党远洋'], ['2021/7/3', '星期六', '中级', '550', '2', 'TSC-2021020008', '乐山云计算项目', '张麻子'], ['2021/7/2', '星期五', '中级', '650', '3', 'TSC-2021020008', '乐山云计算项目', '李贵阳']]

# keys_set = set()
# data_dic = {}
#
# for item in every_name_list:
#     keys_set.add(item[0])
#
# for key in keys_set:
#     data_dic[key] = []
#
# print(data_dic)
# for key, val in data_dic.items():
#     for item in every_name_list:
#         if key == item[0]:
#             val.append(item)
#             data_dic[key] = val
#


import configparser

cp = configparser.ConfigParser()

filename = cp.read('../static/config.ini')

print(filename)

# 获取配置标题
sec = cp.sections()
print(sec)

# 获取单个配置标题下的 key
item = cp.options('domain')
print(item)

# 获取单个配置标题下的 键值对
items = cp.items('domain')
print(items)

# 直接获取值
ip = cp.get('domain', 'ip')


# # 添加配置
# cp.add_section('python')
# cp.set('python', 'tuple', '不可变集合')
# cp.set('python', 'str', '字符串类型')
# cp.add_section('数组')
# cp.set('数组', 'list', '可变类型')
#
# # 写入文件
# with open('../static/config.ini', 'w+') as f:
#     cp.write(f)
