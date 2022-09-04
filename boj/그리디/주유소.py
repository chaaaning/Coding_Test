import sys

input = sys.stdin.readline

n = int(input().rstrip())
edges = list(map(int, input().split()))
gas_costs = list(map(int, input().split()))

idx_list = [i for i in range(n)]
visited = [False]*n
city_idx_list = list(map(lambda x,y: (x,y), gas_costs, idx_list))
city_idx_list.sort()

end_idx, total_cost = n, 0
while city_idx_list:
    cost, idx = city_idx_list.pop(0)
    if not visited[idx]:
        visited[idx:end_idx] = [True]*(end_idx-idx)
        if end_idx==-1 or idx-end_idx!=1:
            total_cost+=(sum(edges[idx:end_idx-1])*cost)
        else:
            total_cost+=(edges[idx]*cost)
        end_idx = idx+1
print(total_cost)