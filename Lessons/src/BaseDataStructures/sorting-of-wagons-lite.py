import sys

def main():
    n = int(input())
    wagons = list(map(int, input().split()))

    stack = []
    expected = 1
    for wagon in wagons:
        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1
        
        if wagon == expected:
            expected += 1
        else:
            stack.append(wagon)

    while stack:
        if stack.pop() != expected:
            print("NO")
            return
        expected += 1

    print("YES")

if __name__ == '__main__':
    main()