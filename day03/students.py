# day03\students.py — 学生成绩表（今天最重要）
# 在代码里手写 6 个学生：

# python


# students = [
#     {"name": "张三", "class": "一班", "chinese": 88, "math": 95, "english": 76},
#     {"name": "李四", "class": "一班", "chinese": 92, "math": 78, "english": 85},
#     ...
# ]
# 要求：

# 每人算总分，把结果写回字典（新增 total 键）
# 按总分从高到低输出排名：1. 张三 总分 259
# 算每科的平均分（语文/数学/英语），保留 1 位小数
# 输出总分最高的那个人的姓名和总分
# 按班级分组，输出每个班的人数和班级平均总分
# 验收：

# 代码块


# 1. 张三 总分 259
# 2. ...
# ---
# 语文平均 86.5  数学平均 91.2  英语平均 80.3
# ---
# 总分最高：张三（259）
# ---
# 一班：3 人，平均总分 245.3
# 二班：3 人，平均总分 238.7

#1
# students = [
#     {"name": "张三", "class": "一班", "chinese": 88, "math": 95, "english": 76},
#     {"name": "李四", "class": "一班", "chinese": 92, "math": 78, "english": 85},
#     {"name": "王五", "class": "二班", "chinese": 100, "math": 20, "english": 70},
#     {"name": "赵六", "class": "二班", "chinese": 0, "math": 78, "english": 83},
#     {"name": "孙七", "class": "三班", "chinese": 76, "math": 76, "english": 45},
#     {"name": "李八", "class": "三班", "chinese": 98, "math": 37, "english": 36},
#     {"name": "郑九", "class": "三班", "chinese": 42, "math": 54, "english": 21},
# ]
# for n in students:
#     n['total'] = float(n['chinese']) + float(n['math']) + float(n['english'])
# max_point = students[0]
# chn_sum,mth_sum,eng_sum,total_sum = 0,0,0,0
# for i in students :
#     if i['total'] > max_point['total']:
#         max_point = i
#     chn_sum = chn_sum + i['chinese']
#     mth_sum = mth_sum + i['math']
#     eng_sum = eng_sum + i['english']
#     total_sum = total_sum + i['total']
# for m in students:
#     print(f"--------------------------\r\n| 姓名：{m['name']},总分：{m['total']} |")
# print(f"--------------------------\r\n年级语文平均分为：{chn_sum/len(students):.2f}  |\r\n年级数学平均分为：{mth_sum/len(students):.2f}  |\r\n年级英语平均分为：{eng_sum/len(students):.2f}  |\r\n年级的总平均分为：{total_sum/len(students):.2f} |\r\n--------------------------")
# print(f"总分最高:{max_point['name']}({max_point['total']})     |\r\n--------------------------")
# class_data,class_cnt = {},{}
# for n in students :
#     c = n['class']
#     if c not in class_data :
#         class_data[c] = 0
#         class_cnt[c] = 0
#     class_data[c] = class_data[c] + n['total']
#     class_cnt[c] = class_cnt[c] + 1
# for c, s in class_data.items():
#     print(f'{c}：{class_cnt[c]} 人，平均总分 {s / class_cnt[c]:.1f}')


#1028 D4使用推导式简化
students = [
    {"name": "张三", "class": "一班", "chinese": 88, "math": 95, "english": 76},
    {"name": "李四", "class": "一班", "chinese": 92, "math": 78, "english": 85},
    {"name": "王五", "class": "二班", "chinese": 100, "math": 20, "english": 70},
    {"name": "赵六", "class": "二班", "chinese": 0, "math": 78, "english": 83},
    {"name": "孙七", "class": "三班", "chinese": 76, "math": 76, "english": 45},
    {"name": "李八", "class": "三班", "chinese": 98, "math": 37, "english": 36},
    {"name": "郑九", "class": "三班", "chinese": 42, "math": 54, "english": 21},
]
# 1. 计算总分（保留原for循环，内部简化）
for n in students:
    n['total'] = sum(n[sub] for sub in ('chinese', 'math', 'english'))

# 2. 查最高分与求和（函数式写法）
max_point = max(students, key=lambda x: x['total'])
chn_sum = sum(s['chinese'] for s in students)
mth_sum = sum(s['math'] for s in students)
eng_sum = sum(s['english'] for s in students)
total_sum = sum(s['total'] for s in students)

# 3. 打印学生信息（保持原样）
for m in students:
    print(f"--------------------------\r\n| 姓名：{m['name']},总分：{m['total']} |")

# 4. 打印年级汇总（保持原样）
print(f"--------------------------\r\n年级语文平均分为：{chn_sum/len(students):.2f}  |\r\n年级数学平均分为：{mth_sum/len(students):.2f}  |\r\n年级英语平均分为：{eng_sum/len(students):.2f}  |\r\n年级的总平均分为：{total_sum/len(students):.2f} |\r\n--------------------------")
print(f"总分最高:{max_point['name']}({max_point['total']})     |\r\n--------------------------")

# 5. 班级统计（使用字典的 get 方法优化）
class_data, class_cnt = {}, {}
for n in students:
    c = n['class']
    class_data[c] = class_data.get(c, 0) + n['total']
    class_cnt[c] = class_cnt.get(c, 0) + 1

for c, s in class_data.items():
    print(f'{c}：{class_cnt[c]} 人，平均总分 {s / class_cnt[c]:.1f}')