# 目录结构
# 代码块


# day07/
# ├── main.py
# ├── storage.py
# ├── utils.py
# └── data/
#     └── records.json     ← 程序自动创建
# 数据结构（最重要的一步，先想清楚再写）
# json


# [
#   {"id": 1, "date": "2026-11-01", "type": "expense", "category": "餐饮", "amount": 25.5, "note": "午饭"},
#   {"id": 2, "date": "2026-11-01", "type": "income",  "category": "工资", "amount": 13704, "note": "10月"}
# ]
# 先定数据结构，再写代码。 这一条以后会救你无数次。

# storage.py（先写这个）
# python


# """负责读写 JSON 文件"""
# from pathlib import Path
# import json

# DEFAULT_PATH = Path(__file__).parent / "data" / "records.json"

# def load(path=DEFAULT_PATH):
#     """读取记录列表；文件不存在或损坏时返回 []"""
#     ...

# def save(records, path=DEFAULT_PATH):
#     """保存记录列表，自动创建目录"""
#     ...
# 要求：

# load 遇到文件不存在 → 返回 []，不报错
# load 遇到内容损坏 → 打印警告，返回 []
# save 自动建 data/ 目录
# 两个函数都有 docstring
# Path(__file__).parent = “当前文件所在目录”。用它，不要用相对路径 "data/..."——相对路径依赖你在哪运行，是个坑。

# utils.py
# python


# def next_id(records):
#     """返回下一个可用 id（最大 id + 1，空列表返回 1）"""

# def format_money(n):
#     """返回 '¥25.50' 这样的字符串"""

# def validate_amount(text):
#     """把输入转成正数 float；非法时 raise ValueError('金额必须大于 0')"""
# main.py（最后写）
# 支持 4 个命令：

# powershell


# python day07/main.py add      # 交互式录入，问日期/类型/分类/金额/备注
# python day07/main.py list     # 列出全部，带序号和格式化金额
# python day07/main.py stats    # 汇总：总收入、总支出、结余、各类支出占比
# python day07/main.py delete 3 # 删除 id=3
# 必须处理：

# 不带参数 → 打印帮助，exit(1)  --ok
# 未知命令 → 提示“未知命令”，exit(1)  --ok
# delete 不带 id → 提示用法
# 删除不存在的 id → “没有 id=99 的记录”，不崩
# 录入时金额输 abc → 提示重输，不崩  --ok
# list 时没有任何记录 → “暂无记录”      --ok
# 验收（写在 README 里）
# 代码块


# $ python main.py add
# 日期（回车=今天）：2026-11-01
# 类型（1 支出 / 2 收入）：1
# 分类：餐饮
# 金额：25.5
# 备注（可空）：午饭
# ✅ 已添加（id=1）

# $ python main.py list
# ID   日期          类型    分类        金额      备注
# 1    2026-11-01   支出   餐饮        ¥25.50    午饭

# $ python main.py stats
# 总收入：¥0.00
# 总支出：¥25.50
# 结余：  ¥-25.50
# 各类支出：
#   餐饮      ¥25.50   100.0%

# $ python main.py delete 99
# ❌ 没有 id=99 的记录


import storage,utils,sys,datetime

#print(" python main.py add       交互式录入，问日期/类型/分类/金额/备注\r\n python main.py list      列出全部，带序号和格式化金额\r\n python main.py stats     汇总：总收入、总支出、结余、各类支出占比\r\n python main.py delete n  删除 id=n")
help2 = """# python main.py add      # 交互式录入，问日期/类型/分类/金额/备注
# python main.py list     # 列出全部，带序号和格式化金额
# python main.py stats    # 汇总：总收入、总支出、结余、各类支出占比
# python main.py delete n # 删除 id=n"""

#输出参数校验
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print(f"请正确键入参数，参考如下：\r\n{help2}")
    sys.exit(1)

