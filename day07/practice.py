from pathlib import Path
p = Path("data")/"record.json"
print(p)
p.parent.mkdir(parents=True,exist_ok=True)
# p.parent.mkdir(parents=True, exist_ok=True) 的作用是创建父目录（即 data 文件夹）。
# exist_ok=True 的作用是：如果 data 文件夹已经存在，就不报错，直接跳过。
p.exists
print(p.read_text(encoding="utf-8") )        # 读（一步到位）
print(p.write_text("aaba", encoding="utf-8") ) # 覆盖写



# 在 Python 中，json 模块主要负责 Python 对象（如字典、列表） 与 JSON 格式字符串 之间的互相转换，以及文件的读写。
# 这里有一个极其重要的规律：带 s 的方法处理字符串（String），不带 s 的处理文件（Stream/File)
import json


aaa = '{"name": "张三", "age": 18, "is_student": true}'
bbb = json.loads(aaa)   #从字符串取，把 JSON 格式的字符串，变成 Python 的字典或列表.load str--dict/list(load读 成字典)
print(f"bbb = {bbb}")

data = {"name": "张三", "age": 18}
json_str = json.dumps(data,ensure_ascii=False,indent=4)  #dump dict/list--str（dump 写成str）

#  ensure_ascii=False  默认认情况下，JSON 会把中文转成 \uXXXX 的 Unicode 编码。加上这个参数，中文就能原样保留
# indent = 4 默认输出的 JSON 是一整行，挤在一起没法看。加上 indent 可以让它换行并缩进（通常用 2 或 4）
print(type(json_str)) # <class 'str'>
print(json_str) # {"name": "\u5f20\u4e09", "age": 18}

# 避坑指南
# JSON 里的布尔值：Python 里是 True / False，JSON 里是 true / false（小写）。用 json.loads() 转换时会自动对应，但如果你手写 JSON 字符串，千万别写成大写，否则报错。

# 不支持的数据类型：JSON 只能存基本数据类型（字典、列表、字符串、数字、布尔、None）。如果你把一个 Python 的 datetime 时间对象或者 set 集合塞进去，会直接报错 TypeError。必须先用 str() 转成字符串。

# 单引号问题：标准的 JSON 只认双引号 ""。如果你手动拼了一个 {'name': '张三'}（单引号），用 json.loads() 解析会直接报错。必须写成 {"name": "张三"}


with open("x.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


with open("x.json", "r", encoding="utf-8") as f:
    data2 = json.load(f)
print(type(data2))


try:
    with open("x.json", "r", encoding="utf-8") as f:
        data3 = json.load(f)          # 可能出错的
except FileNotFoundError:
    data3 = []                    # 文件不存在 → 当作空数据
except json.JSONDecodeError:
    print("文件内容损坏")
    data3 = []
else:
    print("读取成功")             # try 里没出错才执行
finally:
    print("无论成败都执行")        # 清理现场（关文件、断连接）