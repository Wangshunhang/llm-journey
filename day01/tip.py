# day01\tip.py — 小费分摊
# 输入账单金额、小费率（百分数，如 15）、人数
# 输出三行：小费金额、总计、每人应付（都保留 2 位）
# 验收：100、15、3 → 小费 15.00、总计 115.00、每人 38.33
# 加分项：如果人数是 0，输出"人数不能为 0"（用 if）
try :
    payAcc = float(input('输入账单金额'))
    feeRate = float(input('输入小费率（百分数，如 15）'))
    hc = int(input('输入人数'))
    if hc == 0 :
        print('人数不能为0！')
        exit()
    
    xf = payAcc * feeRate/100
    all = payAcc + xf 
    perp = all / hc
    print(f"小费金额为{xf:.2f}")
    print(f"总计{all:.2f}")
    print(f"每人应付{perp:.2f}")
except ValueError:
    print('请输入正确数字')