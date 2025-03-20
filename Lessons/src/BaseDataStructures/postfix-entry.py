import sys

def main():
    stack = []
    tokens = input().split(' ')

    for token in tokens:
        if token.isdigit():  
            stack.append(int(token))
        else:  
            b = stack.pop()  
            a = stack.pop() 

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)

    print(stack[0]) 

if __name__ == '__main__':
    main()