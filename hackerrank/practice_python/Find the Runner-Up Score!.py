if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(arr)
    l.sort()
    max = l[-1]
    max_n = l.count(max)
    if max_n == len(l):
        print(None)
    else:
        print(l[-1-max_n])
