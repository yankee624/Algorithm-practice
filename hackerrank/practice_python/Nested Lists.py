if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])

    l = sorted(l, key = lambda std: std[1])
    
    min_score = l[0][1]
    for i in range(len(l)):
        if l[i][1] != min_score:
            sec_min_score = l[i][1]
            break
    
    names = []
    for i in range(len(l)):
        if l[i][1] == sec_min_score:
            names.append(l[i][0])
            
    names.sort()
    for name in names:
        print(name)
