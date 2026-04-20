class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_to_set = set(nums)
        if len(list_to_set) == len(nums):
            return False
        else:
            return True