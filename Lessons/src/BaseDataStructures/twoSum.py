class Solution(object):
    def twoSum(nums, target):
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        for i in range(len(nums)):
            remainder = target - nums[i]
            if ((remainder in hash) and (hash[remainder]!=i)):
                return [i,hash[remainder]]
        return []