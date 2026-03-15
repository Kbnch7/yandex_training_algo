import sys


def main():
    p, v = map(int, input().split())
    q, m = map(int, input().split())
    arr1 = [p - v, p + v] # -7, 7
    arr2 = [q - m, q + m] # 7, 17
    if arr2[0] <= arr1[1] <= arr2[1]:
        if arr2[0] <= arr1[0] <= arr2[1]:
            arr1 = []
        else:
            arr1[1] = arr2[0] - 1
    if arr1:
        if arr1[0] <= arr2[1] <= arr1[1]:
            if arr1[0] <= arr2[0] <= arr1[1]:
                arr2 = []
            else:
                arr2[1] = arr1[0] - 1

    res = 0
    if arr1:
        res += arr1[1] - arr1[0] + 1
    if arr2:
        res += arr2[1] - arr2[0] + 1
    print(res)


if __name__ == '__main__':
    main()

# -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 # 15

# 7 8 9 10 11 12 13 14 15 16 17 # 11