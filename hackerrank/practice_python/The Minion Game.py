# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    stu, kev = 0, 0
    str_len = len(string)
    i = 0
    for c in string:
        if c in 'AEIOU':
            kev += str_len - i
        else:
            stu += str_len - i
        i += 1
    
    if stu > kev:
        print("Stuart {}".format(stu))
    elif stu < kev:
        print("Kevin {}".format(kev))
    else:
        print("Draw")
        
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
