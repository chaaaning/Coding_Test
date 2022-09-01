import sys

input = sys.stdin.readline

n, m = map(int, input().split())

poketmon_book_dict, p_book = dict(), []
for i in range(n):
    pocketmon = input().rstrip()
    poketmon_book_dict[pocketmon] = i
    p_book.append(pocketmon)
    
result_list=[]

for _ in range(m):
    input_value = input().rstrip()
    try:
        input_value = int(input_value)
        result_list.append(p_book[input_value-1])
    except:
        result_list.append(poketmon_book_dict[input_value]+1)
for result in result_list:
    print(result)