class Solution(object):
    def searchInsert(self, nums, target):
            left = 0
            right = len(nums)-1
            while (left<=right):
                avg = (left + right)//2
                if(nums[avg]==target):
                    return avg
                if(nums[avg]<target):
                    left = avg+1
                else:
                    right = avg-1
            return left