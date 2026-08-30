class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        hashtable=dict()
        count=0
        value=nums[0]

        for key in nums:
            if key!=value:
                count=1
                value=key
            else:
                count+=1

            hashtable[key]=count

        hashtable=dict(sorted(hashtable.items(),key=lambda item:item[1],reverse=True))

        res=list(hashtable.keys())

        res=res[:k]
        return res

        


        







        