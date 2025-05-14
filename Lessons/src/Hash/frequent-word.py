import sys

def main():
    text = sys.stdin.read()
    words = text.split()
    frequent = {}

    for word in words:
        if word in frequent:
            frequent[word] += 1
        else:
            frequent[word] = 1
    
    mf = max(frequent.values()) if frequent else 0
    cw = [word for word, count in frequent.items() if count == mf]
    
    if cw:
        result = min(cw)
    else:
        result = ""

    print(result)

if __name__ == '__main__':
    main()
