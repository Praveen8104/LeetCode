class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a={}
        for i in nums:
            if i not in a.keys():
                a[i]=1
            else:
                return True
        return False

        '''if len((nums))==len(set(nums)):
            return False
        else:
            return True'''
