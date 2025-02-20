import sys
def main():
    nums = list(map(int, input().split()))
    nums.sort()
    n = len(nums)

    prod1 = nums[n-1] * nums[n-2] * nums[n-3]
    prod2 = nums[0] * nums[1] * nums[n-1] 
    
    if prod2 > prod1:
        print(str(nums[0]) + " " + str(nums[1]) + " " + str(nums[n-1]))
    else:
        print(str(nums[n-3]) + " " + str(nums[n-2]) + " " + str(nums[n-1]))
   
    
if __name__ == '__main__':
    main()