import sys


def main():
    n = int(input())
    teams = list(map(int, input().split()))
    if n == 1:
        print(1)
        return
    curr_capital = teams[0]
    prev_team = teams[0]
    last_looser = 1
    for i in range(1, len(teams)-1):
        # может ли компания захватить кого-то из предыдущих ? (если нет, то она не сможет выиграть вообще)
        if teams[i] <= teams[i-1] and teams[i] <= prev_team:
            last_looser = i + 1
            curr_capital += teams[i]
        else:
            curr_capital += teams[i]
            # может ли компания захватить следующую компанию при условии, что захватит все предыдущие ? (если нет, то она и не сможет выиграть вообще))
            if curr_capital <= teams[i+1]:
                last_looser = i + 1
            if i > 1 and teams[i] != teams[i-1]:
                prev_team = teams[i-1]
    if teams[-1] <= teams[-2] and teams[-1] <= prev_team:
        last_looser += 1

    # выводим компании так, что победить могут только компании, вышестоящие которых могут захватить компанию выше
    for i in range(last_looser):
        print(0)
    for i in range(n - last_looser):
        print(1)

if __name__ == '__main__':
    main()
