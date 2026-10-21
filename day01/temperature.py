# 输入摄氏度，输出 华氏 = 摄氏 × 9 / 5 + 32，保留 1 位小数
# 验收：100 → 212.0
# 提示：9 / 5 在 Python 3 里就是 1.8，不用写成 9.0/5.0
try :
    ssTem = float(input('输入摄氏度:'))
    hsTem = ssTem * 9 / 5 + 32
    print(f"华氏度为{hsTem:.1f}")
except ValueError :
    print("请输入数字！")