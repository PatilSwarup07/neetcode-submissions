class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        left=0
        right=len(heights)-1
        while right>left:
            l=right-left
            b=min(heights[left],heights[right])

            area=max(area,l*b)

            if heights[left]>heights[right]:
                right-=1

            else:
                left+=1


        return area

        