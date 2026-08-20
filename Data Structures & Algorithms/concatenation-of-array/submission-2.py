class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        duplicate=nums[:]
        
        for i in duplicate:
            nums.append(i)

        return nums
        

        