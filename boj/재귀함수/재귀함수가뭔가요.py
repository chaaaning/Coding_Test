import sys
import copy

input=sys.stdin.readline
n = int(input().rstrip())

s1 = '"재귀함수가 뭔가요?"'
s2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
s3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
s4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
s5 = '라고 답변하였지.'

def what_is_recursive(k):
    if k==n:
        print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
    for s in [s1,s2,s3,s4,s5]:
        if s != s5:
            if k==0:
                print("____"*(n-k)+s)
                print("____"*(n-k)+'"재귀함수는 자기 자신을 호출하는 함수라네"')
                print("____"*(n-k)+s5)
                return None
            else:
                print("____"*(n-k)+s)
        else:
            what_is_recursive(k-1)
            print("____"*(n-k)+s)

n_copy = copy.deepcopy(n)
what_is_recursive(n_copy)