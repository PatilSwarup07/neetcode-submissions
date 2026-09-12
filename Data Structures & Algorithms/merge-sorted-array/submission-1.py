class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # if m==0:
        #     nums1[:]=nums2[:]

        # index1=0
        # index2=0

        # for i in range(len(nums1)):
        #     if nums1[index1]>nums[index2]:
        #         nums

        for i in range(m,len(nums1)):
            nums1[i]=nums2[m-i]

        nums1.sort()

        