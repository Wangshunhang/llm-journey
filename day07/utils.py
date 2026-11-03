# 每个函数都有 docstring（三引号）
# 每个函数都有 return
# 函数里不能有 input() 和 print()
# 函数之间不能互相调用（三个函数彼此独立）
# 文件名 utils.py（不能叫 tools.py 或 helper.py——utils 是约定俗成的名字）

# [
#   {"id": 1, "date": "2026-11-01", "type": "expense", "category": "餐饮", "amount": 25.5, "note": "午饭"},
#   {"id": 2, "date": "2026-11-01", "type": "income",  "category": "工资", "amount": 13704, "note": "10月"}
# ]
# 先定数据结构，再写代码



def next_id(records: list[dict]) -> int:
    """返回下一个可用 id（最大 id + 1，空列表返回 1）"""
    if not records:
        return 1
    # nlist = []            #用推导式更简洁，但为了加深练习，还是用基础先写出来
    # for n in records:
    #     nlist.append(n["id"])
    # return(max(nlist)+1)
    return(max(n["id"] for n in records)+1)  

# 测试下
# print(next_id([
#   {"id": 1, "date": "2026-11-01", "type": "expense", "category": "餐饮", "amount": 25.5, "note": "午饭"},
#   {"id": 2, "date": "2026-11-01", "type": "income",  "category": "工资", "amount": 13704, "note": "10月"}
# ]))
# print(next_id([]))

import math

def format_money(n:float)-> str:
    """返回 '¥25.50' 这样的字符串"""
    if n >= 0 :
        return(f'¥{n:.2f}')
    else:
        return(f'-¥{abs(n):.2f}')
# print(format_money(-5))


def validate_amount(text:str)-> float:
    """把输入转成正数 float；非法时 raise ValueError('金额必须大于 0')"""
    try :
        n = float(text.strip())        
    except ValueError :
        raise ValueError("不是合法数字")
    if not math.isfinite(n) :
          raise ValueError("金额必须大于 0")  
    if n <= 0:
        raise ValueError("金额必须大于 0")
    return(n)

if __name__ == "__main__":
    # ---- next_id ----
    assert next_id([]) == 1
    assert next_id([{"id": 1}]) == 2
    assert next_id([{"id": 1}, {"id": 5}]) == 6
    assert next_id([{"id": 5}, {"id": 1}]) == 6

    # ---- format_money ----
    assert format_money(25.5) == "¥25.50"
    assert format_money(0) == "¥0.00"
    assert format_money(13704) == "¥13704.00"
    assert format_money(-25.5) == "-¥25.50"

    # ---- validate_amount ----
    assert validate_amount("25.5") == 25.5
    assert validate_amount(" 30 ") == 30.0
    assert isinstance(validate_amount("100"), float)

    for bad in ["0", "0.0", "-5", "abc", "", " ", "nan", "inf", "-inf"]:
        try:
            validate_amount(bad)
            print(f"❌ {bad!r} 应该报错")
        except ValueError:
            pass

    print("✅ utils.py 全部测试通过")

# print(validate_amount('0.215'))

# 输入
# 用户输入的字符串（来自 input()）。

# 输出
# 返回一个大于 0 的 float。

# 规则
# ✅ 成功的情况：

# 输入	返回	说明
# "25.5"	25.5	
# " 30 "	30.0	去掉两端空白
# "100"	100.0	返回 float，不是 int
# "0.01"	0.01	最小合法值
# ❌ 失败的情况 —— 统一抛 ValueError("金额必须大于 0")：

# 输入	原因
# "0"	等于 0
# "0.0"	等于 0
# "-5"	负数
# "abc"	不是数字
# ""	空字符串
# " "	只有空白
# "nan" / "inf"	特殊值，也算非法

# 必须满足
# 所有失败都抛同一条消息 "金额必须大于 0"
# 函数内不打印任何东西（不 print）——消息由调用者决定怎么显示
# 返回的一定是 float，validate_amount("100") → 100.0


