class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start=0
        # mid=len(nums)-k
        # for _ in range(k):
        #     nums[start],nums[mid]=nums[mid],nums[start]
        #     start+=1
        #     mid+=1

        # return nums

        for _ in range(k):
            value=nums.pop(-1)
            nums.insert(0,value)

        return nums

        