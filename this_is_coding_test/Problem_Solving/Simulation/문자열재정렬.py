import sys

input = sys.stdin.readline

letters = list(map(str, input().rstrip()))
letters.sort()
num_max_index = 0

for i in range(len(letters)):
    try:
        letters[i] = int(letters[i])
    except:
        num_max_index=i
        break
    
result = "".join(letters[num_max_index:])+str(sum(letters[:num_max_index]))

print(result)