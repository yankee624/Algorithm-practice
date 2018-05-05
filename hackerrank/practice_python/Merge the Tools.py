# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    for i in range(len(string)//k):
        t = string[i*k:(i+1)*k]
        u = []
        for c in t:
            if c not in u:
                u.append(c)
        print(''.join(u))
