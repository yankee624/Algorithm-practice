# dealing with inputs, packing/unpacking with *

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    s = student_marks[query_name]
    avg = round(sum(s)/len(s),2)
    print('{0:.2f}'.format(avg))
