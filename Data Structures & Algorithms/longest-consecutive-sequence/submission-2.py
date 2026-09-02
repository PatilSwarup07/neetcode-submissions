class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter=1
        nums=list(set(nums))
        nums.sort()
        current_max=1

        if len(nums)==0:
            return 0
        for i in range(0,len(nums)-1):
            if nums[i]+1==nums[i+1]:
                counter+=1    

            else:
                counter=1
                
            current_max=max(current_max,counter)
        return current_max
        