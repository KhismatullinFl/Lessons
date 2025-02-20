import sys
def main():
    n, l = map(int, input().split())
    nums = []
    for _ in range(n):
        nums.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(i + 1, n):
            merged_nums = nums[i] + nums[j]
            merged_nums.sort()
            print(merged_nums[l - 1])

if __name__ == '__main__':
    main()