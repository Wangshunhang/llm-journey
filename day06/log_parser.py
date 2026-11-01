# 输入数据（写在代码里）
# python

# 题目&要求
# logs = """2026-10-31 14:23:01 ERROR [billing-service] ip=10.12.3.45 code=500 cost=1283ms msg="批价计算超时"
# 2026-10-31 14:23:05 INFO [billing-service] ip=10.12.3.45 code=200 cost=35ms msg="入账成功"
# 2026-10-31 14:23:11 WARN [account-service] ip=10.12.3.9 code=200 cost=890ms msg="慢查询"
# 2026-10-31 14:23:19 ERROR [account-service] ip=10.12.3.9 code=500 cost=2300ms msg="账务汇总失败"
# 2026-10-31 14:23:22 INFO [settle-service] ip=10.12.3.77 code=200 cost=12ms msg="结算单生成"
# 2026-10-31 14:23:30 DEBUG [billing-service] ip=10.12.3.45 code=200 cost=8ms msg="缓存命中" """
# 第一步：解析成结构化的 list[dict]
# python


# def parse_line(line):
#     """解析一行日志，返回 dict；解析失败返回 None"""
#     pattern = r'...'           # ← 你来写
#     m = re.search(pattern, line)
#     if not m:
#         return None
#     return {
#         "time": m.group("time"),
#         "level": m.group("level"),
#         "service": m.group("service"),
#         "ip": m.group("ip"),
#         "code": int(m.group("code")),
#         "cost_ms": int(m.group("cost")),
#         "msg": m.group("msg"),
#     }
# 提示：

# 用命名分组 (?P<time>...)
# 时间：\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}
# 级别：[A-Z]+
# 服务名带中括号：\[(?P<service>\w+)\]（[ 在正则里是特殊字符，要写 \[ 转义）
# 耗时：(\d+)ms —— 你只要数字，不要 ms（用分组）
# msg 带引号："(?P<msg>[^"]+)"（"除了引号以外的所有字符"，这句要想一下）
# 第二步：5 个统计函数
# python


# def by_level(parsed):      # {"ERROR": 2, "INFO": 2, "WARN": 1, "DEBUG": 1}
# def slow_requests(parsed, threshold=1000):  # 返回耗时 > 阈值的行（列表）
# def error_rate(parsed):    # ERROR 数 / 总数，保留 2 位
# def by_service(parsed):    # 每个服务的请求数 + 平均耗时
# def ip_summary(parsed):    # 每个 IP 出现次数，降序
# 第三步：输出
# 代码块


# ===== 日志分析报告 =====
# 解析成功：6 行，失败：0 行
# ---
# 按级别：{'ERROR': 2, 'INFO': 2, 'WARN': 1, 'DEBUG': 1}
# 错误率：33.33%
# ---
# 慢请求（>1000ms）：
#   14:23:01 [billing-service] 1283ms 批价计算超时
#   14:23:11 [account-service] 890ms ...   ← 这个不该出现，仔细看
# ---
# 按服务：
#   billing-service   3 次，平均 442.0ms
#   ...
# ---
# 按 IP：
#   10.12.3.45   3 次


# 答题：



import re,sys 


logs = """2026-10-31 14:23:01 ERROR [billing-service] ip=10.12.3.45 code=500 cost=1283ms msg="批价计算超时"
2026-10-31 14:23:05 INFO [billing-service] ip=10.12.3.45 code=200 cost=35ms msg="入账成功"
2026-10-31 14:23:11 WARN [account-service] ip=10.12.3.9 code=200 cost=890ms msg="慢查询"
2026-10-31 14:23:19 ERROR [account-service] ip=10.12.3.9 code=500 cost=2300ms msg="账务汇总失败"
2026-10-31 14:23:22 INFO [settle-service] ip=10.12.3.77 code=200 cost=12ms msg="结算单生成"
2026-10-31 14:23:30 DEBUG [billing-service] ip=10.12.3.45 code=200 cost=8ms msg="缓存命中" """



def parse_line(line):
    pattern = (
    r'(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
    r'(\s+(?P<level>[a-zA-Z]+)\s+)'
    r'(\[(?P<service>[^\]]+)\]\s+)'
    r'(ip=(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+)'
    r'(code=(?P<code>\d+)\s+)'
    r'(cost=(?P<cost>\d+)ms)\s+'  
    r'(msg=\"(?P<msg>[^\"]+)\")'
    )        
    # m = re.search(pattern, line)
    # if not m:
    #     return None
    # return {
    #     "time": m.group("time"),
    #     "level": m.group("level"),
    #     "service": m.group("service"),
    #     "ip": m.group("ip"),
    #     "code": int(m.group("code")),
    #     "cost_ms": int(m.group("cost")),
    #     "msg": m.group("msg"),
    # }
    # 这里查资料的时候遇到了可以用groupdict方法直接返回字典,用re.finditer直接扫描全文，用re.search只是找第一个，这样的话直接返回一整个list[dict1,dict2]给后面用
    # 可以这样写
    result_list = []
    for n in re.finditer(pattern,line):
        data = n.groupdict()
    # 因为正则提取出来的全是字符串，需要手动转一下数字类型,这里可以用推导式吗？感觉有点麻烦，并且可读性也会变差吧？
        data['code'] = int(data['code'])
        data['cost'] = int(data['cost'])
        result_list.append(data)
    return result_list    
