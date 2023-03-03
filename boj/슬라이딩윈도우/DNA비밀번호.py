import sys

input = sys.stdin.readline

S, P = map(int, input().split())
L_DNA = input().rstrip()
conditions = list(map(int, input().split()))

dc = {"A":0, "C":1, "G":2, "T":3}
cur_dna = [0]*4

count=0

for i, l in enumerate(L_DNA):
    cur_dna[dc[l]]+=1
    if i<P-1:
        continue
    elif i!=P-1:
        cur_dna[dc[L_DNA[i-P]]]-=1
    if all(list(map(lambda x1, x2: x1>=x2, cur_dna, conditions))):
        count+=1
        
print(count)