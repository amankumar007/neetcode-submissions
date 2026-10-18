class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)

        p=1
        s=1
        prod=[1 for i in range(n)]
        for i in range(n):
            prod[i]*=p
            prod[n-i-1]*=s

            p*=nums[i]
            s*=nums[n-i-1]

        return prod