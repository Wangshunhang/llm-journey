# 负责读写 JSON 文件
#     ...
# 要求：

# load 遇到文件不存在 → 返回 []，不报错
# load 遇到内容损坏 → 打印警告，返回 []
# save 自动建 data/ 目录
# 两个函数都有 docstring
# Path(__file__).parent = “当前文件所在目录”。用它，不要用相对路径 "data/..."——相对路径依赖你在哪运行，是个坑。
from pathlib import Path
import json

default_path = Path(__file__).parent/"data"/"records.json"


def load(path=default_path):
    """读取记录列表；文件不存在或损坏时返回 []"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []                      # 首次运行正常
    except json.JSONDecodeError:
        print(f"⚠️ 文件已损坏：{path}")  # 损坏要告诉用户
        return []
    # else :
    #     print('文件读取成功')
    # finally :
    #     print("无论成败都执行")        # 清理现场（关文件、断连接）   

def save(records, path=default_path):
    """保存记录列表，自动创建目录"""
    path.parent.mkdir(parents=True,exist_ok=True)
    with open(path,"w",encoding='utf-8') as f :
        json.dump(records,f,ensure_ascii = False,indent=2)

