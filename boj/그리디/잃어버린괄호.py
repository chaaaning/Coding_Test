import sys

input = sys.stdin.readline
formula = input().rstrip()

m_split = formula.split("-")
mp_split = list(map(lambda x: x.split("+"), m_split))
base_num, diff_num = 0, 0
for i, val in enumerate(mp_split):
    if i==0:
        base_num += sum(map(lambda x: int(x), val))
    else:
        diff_num += sum(map(lambda x: int(x), val))

print(base_num - diff_num)