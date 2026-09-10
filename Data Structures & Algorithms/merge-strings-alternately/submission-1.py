class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        
        n=min(n1,n2)
        N=max(n1,n2)
        
        if n2>=n1:
            Max=word2
            # Min=word1
        else:
            Max=word1
            # Min=word2

        # res=[]

        res_str=''
        for i in range(n):
            # res.append(word1[i])   
            res_str+=word1[i]   
            # res.append(word2[i])
            res_str+=word2[i]

        for i in range(n,N):
            res_str+=Max[i]


        return res_str




        