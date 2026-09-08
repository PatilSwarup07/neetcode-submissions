class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write=0
        for read in range(len(nums)-1):
            if nums[read]!=nums[read+1]:
                write+=1
                nums[write]=nums[read+1]

        return write+1
        

        