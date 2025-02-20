class Solution(object):
    def intersect(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        first = 0
        second = 0
        res=[]
        while(first<len(nums1) and second<len(nums2)):
            if (nums1[first]==nums2[second]):
                res.append(nums1[first])
                first+=1
                second+=1
            elif(nums1[first]<nums2[second]):
                first+=1
            else:
                second+=1
        return res