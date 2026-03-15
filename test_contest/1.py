import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    arr = []
    s = input()
    d = {
        "1": "a",
        "2": "b",
        "3": "c",
        "4": "d",
        "5": "e",
        "6": "f",
        "7": "g",
        "8": "h",
        "9": "i",
        "10#": "j",
        "11#": "k",
        "12#": "l",
        "13#": "m",
        "14#": "n",
        "15#": "o",
        "16#": "p",
        "17#": "q",
        "18#": "r",
        "19#": "s",
        "20#": "t",
        "21#": "u",
        "22#": "v",
        "23#": "w",
        "24#": "x",
        "25#": "y",
        "26#": "z",
    }
    i = 0
    while i < len(s):
        if i + 2 > len(s) - 1:
            arr.append(s[i])
            i += 1
        else:
            if s[i+2] == '#':
                arr.append(s[i:i+2] + '#')
                i += 3
            else:
                arr.append(s[i])
                i += 1
    return ''.join([d[i] for i in arr])


if __name__ == '__main__':
    print(main())
