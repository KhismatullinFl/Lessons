import sys
def main():
    n = int(input())
    limit = list(map(int, input().split()))
    k = int(input())
    presses = list(map(int, input().split()))

    press_count = [0] * n

    for press in presses:
        press_count[press - 1] += 1

    for i in range(n):
        if press_count[i] > limit[i]:
            print("YES")
        else:
            print("NO")
if __name__ == '__main__':
    main()