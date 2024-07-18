# 정렬을 마친 두 배열을 병합하기

from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
    pa, pb, pc = 0, 0, 0 # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c) # 각 배열의 원소 수

    while pa < na and pb < nb: # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= a[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1
    
    while pa < na: # a에 남은 원소를 c에 복사
        c[pc] = a[pa]
        pa += 1
        pc += 1
    
    while pb < nb: # b에 남은 원소를 c에 복사
        c[pc] = b[pb]
        pb += 1
        pc += 1