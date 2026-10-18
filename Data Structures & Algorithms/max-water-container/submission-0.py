class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        j=n-1
        maxVol=-float('inf')
        while(i<j):
            maxVol=max(maxVol, min(heights[i],heights[j])*(j-i))
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return maxVol
