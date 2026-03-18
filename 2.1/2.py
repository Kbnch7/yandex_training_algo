import sys


def main():
    arr = list(map(int, input().split()))
    my_set = set()
    for i in arr:
        if i in my_set:
            print("YES")
        else:
            print("NO")
            my_set.add(i)


if __name__ == '__main__':
    main()
