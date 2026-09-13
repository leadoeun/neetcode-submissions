class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        if nums.count(0) > 1:
            return [0] * len(nums)
        elif 0 in nums:
            product = 1
            for n in nums:
                if n != 0:
                    product *= n
            result = [0] * len(nums)
            result[nums.index(0)] = product
        else: 
            product = 1
            for n in nums:
                product *= n
            for n in nums: 
                result.append(int(product / n))
        return result
        