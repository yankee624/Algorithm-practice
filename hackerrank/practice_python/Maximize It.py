# https://www.hackerrank.com/challenges/maximize-it/problem

import itertools

K, M = map(int, input().split())
L = []
for i in range(K):
    L.append(list(map(int, input().split()))[1:]) # first number indicates number of numbers

S = map(lambda x: sum(i**2 for i in x)%M, itertools.product(*L))
print(max(S))
