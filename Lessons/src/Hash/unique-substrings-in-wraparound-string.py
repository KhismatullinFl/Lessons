class Solution(object):
    def findSubstringInWraproundString(self, s):
        
        max_len = [0] * 26
        current_max = 1
        
        s_nums = [ord(c) - ord('a') for c in s]
        
        for i in range(len(s_nums)):
            if i > 0 and (s_nums[i] - s_nums[i-1] == 1 or (s_nums[i-1] - s_nums[i]== 25)):
                current_max += 1
            else:
                current_max = 1
            
            idx = s_nums[i]
            max_len[idx] = max(max_len[idx], current_max)
        
        return sum(max_len)
        