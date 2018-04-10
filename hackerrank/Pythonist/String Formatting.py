def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1,number+1):
        print("{num1:>{w}} {num2:>{w}o} {num3:>{w}X} {num4:>{w}b}".format(
                num1 = i, num2 = i, num3 = i, num4 = i, w = width)
            )
              
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
