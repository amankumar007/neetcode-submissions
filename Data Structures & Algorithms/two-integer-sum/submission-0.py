class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        res=[]
        for i in range(len(nums)):
            if target-nums[i] in h:
                res.extend([h[target-nums[i]], i])
            h[nums[i]]=i
        return res