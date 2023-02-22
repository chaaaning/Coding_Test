import sys

input = sys.stdin.readline

S = input().rstrip()
q = int(input())

graph = [[] for _ in range(26)]
dp = [[] for _ in range(26)]
for i, s in enumerate(S):
    idx = ord(s)-97
    graph[idx].append(i)
    if not dp[idx]:
        dp[idx]+=[0]*i
        dp[idx]+=[1]
        continue

    dp[idx]+=[dp[idx][-1]]*(i-graph[idx][-2]-1)
    dp[idx]+=[dp[idx][-1]+1]

result = []

for _ in range(q):
    target, s, e = input().split()
    start, end = int(s), int(e)
    t_idx = ord(target)-97
    if not dp[t_idx]:
        result.append(0)
        continue

    if start!=0:
        try:
            result.append(dp[t_idx][end]-dp[t_idx][start-1])
        except:
            try:
                result.append(dp[t_idx][-1]-dp[t_idx][start-1])
            except:
                result.append(0)
    else:
        try:
            result.append(dp[t_idx][end])
        except:
            result.append(dp[t_idx][-1])
        
for r in result:
    print(r)
    
# for i, d in enumerate(dp):
#     print(f"{chr(i+97)} : {d}")
