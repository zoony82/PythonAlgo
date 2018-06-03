# -*- coding: utf-8 -*-
import numpy

print('순차 탐색')
def search_list(a, x):
    n = len(a)
    for i in range(0,n):
        if a[i] == x:
            return i
    return -1

v = [17, 92, 18, 33, 7, 33, 42]
print(type(v))
print(search_list(v,18))

print('선택 정렬')
def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        #찾은 최솟값을 i번 위치로
        a[i], a[min_idx] = a[min_idx], a[i]
d = [2,4,5,1,3]
sel_sort(d)
print(d)

print('삽입 정렬')
def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >=0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

d = [2,4,5,1,3]
ins_sort(d)
print(d)

print('병합 정렬')
def merge_sort(p_a):
    n = len(p_a)
    if n <= 1:
        return

    mid = n // 2
    g1 = p_a[:mid]
    #print(g1)
    g2 = p_a[mid:]
    #print(g2)
    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0
    # 두 그룹을 하나로 병합
    #rint('병합 시작 p_a', p_a, 'g1', g1, 'g2', g2)
    while i1 < len(g1) and i2 < len(g2):
        #print('while', i1, i2, ia, len(g1), len(g2))
        if g1[i1] < g2[i2]:
            p_a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            p_a[ia] = g2[i2]
            i2 += 1
            ia += 1
    #print ('1단계 종료 p_a', p_a, 'g1', g1, 'g2', g2)
    #아직 남아 있는 자료들을 결과에 추가
    while i1 < len(g1):
        #print('남아있는 자료 추가 i1 g1',i1, g1)
        p_a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        #print('남아있는 자료 추가 i2 g2',i1, g2)
        p_a[ia] = g2[i2]
        i2 += 1
        ia += 1

d = [6,8,3,9,10,1,2,4,7,5]
merge_sort(d)
print(d)


print("퀵 정렬")

def quick_sort_sub(ap, start, end):
    #종료조건 : 정렬 대상이 한 개 이하이면 정렬할 필요가 없음
    print('step 1',ap, start, end)
    if end - start <= 0:
        return
    #기준값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤
    #[기준 값보다 작은 값들, 기준 값보다 큰 값들]
    pivot = ap[end] # 편의상 리스트의 마지막 값을 기준 값으로 정함
    i = start
    for j in range(start, end):
        if ap[j] <= pivot:
            print('if ap[j] <= pivot:', pivot, i, j, ap[i], ap[j] )
            ap[i], ap[j] = ap[j], ap[i]
            i += 1
    ap[i], ap[end] = ap[end], ap[i]

    print('quick_sort_sub 1 :',ap, start, i-i)
    quick_sort_sub(ap, start, i - 1) #기준 값보다 작은 그룹을 재귀호출로 다시 정렬
    print('quick_sort_sub 2 :', ap, i+1, end)
    quick_sort_sub(ap, i + 1, end) # 기준 값보다 큰 값을 재귀 호출로 다시 정렬

def quick_sort(a):
    print('quick_sort_sub 1st', a, 0, len(a) - 1)
    quick_sort_sub(a, 0, len(a) - 1)

d = [6,8,3,9,10,1,2,4,7,5]
quick_sort(d)
print(d)