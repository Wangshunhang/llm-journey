# day1
# age = 25                # 普通变量名，最常见
# user_name = "Alice"     # 用下划线连接单词，清晰易读
# _total = 100            # 下划线开头通常表示“内部使用”或“私有”
# MAX_SIZE = 1024         # 全大写通常表示“常量”（固定不变的值）
# calculate_area()        # 函数名，动词+名词
# StudentInfo             # 类名，首字母大写（驼峰命名法）
# __private_var           # 双下划线开头，有特殊含义


# case1
# # 输入身高（米）、体重（公斤）
# # 计算 BMI = 体重 / 身高²，保留 2 位小数
# # 用 if/elif/else 加一句判断：<18.5 偏瘦 / 18.5–24 正常 / ≥24 偏胖
# # 验收：输入 1.75 和 70 → 输出 BMI 22.86，正常
# # 提示：if bmi < 18.5: 这种写法，注意冒号和缩进 



try:
    height= float(input('输入身高（米）'))
    weight= float(input('输入体重（公斤）'))
    BMI = (weight/(height**2))

    if BMI < 18.5 :
        print(f"你的BMI指数是{BMI:.2f},偏瘦")
    elif BMI >= 18.5 and BMI <= 24 :
        print(f"你的BMI指数是{BMI:.2f},正常")
    else :
        print(f"你的BMI指数是{BMI:.2f},偏胖")
            
except ValueError:
    print("请输入数字！")

