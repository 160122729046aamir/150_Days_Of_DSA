class Solution(object):
    def containsDuplicate(self, nums):
        nums1 = {i for i in nums}
        if len(nums)==len(nums1):
            return False
        else:
            return True
        
