# 要求：

# 程序随机生成 1–100 的数（import random）
# 用户输入数字，提示“大了 / 小了”
# 最多猜 7 次，用完就公布答案
# 输入非数字要提示重来，且不扣次数
# 猜对后显示“用了 X 次”
# 验收：能连续玩 3 局不崩；输入 abc 不崩；7 次没猜中会公布答案。

# 这个题练的是 while True + break + continue + try/except 的组合，是你 D1–D3 所有东西的综合。

import random
aaa = random.randint(1,100)
print("-------------我们来玩一个猜数字的游戏，敲入数字1-100，我会告诉你大了还是小了，有7次机会哦---------------")
count = 0
while count < 7 :
    try :
        bbb = int(input('请输入数字：'))
        if bbb < 1 or bbb > 100 :
            print(f'请输入1-100的整数！你已经猜了{count}次了！还剩下{7-count}次机会！')
            continue
        count += 1
        if bbb == aaa :
            print(f'猜对了！你用了{count}次！')
            break
        elif bbb > aaa :
            print(f'大了，再来！你已经猜了{count}次了！还剩下{7-count}次机会！')
            continue
        else :
            print(f'小了，再来！你已经猜了{count}次了！还剩下{7-count}次机会！')
            continue
    except ValueError:
        print(f'请输入一个整数!重来！你已经猜了{count}次了！还剩下{7-count}次机会！')
        continue
else:
    print(f"你用完7次机会了！正确答案是：{aaa}") 
print("Bye!")