class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup=set()
        for i in range(len(nums)):
            if nums[i] in dedup:
                return True
            dedup.add(nums[i])

        return False
        