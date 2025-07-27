class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge=nums1+nums2
        merge.sort()
        mid=(0+len(merge))//2
        if len(merge)%2!=0:
            o=merge[mid]
            return o
        else:
            e=(merge[mid-1]+merge[mid])/2
            return e