if sys.argv[1] == 'add':  # 交互式录入，问日期/类型/分类/金额/备注
    records = storage.load()
    id_a = utils.next_id(records)

    #时间
    date_a = input("日期（回车=今天，格式例如：2026-11-01)：")
    if not date_a:
        date_a = datetime.date.today().isoformat()
    print(date_a)

    # 类型校验
    while True:
        t_input = input("类型（1 支出 / 2 收入）:").strip()
        if not t_input:
            print("❌ 类型不能为空，请重新输入！")
            continue
        if t_input not in ("1", "2"):
            print("❌ 类型只能输入 1 或者 2，请重新输入！")
            continue
        type_a = t_input
        break

    # 分类校验
    while True:
        c_input = input("分类：").strip()
        if not c_input:
            print("❌ 分类不能为空，请重新输入！")
            continue
        category_a = c_input
        break

    # 金额校验输入 + 错误重试
    while True:
        amount_input = input("金额：")
        try:
            amount_a = utils.validate_amount(amount_input)
            break
        except ValueError as e:
            print(f"❌ {e}，请重新输入！")

    note_a = input("备注（可空）")
    dict_add = {
        "id" : id_a,
        "date" : f'{date_a}',
        "type" : f'{type_a}',
        "category" : f'{category_a}',
        "amount" : amount_a,
        "note" : f'{note_a}'
        }
    records.append(dict_add)  
    # print(dict_add)
    # print(records)
    storage.save(records)  #写json
    print(f" ✅ 已添加（id={id_a}）") 

elif sys.argv[1] == 'list':     # 列出全部，带序号和格式化金额
    records = storage.load()
    if not records:
        print(" ✅ 暂无记账记录")
        sys.exit(0)

    # 类型映射表
    type_map = {
        "1": "支出",
        "2": "收入"
    }
    # 打印表头
    print(f"{'ID':<4}{'日期':<14}{'类型':<6}{'分类':<10}{'金额':<10}{'备注'}")
    print("-" * 52) # 分割线，美化

    # 循环逐条打印
    for rec in records:
        show_type = type_map[rec["type"]]
        show_money = utils.format_money(rec["amount"])
        print(f"{rec['id']:<4}{rec['date']:<14}{show_type:<6}{rec['category']:<10}{show_money:<10}{rec['note']}") 

elif  sys.argv[1] == 'stats':       # 汇总：总收入、总支出、结余、各类支出占比
    records = storage.load()
    if not records:
        print(" ✅ 暂无记账记录")
        sys.exit(0)

    income = sum(n["amount"] for n in records if n["type"] == "2")
    expense = sum(n["amount"] for n in records if n["type"] == "1")
    print(f"总收入：{utils.format_money(income)}")
    print(f"总支出：{utils.format_money(expense)}")
    print(f"结余：  {utils.format_money(income - expense)}")
    category_data = {} 
    # category_cnt = {}  #建两个个关于分类的字典，一个存累加金额，一个记累加次数，用get规避取不到报错
    for n in records:
        if n['type'] == '1' :
            c = n['category']
            category_data[c] = category_data.get(c, 0) + n['amount']
            # category_cnt[c] = category_cnt.get(c, 0) + 1
    # print(category_data)
    # print(category_cnt)
    total_fee = 0
    if category_data:                  # 没有支出就不显示这块
        total_fee = sum(category_data.values())

    for c, s in category_data.items():
        print(f'{c:<4}{utils.format_money(s):<4} 支出占比:{s/total_fee:.2%}') # ✅真正的原因是“空 dict 不进入循环”，不是“金额不为 0”

elif  sys.argv[1] == 'delete': #删除 id= 的记录
    if len(sys.argv) != 3 :
        print(f"❌正确用法为python main.py delete n ---删除 id=n的记录")
        sys.exit(1)
    try :  #校验输入的id
        id_input = int(sys.argv[2].strip())
    except ValueError:
        print(f"❌ {sys.argv[2]!r} 不是合法整数 id")
        sys.exit(1)
    records = storage.load()
    # if id_input <= 0 or id_input >= utils.next_id(records) :  删掉，后面delx已经校验过
    #     print(f'❌没有id = {id_input}的记录，清确认！')
    #     sys.exit(1)
    if not records:
        print(" ✅ 暂无记账记录")
        sys.exit(0) 
    delx = -1          
    for i,n in enumerate(records) :
        if n['id'] == id_input :
            delx = i
            break
    if delx == -1:  #这里需要校验了，因为不能保证id是连续的，中间可能已经删除某些id了
        print(f'❌没有id = {id_input}的记录，请确认！')
        sys.exit(1)
    del records[delx] #这个时候可以确定删除了
    print(f"✅ 已删除 id = {id_input}")
    # print(records)
    storage.save(records) #写到json里
else :
    print('❌未知命令')
    sys.exit(1)

# [
#   {"id": 1, "date": "2026-11-01", "type": "expense", "category": "餐饮", "amount": 25.5, "note": "午饭"},
#   {"id": 2, "date": "2026-11-01", "type": "income",  "category": "工资", "amount": 13704, "note": "10月"}
# ]