n, m, k = map(int, input().split())     # 첫째 줄 입력
data = list(map(int, input().split()))  # 둘째 줄 입력
answer = 0      # 출력값 초기화

data.sort()     # 리스트 정렬 O(data)
f_max, s_max = data[-1], data[-2]   # 가장 큰 값과 두 번째 큰 값 O(1)

chunk, rest = m//(k+1), m%(k+1)     # chunk는 반복되는 뭉치, rest는 남은 수

'''
(반복 뭉치 * 최대 반복 수 * 가장 큰 값) 
+ (반복 뭉치 * 두 번째 큰 값) 
+ (남은 수 * 가장 큰 값)
'''
answer = (chunk*k*f_max) + (chunk*s_max) + (rest*f_max)

print(answer)
