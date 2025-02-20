class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x
        while (left<=right):
            avg = (left + right)//2
            if(avg*avg==x):
                return avg
            if(avg*avg<x):
                left = avg+1
            else:
                right = avg-1
        return left-1