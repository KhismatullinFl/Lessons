import sys

def main():
    s = input()
    stack = []
    for i in s:
        if (i=='(' or i=='[' or i=='{'):
            stack.append(i)
        else:
            if(len(stack)!=0):
                if(stack[-1]=='(' and i==')'):
                    stack.pop()
                    continue
                if(stack[-1]=='[' and i==']'):
                    stack.pop()
                    continue
                if(stack[-1]=='{' and i=='}'):
                    stack.pop()
                    continue
                print('no')
                return
            else:
                print('no')
                return
    if(len(stack)!=0):
        print('no')
        return
    print('yes')

if __name__ == '__main__':
    main()