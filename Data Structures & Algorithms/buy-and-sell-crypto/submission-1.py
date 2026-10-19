class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxSuf=[0 for i in range(n)]

        m=0
        for i in range(n):
            maxSuf[n-i-1]=max(m, prices[n-i-1])
            m = max(m,prices[n-i-1])
        
        maxProf=0
        for i in range(n):
            maxProf= max(maxProf, maxSuf[i]-prices[i])

        return maxProf
