import sys
import datetime
import utils
from models import Account

help2 = """# python main.py add      # 交互式录入，问日期/类型/分类/金额/备注
# python main.py list     # 列出全部，带序号和格式化金额
# python main.py stats    # 汇总：总收入、总支出、结余、各类支出占比
# python main.py delete n # 删除 id=n"""

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print(f"请正确键入参数：\n{help2}")
    sys.exit(1)

account = Account()          # ← 一行，所有初始化都在里面

if sys.argv[1] == 'add':
    # 输入部分（日期/类型/分类/金额）完全照抄 D7

    #时间
    while True:
        date_a = input("日期（回车=今天，格式例如：2026-11-01)：").strip()
        if not date_a:
            date_a = datetime.date.today().isoformat()
            break
        try:
            datetime.date.fromisoformat(date_a)
            break
        except ValueError:
            print("❌ 格式错误，请重新输入 yyyy-mm-dd")
            continue

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

    rec = account.add(date_a, type_a, category_a, amount_a, note_a)
    print(f"✅ 已添加（id={rec.id}）")

elif sys.argv[1] == 'list':
    if not account:
        print("✅ 暂无记账记录")
        sys.exit(0)

    # 类型映射表
    type_map = {
        "1": "支出",
        "2": "收入"
    }

    # 打印表头
    print(f"{'ID':<4}{'日期':<14}{'类型':<6}{'分类':<10}{'金额':<10}{'备注'}")
    print("-" * 52) # 分割线，美化
    
    for rec in account:
        show_type = type_map[rec.type]        # ← 改成属性访问
        show_money = utils.format_money(rec.amount)
        print(f"{rec.id:<4}{rec.date:<14}{show_type:<6}{rec.category:<10}{show_money:<10}{rec.note}") 

elif sys.argv[1] == 'stats':
    if not account:
        print("✅ 暂无记账记录")
        sys.exit(0)

    t = account.total()
    print(f"总收入：{utils.format_money(t['income'])}")
    print(f"总支出：{utils.format_money(t['expense'])}")
    print(f"结余：  {utils.format_money(t['balance'])}")

    category_data = account.expense_by_category
    if category_data:
        total_fee = sum(category_data.values())
        for c, s in category_data.items():
            print(f'{c:<4}{utils.format_money(s):<4} 支出占比:{s/total_fee:.2%}')

elif  sys.argv[1] == 'delete': #删除 id= 的记录
    if len(sys.argv) != 3 :
        print(f"❌正确用法为python main.py delete n ---删除 id=n的记录")
        sys.exit(1)
    try :  #校验输入的id
        id_input = int(sys.argv[2].strip())
    except ValueError:
        print(f"❌ {sys.argv[2]!r} 不是合法整数 id")
        sys.exit(1)
    if account.delete(id_input):
        print(f"✅ 已删除 id = {id_input}")
    else:
        print(f"❌ 没有 id = {id_input} 的记录")

else:
    print('❌未知命令')
    sys.exit(1)