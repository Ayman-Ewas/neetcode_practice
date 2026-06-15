class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct = set(nums)
        return not(len(distinct) == len(nums))