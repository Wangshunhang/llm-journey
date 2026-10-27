# 每题先写普通循环版，再写推导式版，两版都跑出来对比结果：


#1 生成 1–20 的平方列表
squa1 = []
for i in range(1,21) :
    squa1.append(i ** 2)
print(squa1)

squa2 = [i ** 2 for i in range(1,21)]
print(squa2)

#2 生成 1–20 里能被 3 整除的数

division1 = []
for i in range(1,21) :
    if i % 3 == 0 :
        division1.append(i)
print(division1)

division2 = [i  for i in range(1,21) if i % 3 == 0 ]
print(division2)


#3 生成 1–20 里平方是偶数的数（提示：x*x % 2 == 0）
aaa1 = []
for i in range(1,21) :
    if i*i % 2 == 0 :
        aaa1.append(i)
print(aaa1)

aaa2 = [i for i in range(1,21) if i*i % 2 == 0]
print(aaa2)



#4 把 ["apple", "banana", "kiwi"] 转成大写和长度成对的字典：{'APPLE': 5, ...}
dicta = {}
aa = ["apple", "banana", "kiwi"] 
bb,cc = [],[]
for word in aa:
    bb.append(len(word))
    cc.append(word.upper())
for k,v in zip(cc,bb):  #方法1 笨办法
    dicta[k] =  v
dictb = dict(zip(cc,bb)) #方法2 直接用dict方法

#方法3 用推导式
dictc = {k:v for k,v in zip([word.upper() for word in aa],[len(word) for word in aa])}
print(dicta,dictb,dictc)

#好像发现了更优雅的写法
dicte = dict(zip((word.upper() for word in aa), (len(word) for word in aa)))
print(f"dicte:{dicte}")
#还可以更优雅,这是最简单的吗？
dictf = {word.upper(): len(word) for word in aa}
print(dictf)


#5 从 [1, 3, 3, 5, 5, 5, 7] 用 set 推导式去重
# 这个不行，直接用方法抄近道了 
# dd = set([1, 3, 3, 5, 5, 5, 7])
dd = {i for i in [1, 3, 3, 5, 5, 5, 7]}
print(dd)



#6 过滤出 students 里数学 ≥ 80 的姓名列表（自己造 5 个学生）

students = [
    {"name": "张三", "class": "一班", "chinese": 88, "math": 95, "english": 76},
    {"name": "李四", "class": "一班", "chinese": 92, "math": 78, "english": 85},
    {"name": "王五", "class": "二班", "chinese": 100, "math": 20, "english": 70},
    {"name": "赵六", "class": "二班", "chinese": 0, "math": 78, "english": 83},
    {"name": "孙七", "class": "三班", "chinese": 76, "math": 86, "english": 45},
    {"name": "李八", "class": "三班", "chinese": 98, "math": 37, "english": 36},
    {"name": "郑九", "class": "三班", "chinese": 42, "math": 94, "english": 21},
]

# 看错了，以为是输出集合
# ee = {}
# for i in students :
#     if i["math"] >= 80 :
#         c = i["name"]
#         d = str(i["math"])
#         for k,v in zip(c,d):
#             ee[c] = d
# print(ee)
#方法1
ee = []
for i in students :
    if i["math"] >= 80 :
        ee.append(i["name"])
print(ee)

#方法2 用推导式
ff = [i["name"] for i in students if i["math"] >= 80 ]
print(ff)

# 把所有学生的总分做成列表（用推导式 + sum，提示：sum(s["chinese"] + ... for ...) 或直接在表达式里写）
gg = []
for i in students :
    gg.append(sum([i["chinese"],i["math"],i["english"]])) #这里还不如不用sum，直接加起来呢
print(gg)

hh = [i["chinese"] + i["math"] + i["english"] for i in students]
print(hh)

# 用一行把 {"a": 1, "b": 2} 的值全部 ×100
print({k:v*100 for k,v in {"a": 1, "b": 2}.items()})