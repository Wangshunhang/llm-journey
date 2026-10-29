# day03\wordcount.py — 词频 Top10
# 在代码里写死一段英文文本（3–5 句就够），然后：

# 全部转小写
# 按空格切词
# 去掉单词两边的标点（提示：word.strip(".,!?;:\"")）
# 用 dict 统计每个词出现次数
# 输出次数最多的前 10 个词，格式：1. the — 7 次
# 额外输出：一共有多少个不同的词（用 len(counts) 或 set）
# 验收：输出 10 行排名 + 一行"不同单词数：N"

# 加分：过滤掉 the / a / is 这类无意义的词（用一个 stop_words 列表）。



# # The morning sun filters gently through the oak leaves outside the window.
# A soft breeze carries the faint scent of fresh grass and wild clover.
# A small bird hops along the fence, tilting its head to watch the world.
# I pour a cup of warm tea and set it down on the wooden table.
# Steam rises slowly, curling into thin, invisible shapes in the air.
# Somewhere far away, a bicycle bell rings once and then fades.
# I open a notebook and pick up a well-worn black pen.
# There is no rush, no task that needs to be finished right now.
# Moments like this make quiet happiness feel easy to reach.
# I take a slow breath and simply enjoy this peaceful morning.


import re

aaa = '''The morning sun filters gently through the oak leaves outside the window.
A soft breeze carries the faint scent of fresh grass and wild clover.
A small bird hops along the fence, tilting its head to watch the world.
I pour a cup of warm tea and set it down on the wooden table.
Steam rises slowly, curling into thin, invisible shapes in the air.
Somewhere far away, a bicycle bell rings once and then fades.
I open a notebook and pick up a well-worn black pen.
There is no rush, no task that needs to be finished right now.
Moments like this make quiet happiness feel easy to reach.
I take a slow breath and simply enjoy this peacefu l morning.'''

bbb = re.sub(r'[^a-zA-Z\s]', '', aaa).lower().split()
dict_a = {}
for i in bbb :
    dict_a[i] = dict_a.get(i,0) + 1
stop_words = ['a', 'the','is']
for n in stop_words:
    if n in dict_a:
        del dict_a[n]
top = sorted(dict_a.items(), key=lambda kv: kv[1], reverse=True)[:10]
lenth_dict = len(dict_a)
for rank, (word, cnt) in enumerate(top, start=1):
    print(f'{rank}. {word} — {cnt} 次')
print(dict_a,f'不同的单词数为{lenth_dict}')