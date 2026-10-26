# po_list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]

# po_list.append('111')
# po_list[5] = '222'
# # 读取第二位
# print (po_list[5])
# # 从第二位开始（包含）截取到倒数第二位（不包含）
# print (po_list[1:-2])


# ① 列表是什么
# python


# todo = ["买菜", "写代码", "看书"]
# print(todo[0])      # 买菜   ← 索引从 0 开始
# print(todo[-1])     # 看书   ← 负数从末尾数
# print(len(todo))    # 3
# 四种"动列表"的操作（今天必须熟


# todo.append("运动")       # 加到最后
# todo.insert(1, "喝水")    # 插到指定位置
# todo.remove("看书")       # 按值删除
# last = todo.pop()         # 弹出最后一个，并返回它

# todo.sort()               # 原地排序（改变自己）
# todo.sort(reverse=True)   # 倒序
# todo.reverse()            # 反转
# 切片：a[起:止:步]——止的位置不包含
# python


# nums = [10, 20, 30, 40, 50]
# nums[1:3]      # [20, 30]      ← 要下标 1、2，不要 3
# nums[:2]       # [10, 20]      ← 从头开始
# nums[2:]       # [30, 40, 50]  ← 到末尾
# nums[::-1]     # [50, 40, 30, 20, 10]  ← 反转（AI 项目里天天用）



# for i, item in enumerate(todo, start=1):
#     print(f"{i}. {item}")

# names = ["A", "B"]
# scores = [90, 85]
# for name, score in zip(names, scores):
#     print(f"{name}: {score}")

# python


# if "买菜" in todo:
#     print("找到了")

# lens = [len(x) for x in todo]     # 每个元素的长度
# ⑥ 今天最大的坑：引用，不是复制
# python


# a = [1, 2, 3]
# b = a          # ← 不是复制！b 和 a 指向同一个列表
# b.append(4)
# print(a)       # [1, 2, 3, 4]  ← a 也变了！

# c = a.copy()   # 这样才是复制
# c.append(5)
# print(a)       # [1, 2, 3, 4]  ← a 没变


# ② day02\todo.py — 待办清单（1.5 小时）
# 要求：

# 启动时显示菜单：1 查看 2 添加 3 删除 4 退出
# 循环接受指令，直到输入 4
# 删除时按编号删（先显示 1. 买菜，再让用户输编号）
# 列表用 list，D2 不存文件（D7 才学文件）
# 删除编号不存在时，提示"没有这个编号"，程序不能崩

todo_list = [] 

while True:
    # 打印菜单
    print("=====待办清单=====")
    print("1 查看待办")
    print("2 添加待办")
    print("3 删除待办")
    print("4 退出程序")
    op = input("请输入操作序号：") 
    # 1 查看
    if op == "1":
        if not todo_list :
            print('待办事项为空！')
        else :
            for i,item in enumerate(todo_list,start = 1) :
                print(f"{i}.{item}")
    # 2 添加
    elif op == "2":
        content =  input('输入待办事项：')
        todo_list.append(content)
        print('加好了')
    # 3 删除
    # 删除之前先展示一下
    elif op == "3" :
        if not todo_list :
            print('没有可以删除的待办事项！')
            continue
        else :
            for i,item in enumerate(todo_list,start = 1) :
                print(f"{i}.{item}")
        try :
            idx = int(input('选择删除的序号'))
            if idx < 1 or idx > len(todo_list):
                print("没有这个编号!")
            else:
                del todo_list[idx-1]       
        except ValueError :
            print('请输入数字编号！')
        except IndexError:
            print("没有这个编号!") 
    # 4 退出程序
    elif op == '4' :
        print('bye bye!')
        break 
    else :
        print('请输出1-4数字，谢谢')      
    