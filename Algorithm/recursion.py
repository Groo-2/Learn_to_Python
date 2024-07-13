# 순수한 재귀 함수 구현하기

def recur1(n: int) -> int:
    """순수한 재귀 함수 recur의 구현"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('정숫값을 입력하세요.: '))

recur1(x)

# 비재귀적으로 재귀 함수 구현하기(꼬리 재귀를 제거)

def recur2(n: int) -> int:
    """꼬리 재귀를 제거한 recur() 함수"""
    while n > 0:
        recur2(n - 1)
        print(n)
        n = n - 2

# 스택으로 재귀 함수 구현하기(재귀를 제거)

from fixed_stack import FixedStack # fixed_stack.py의 FixedStack 클래스를 임포트

def recur3(n: int) -> int:
    """재귀를 제거한 recur()함수"""
    s = FixedStack(n)

    while True:
        if n > 0:
            s.push(n) # n값을 push
            n = n - 1
            continue
        if not s.is_empty(): # 스택이 비어 있지 않으면
            n = s.pop() # 저장한 값을 n에 pop
            print(n)
            n = n - 2
            continue
        break