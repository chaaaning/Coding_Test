# Binary Search (이진 탐색)

**INDEX**

- [순차 탐색](#순차-탐색)
- [이진 탐색](#이진-탐색)
- [트리 자료구조](#트리-자료구조)
- [이진 탐색 트리](#이진-탐색-트리)
---

## 순차 탐색

- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

- 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.

- 리스트 내에 데이터가 아무리 많아도 시간이 충분하다면 항상 원하는 원소를 찾을 수 있다.

```python
def sequential_search(n, target, array):
    for i in range(n):
        if array[i]==target:
            return i+1
```

## 이진 탐색

- 시작점, 끝점, 중간점을 사용하여 차증려는 데이터와 중간점 위치에 있는 데이터를 반복저으로 비교해 원하는 데이터를 찾는 과정 (단 정렬된 상태에서 사용 가능)

- 재귀로 구현한 이진 탐색
    ```python
    def binary_search(arr, target, start, end):
        if start > end:
            return None

        mid = (start+end)//2
        
        if arr[mid] == target: return mid
        elif arr[mid] > target: 
            return binary_search(arr,target, start, mid-1)
        else:
            return binary_search(arr, target, mid+1, end)
    ```

- loop로 구현한 이진 탐색
    ```python
    def binary_search(arr, target, start, end):
        while True:
            if start > end: break

            mid = (start+end)//2

            if arr[mid]==target: return mid
            elif arr[mid] > target: end = mid-1
            else: start = mid+1
    ```

## 트리 자료구조

- 이진 탐색은 전제 조건이 데이터 정렬이다. 즉, 동작 프로그램에서 데이터를 정렬해두는 경우에 이진 탐색을 효과적으로 사용할 수 있다. 트리 자료구조의 경우 항상 데이터가 정렬되어 있으므로 이진 탐색을 유용하게 적용할 수 있다.

- 노드와 노드의 연결로 표현하며 노드는 정보의 단위로 어떠한 정보를 가지고 있는 개체로 이해할 수 있다.

- 트리 자료구조는 그래프 자료구조의 일종으로 데이터베이스 시스템이나 파일 시스템과 같은 곳에서 많은 양의 데이터를 관리하기 위한 목적으로 사용한다.

- 트리자료 구조의 특징
    - 부모 노드와 자식 노드의 관계로 표현
    - 최상단 노드를 루트 노드라고 함
    - 최하단 노드를 단말 노드라고 함
    - 일부를 떼어내도 트리 구조이며 이를 서브 트리라 함
    - 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합

## 이진 탐색 트리

- 트리 자료구조 중 가장 간단한 형태로 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다.

- 이진 탐색 트리의 특징
    - 부모 노드보다 왼쪽 자식 노드가 작다
    - 부모 노드보다 오른쪽 자식 노드가 크다