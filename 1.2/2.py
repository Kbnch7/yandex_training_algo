import sys


def main():
    arr = list(map(int, input().split()))
    lower0, greater0 = None, None
    max_multiply = float('-inf')
    numbers = []
    for i in arr:
        if i <= 0:
            if not lower0:
                lower0 = i
            else:
                if i*lower0 > max_multiply:
                    max_multiply = i*lower0
                    numbers = [i, lower0]
                if i <= lower0:
                    lower0 = i
        else:
            if not greater0:
                greater0 = i
            else:
                if i*greater0 > max_multiply:
                    max_multiply = i*greater0
                    numbers = [greater0, i]
                if i >= greater0:
                    greater0 = i
    if not numbers:
        print(*sorted(arr))
    else:
        print(*sorted(numbers))

if __name__ == '__main__':
    main()
