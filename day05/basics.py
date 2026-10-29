# 每个都要有 docstring 和 return：

# python


#1 def is_even(n):
#     """判断是否为偶数"""
#     return n % 2 == 0
# 写这 8 个：

# is_even(n) — 是否偶数

def is_even(n):
    return n % 2 == 0 
while True :
    try :
        a = int(input('请输入一个整数'))
        break
    except ValueError:
        print('必须是整数')
        # continue #这个可以省掉，会重新循环
if is_even(a):
    print(f"{a} 是偶数")
else:
    print(f"{a} 是奇数")



#2 celsius_to_fahrenheit(c) — 摄氏转华氏  这里我改了下，一个函数完成所有的事情，包含输入输出和状态控制，不知道是功能和控制一起写好一点还是分开写好点，AI你能帮我回答下吗？


def celsius_to_fahrenheit() :
    while True:
        try :
            c = float(input('输入摄氏度:'))
            fahrenheit = c * 9 / 5 + 32
            print(f"{c}摄氏度 = {fahrenheit:.1f}华氏度") 
            return fahrenheit
        except ValueError :
            print("请输入数字！")
celsius_to_fahrenheit()





#3 calc_bmi(height, weight) — 返回 BMI（保留 2 位） 我觉得函数最好只写功能；把流程，输入输出，状态控制还是放到外面吧，方便调试.对吗？


def calc_bmi(height, weight) :
    return round(weight / height**2, 2)
while True :
    try:
        height1= float(input('输入身高（米）'))
        weight1= float(input('输入体重（公斤）'))
        if height1 == 0 :
            print("身高不能为0！请重新输入")
        else :
            BMI1 = calc_bmi(height1,weight1)
            if BMI1 < 18.5 :
                print(f"你的BMI指数是{BMI1:.2f},偏瘦")
                break
            elif BMI1 <= 24 :
                print(f"你的BMI指数是{BMI1:.2f},正常")
                break
            else :
                print(f"你的BMI指数是{BMI1:.2f},偏胖")
                break           
    except ValueError:
        print("请输入数字！")

#4 get_grade(score) — 返回 'A'/'B'/'C'/'D'  何意味，不理解需求？ 难道是输入一个分数，评价ABCD等级吗？


def get_grade(score):
    if 90 <= score <= 100  :
        return('A')
    elif 80 <= score < 90 :
        return('B')
    elif 60 <= score < 80 :
        return('C')
    else :
        return('D')
while True :
    try :
        aaa = float(input('请输出你的成绩，0-100:  '))
        if aaa < 0 or aaa > 100 :
            print('请输入0-100的数！')
            continue
        else :
            print(f'你的成绩评级为{get_grade(aaa)}！')
            break
    except ValueError:
        print("请输入数字！")


#5 count_words(text) — 返回词频 dict（把 D3 的代码搬进函数）,这个就不用while True控制了



import re
def count_words(text1) :
    bbb = re.sub(r'[^a-zA-Z\s]', '', text1).lower().split()
    dict_a = {}
    for i in bbb :
        dict_a[i] = dict_a.get(i,0) + 1
    stop_words = ['a', 'the','is']
    for n in stop_words:
        if n in dict_a:
            del dict_a[n]
    return(dict_a)
def top_n(counts, n=10): #从词频字典里取前 n
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]
aaa = input(rf"请输入一串文本,回车执行，换行请用'\r\n'")
bbb = count_words(aaa)
for rank, (word, cnt) in enumerate(top_n(bbb), start=1):
    print(f'{rank}. {word} — {cnt} 次')




#6 filter_even(nums) — 返回偶数列表（用推导式）,这个就不用while True控制了


def filter_even(nums): #处理列表
    int_nums = []   
    for x in nums:
        # 去掉字符串前后的空格
        x = x.strip()        
        # 如果用户多打了逗号，会产生空字符串 ''，也算无效输入
        if x == '':
            continue  # 忽略空字符串（如果空也算错，可以把 continue 换成 raise）           
        try:
            # 尝试转换成整数
            int_nums.append(int(x))
        except ValueError:
            # 只要有一个转换失败（比如输入了字母、中文），直接报错！
            # 这里的 raise 会触发外面的 except ValueError
            raise ValueError(f"输入的值 {x!r} 不是数字")
        # 代码能走到这里，说明全部都是合法数字，现在过滤偶数
    li = [n for n in int_nums if n % 2 == 0]
    return li    
try :
    aaa = input('请输入整数，用逗号隔开：').replace('，', ',').split(',') # 如果用户不按要求输入比如一个客户去了酒吧要游泳，咋办;唉，先把中文符号过滤吧.想到了，可以强制转换成int，报错就抛异常呗！在函数里做！
    print(f"偶数列表是{filter_even(aaa)}")
except ValueError as e :
    print(e)

#7 min_max(nums) — 返回 (最小值, 最大值)  哈哈我现在有处理输入列表的经验了！,这个就不用while True控制了


def min_max(nums): #处理列表
    int_nums = []   
    for x in nums:
        # 去掉字符串前后的空格
        x = x.strip()        
        # 如果用户多打了逗号，会产生空字符串 ''，也算无效输入
        if x == '':
            continue  # 忽略空字符串（如果空也算错，可以把 continue 换成 raise）           
        try:
            int_nums.append(float(x))
        except ValueError:
            # 只要有一个转换失败（比如输入了字母、中文），直接报错！
            # 这里的 raise 会触发外面的 except ValueError
            raise ValueError(f"输入的值 {x!r} 不是数字")
        # 代码能走到这里，说明全部都是合法数字，现在写功能
    return min(int_nums),max(int_nums)    
try :
    aaa = input('请输入整数，用逗号隔开：').replace('，', ',').split(',')
    min_aaa ,max_aaa =  min_max(aaa)
    print(f"最小值为：{min_aaa:g},最大值为: {max_aaa:g}")
except ValueError as e :
    print(e)


#8 safe_div(a, b) — 除法，b 为 0 时返回 None 不崩,这个就不用while True控制了
def safe_div(a, b):
    if b == 0:
        return None
    return a / b

try:
    a = float(input("被除数："))
    b = float(input("除数："))
    result = safe_div(a, b)                 
    if result is None:
        print("错误：除数不能为 0")
    else:
        print(f"结果是：{result}")
except ValueError:
    print("请输入数字")

# 每个函数在下面写 2–3 行调用测试。