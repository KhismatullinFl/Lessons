from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result = []
        queue = deque()  
        for i in range(len(nums)):
            if queue and queue[0] < i - k + 1:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)
            if i >= k - 1:
                result.append(nums[queue[0]])  

        return result

