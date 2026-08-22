class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # Dictionary to store: { number: index }
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # Check if the needed number has already been seen
            if complement in seen:
                return [seen[complement], index]
            
            # Otherwise, remember this number and its position
            seen[num] = index
        return []
        
        