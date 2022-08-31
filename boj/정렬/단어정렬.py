import sys

input = sys.stdin.readline
n = int(input().rstrip())

words, visited = [], []
for _ in range(n):
    word = input().rstrip()
    if word not in visited:
        words.append((len(word), word))
        visited.append(word)
  
words.sort()

for length, word in words:
    print(word)