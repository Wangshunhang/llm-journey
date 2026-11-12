"""账本模型"""
import utils
import storage

class Record:
    """一条记账记录"""
    def __init__(self, id, date, type, category, amount, note=""):
        self.id = id
        self.date = date
        self.type = type
        self.category = category
        self.amount = amount
        self.note = note
        #self.records = [] 删掉 ！单条记录不需要这个列表

    def to_dict(self):
        """转成可以存进 JSON 的 dict"""
        d = {
            "id": self.id,
            "date": self.date,
            "type": self.type,
            "category": self.category,
            "amount": self.amount,
            "note": self.note,
        }
        return d  # 返回字典，不污染实例属性

    @classmethod
    def from_dict(cls, d):
        """从 JSON 的 dict 构造一个 Record 对象"""
        return cls(
            id=d["id"],                       # id 必须有，用 []
            date=d.get("date", ""),
            type=d.get("type", "1"),
            category=d.get("category", "未分类"),
            amount=d.get("amount", 0.0),
            note=d.get("note", "") # get容错，防止老json没有note字段
        )

    def __repr__(self):
        """打印时的样子，方便调试"""
        return  f"<Record id={self.id} {self.date} {self.type}/{self.category} ¥{self.amount} {self.note!r}>"



class Account:
    """一个账本"""
    def __init__(self, path=None):
        self.path = path if path is not None else storage.default_path
        self.records = []
        #实例化的时候会先执行init加载数据
        self.load()

    def load(self):
        """从文件读出 records"""
        raw_data = storage.load(self.path)
        #从 list[dict] 转成 list[Record]（对象化）
        self.records = [Record.from_dict(d) for d in raw_data]


    def save(self):
        """把 records 写回文件"""
        #要先把list[Record]对象实例化
        raw_data = [r.to_dict() for r in self.records] 
        storage.save(raw_data,path=self.path)
 

    def add(self, date, type, category, amount, note=""):
        """加一条记录，返回新建的 Record"""
        # 算新 id：next_id 需要 list[dict]，所以先转换
        raw_data = [r.to_dict() for r in self.records]
        new_id = utils.next_id(raw_data)

        # 造对象并加入列表
        new_record = Record(new_id, date, type, category, amount, note)
        self.records.append(new_record)

        # 落盘并返回
        self.save()
        return new_record

    def delete(self, record_id):
        """删除指定 id，成功返回 True，没找到返回 False"""
        for i, r in enumerate(self.records):
            if r.id == record_id:
                # 用 pop 根据索引删除，或者 del self.records[i]
                self.records.pop(i)
                self.save()
                return True
        return False

    def all(self):
        """返回所有记录"""
        return self.records.copy()       # 1\或者return list(self.records) 用list() 复制一份 2\或者用tuple: return tuple(self.records)

    def total(self):
        """返回 {'income': ..., 'expense': ..., 'balance': ...}"""
        income = sum(r.amount for r in self.records if r.type == "2")
        expense = sum(r.amount for r in self.records if r.type == "1")
        return {"income": income, "expense": expense, "balance": income - expense}
    
    def expense_by_category(self):
        """返回 {分类: 总金额}"""
        result = {}
        for r in self.records:
            if r.type == "1":
                result[r.category] = result.get(r.category, 0) + r.amount
        return result

# test begin
if __name__ == "__main__":
    import tempfile
    from pathlib import Path

    tmp = Path(tempfile.mkdtemp()) / "test.json"
    acc = Account(tmp)

    # 空账本
    assert acc.all() == []
    assert acc.total()["balance"] == 0

    # 加两条
    r1 = acc.add("2026-11-11", "1", "餐饮", 25.5, "午饭")
    r2 = acc.add("2026-11-11", "2", "工资", 13704, "十月")
    assert r1.id == 1
    assert r2.id == 2
    assert len(acc.all()) == 2

    # 新对象读同一个文件 —— 验证持久化
    acc2 = Account(tmp)
    assert len(acc2.all()) == 2
    assert acc2.all()[0].note == "午饭"

    # 汇总
    t = acc2.total()
    assert t["income"] == 13704
    assert t["expense"] == 25.5
    assert t["balance"] == 13704 - 25.5

    # 分类
    assert acc2.expense_by_category() == {"餐饮": 25.5}

    # 删除
    assert acc2.delete(1) is True
    assert acc2.delete(999) is False
    assert len(acc2.all()) == 1

    # 删后再加，id 不能撞
    r3 = acc2.add("2026-11-11", "1", "交通", 10)
    assert r3.id == 3          # ← max(2)+1 = 3，不是 len+1 = 2

    print("✅ models.py 全部测试通过")