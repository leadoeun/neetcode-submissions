class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            numsum = numbers[i] + numbers[j]
            if numsum == target:
                return [i + 1, j + 1]
            elif numsum < target:
                i += 1
            elif numsum > target:
                j -= 1
        return None
        