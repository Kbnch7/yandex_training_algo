import sys


def main():
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    print(' '.join([str(i) for i in sorted(list(set1 & set2))]))


if __name__ == '__main__':
    main()
