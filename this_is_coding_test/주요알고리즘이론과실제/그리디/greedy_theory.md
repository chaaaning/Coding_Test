# Greedy

**INDEX**
- [개요](#개요)
- [주의해야 할 사항](#주의해야-할-사항)
---

## 개요

- 그리디 알고리즘은 단순하지만 강력한 문제 해결 방법이다. 해당 알고리즘은 `현재 상황에서 지금 당장 좋은 것만 고르는 방법`으로, 그리디 알고리즘을 이용하면 매 순간 가장 좋아 보이는 것을 선택하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다. 그리디 알고리즘은 사전에 외우고 있지 않아도 풀 수 있을 가능성이 높은 문제 유형이라는 특징이 있다. 이후 공부할 정렬, 최단 경로 등의 알고리즘 유형은 이미 그 알고리즘의 사용 방법을 정확히 알고 있어야만 해결 가능한 경우가 많다.

    > 예를 들어 여러 개의 데이터를 빠르게 정렬해야 하는 문제는 정렬 라이브러리의 사용 방법을 알고 있어야 한다. 또 다른 예시로 최단 경로를 빠르게 찾아야 하는 문제는 플로이드 워셜 또는 다익스트라 알고리즘과 같은 특정 알고리즘을 미리 알고 있거나 팀 노트를 통해 준비해야 풀 수 있다. 

- 보통 코딩 테스트에서 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구한다. 즉, 특정 문제를 만났을 대 단순히 현재 상황에서 가장 좋아 보이는 것만을 선택해도 문제를 풀 수 있는지를 파아가할 수 있어야 한다.

- 그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘이므로 문제에서 `가장 큰 순서대로`, `가장 작은 순서대로`와 같은 기준을 알게 모르게 제시한다. 대체로 이 기준은 정렬 알고리즘을 사용했을 때 만족시킬 수 있으므로 그리디 알고리즘 문제는 자주 정렬 알고리즘과 짝을 이뤄 출제된다.

## 주의해야 할 사항

- 그리디 알고리즘에서는 문제 풀이를 위한 최소 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 답을 도출할수 있다. 어떠한 코딩 테스트 문제에서 바로 문제 유형을 파악하기 어렵다면 그리디 알고리즘을 의심하고, 문제를 해결할 수 있는 탐욕적인 해결법이 존재하는지 고민해 보아야 한다. 만약 그리디 알고리즘으로 해결할 수 없다면 이후 다이나믹 프로그래밍이나 그래프 알고리즘으로 문제를 해결할 수 있는지 고민해 보는 것도 좋은 방법이다.
