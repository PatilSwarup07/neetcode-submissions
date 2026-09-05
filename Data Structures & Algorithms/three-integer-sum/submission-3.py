class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        unique_res=[]
        nums.sort()

        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1

            while right>left:
                if nums[i]+nums[left]+nums[right]==0:
                    res.append([nums[i],nums[left],nums[right]])
                    right-=1

                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1

                else:
                    left+=1


        for i in res:
            if i not in unique_res:
                unique_res.append(i)

        return unique_res


