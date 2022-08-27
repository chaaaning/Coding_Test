import sys

input = sys.stdin.readline
s = input().rstrip()

alphabet_list = [-1]*26

for i in range(26):
    mod_i = 97+i
    for j in range(len(s)):
        if chr(mod_i)==s[j]:
            alphabet_list[i] = j
            break

for alphabet in alphabet_list:
    print(alphabet, end=" ")