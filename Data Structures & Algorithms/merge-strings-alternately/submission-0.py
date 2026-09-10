class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        
        n=min(n1,n2)
        N=max(n1,n2)
        res=[]

        if n2>n1:
            Max=word2
        else:
            Max=word1

        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])


        if N>n:
            for i in range(n,N):
                res.append(Max[i])
        
        res_str=''
        for i in res:
            res_str+=i

        return res_str