# print(parse_line(logs))

# def by_level(parsed):      # {"ERROR": 2, "INFO": 2, "WARN": 1, "DEBUG": 1}
#     try :
#         cnt_error,cnt_info,cnt_warn,cnt_debug = 0,0,0,0
#         for n in parsed:
#             if n['level'] == 'ERROR':
#                 cnt_error +=1
#             elif n['level'] == 'INFO':
#                 cnt_info +=1
#             elif n['level'] == 'WARN':
#                 cnt_warn +=1
#             elif n['level'] == 'DEBUG':
#                 cnt_debug +=1
#         err_rate = cnt_error/sum([cnt_error,cnt_info,cnt_warn,cnt_debug]) 
#     except ZeroDivisionError :
#         return(cnt_error,cnt_info,cnt_warn,cnt_debug,0)
#     # return {
#     #     "ERROR": cnt_error,
#     #     "INFO": cnt_info, 
#     #     "WARN": cnt_warn, 
#     #     "DEBUG": cnt_debug
#     # }
#     #   算了这里不return一个dict了，麻烦，不如直接返回需要的变量，给主流程调用再取
#     return(cnt_error,cnt_info,cnt_warn,cnt_debug,err_rate)

# print(by_level(aaa))

def by_level(parsed):
    counts = {}
    for n in parsed:
        level = n["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts




def slow_requests(parsed, threshold=1000):  # 返回耗时 > 阈值的行（列表）
    result_list = []
    for n in parsed :
        if n['cost'] > threshold :
            # filtered_data = {            #构造一个新字典把需要的key:value放进去,但如果在内存充足的情况下把原始数据都拿出去是不是更方便调用
            #     "time": n["time"],
            #     "service": n["service"],
            #     "cost": n["cost"],
            #     "msg": n["msg"]
            # }
            # result_list.append(filtered_data)
            result_list.append(n)
    return result_list
# print(slow_requests(aaa))



# def error_rate(parsed):    # ERROR 数 / 总数，保留 2 位  
def error_rate(parsed):
    if not parsed:
        return 0.0
    errors = sum(1 for n in parsed if n["level"] == "ERROR")
    return errors / len(parsed)

def by_service(parsed):    # 每个服务的请求数 + 平均耗时
    service_dict = {}    
    for n in parsed :
        svc = n['service']
        cst = n['cost']
        if svc not in service_dict :
            service_dict[svc] = {'counts': 0, 'total': 0}
        service_dict[svc]['counts'] += 1
        service_dict[svc]['total'] += cst
    for svc, data in service_dict.items():
        avg = round(data['total'] / data['counts'], 2)
        data['avg'] = avg 
    return service_dict
# print(by_service(aaa))


def ip_summary(parsed):    # 每个 IP 出现次数，降序
    ip_dict = {}
    for n in parsed :
        eve_ip = n['ip']
        if eve_ip not in ip_dict :
            ip_dict[eve_ip] = 0
        ip_dict[eve_ip] += 1
    #按照value排序下，降序
    sorted_items = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_items
# print(ip_summary(aaa))

# ok开始干活
aaa = parse_line(logs)
if aaa is None or aaa == [] :
    print("❌ 致命错误：日志格式不对，无法解析！")
    sys.exit(1) 
bbb = by_level(aaa)
ccc = slow_requests(aaa)
ddd = by_service(aaa)
eee = ip_summary(aaa)
fff = error_rate(aaa)


print('===== 日志分析报告 =====')
print(f'解析成功：{len(aaa)}行，失败：0 行')
print('---')
print(f"按级别：{bbb}")
print(f'错误率：{fff:.2%}')
print('---')
print(f'慢请求（>1000ms）：')
for n in ccc :
    print(f"    {n['time']} [{n['service']}] {n['cost']}ms {n['msg']}")
print('---')
print('按服务：')
for n,v in ddd.items():
    print(f"    {n} {v['counts']}次 平均{v['avg']}ms")
print('---')
print('按 IP：')
for n,m in eee :
    print(f'{n} {m}次')

# 终于写完了，功能没问题了但是还需要做一下状态控制，异常处理下，如果输入一个空字典呢，这样我在parse_line(logs)加一个判断，如果正则没匹配到返回None的话，或者只返回了空列表，程序退出