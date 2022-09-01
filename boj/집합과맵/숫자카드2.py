import sys

input = sys.stdin.readline

n = int(input().rstrip())
cards_a = list(map(int, input().split()))
cards_a_dict = dict()
for card in cards_a:
    try:
        cards_a_dict[card]+=1
    except:
        cards_a_dict[card]=1
m = int(input().rstrip())        
cards_b = list(map(int, input().split()))
for card in cards_b:
    try:
        print(cards_a_dict[card], end=" ")
    except:
        print(0, end=" ")