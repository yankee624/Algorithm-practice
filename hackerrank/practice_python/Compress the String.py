# https://www.hackerrank.com/challenges/compress-the-string/problem

import itertools

s = input()
for i,j in itertools.groupby(s):
     print('({0}, {1})'.format(len(list(j)),i),end=' ')
