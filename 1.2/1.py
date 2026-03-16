import sys


def main():
    t1, t2 = map(int, input().split())
    mode = input()

    match mode:
        case "freeze":
            if t1 > t2:
                t1 = t2
        case "heat":
            if t1 < t2:
                t1 = t2
        case "auto":
            t1 = t2
    print(t1)

if __name__ == '__main__':
    main()
