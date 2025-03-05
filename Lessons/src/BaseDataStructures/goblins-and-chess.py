import sys
from collections import deque

def main():
    privileged = deque()
    ordinary = deque()
    
    n = int(input())
    
    for i in range(n):
        s = input().split()
        if s[0] == '-':
            print(privileged.popleft())
        elif s[0] == '+':
            ordinary.append(s[1])
        else:
            ordinary.appendleft(s[1])
        if len(ordinary) > len(privileged):
            x = ordinary.popleft()
            privileged.append(x)

if __name__ == '__main__':
    main()