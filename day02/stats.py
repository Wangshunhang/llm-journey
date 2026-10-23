# 题目
# 用 input() 循环录入成绩，输入 done 结束
# 输出：最高分、最低分、平均分、总分、人数
# 平均分保留 2 位小数
# 排序后输出所有成绩
# 上面 5 个统计值不准用 max() min() sum()，自己用循环写
# 验收：输入 90 85 78 95 done → 最高 95、最低 78、平均 87、总分 348、人数 4

# 为什么要手写而不是用 max()？因为面试要考"你知不知道循环怎么写"，而且写了你才知道 max() 帮你省了什么。

po_list = []
while True:
    cont = input('请输出分数,done结束')
    if cont == 'done':
        break
    try :
        num = float(cont)
        po_list.append(num)
    except ValueError:
        print('请输入数字或者done！')
if not po_list :
    print('不能为空！')
else:
    max_point = po_list[0] 
    min_point = po_list[0]
    sum_point = 0        
    for n in po_list :
        if n > max_point :
            max_point = n 
        if n < min_point :
            min_point = n    
        sum_point = sum_point + n
    ave_point = float(sum_point / len(po_list))
    # po_list.sort(reverse=True) #不建议这样 
    # spo_list = po_list # ← 这不是复制！spo_list 和 po_list 是同一个列表
    spo_list = sorted(po_list)
    print(spo_list)
    print(f'最高分{max_point},最低分{min_point},平均分{ave_point:.2f},总分{sum_point},人数{len(po_list)}')