# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    l = [0,1]
    if n >=0 and n<=2:
        return l[0:n]
    
    for _ in range(n-2):
        l.append(l[-2]+l[-1])
    return l
    
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
