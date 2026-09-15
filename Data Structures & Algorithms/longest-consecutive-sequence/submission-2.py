class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums) 
        consecdict = dict()
        for n in numset:
            if n-1 not in numset:
                consecdict[n] = [n]
        print(consecdict)
# find largest start smaller than n 
        for n in numset:
            max_k = min(consecdict.keys())
            if n not in consecdict.keys():
                for k in consecdict.keys():
                    if k > n: continue
                    elif k > max_k:
                        max_k = k
                consecdict[max_k].append(n)
        
        max_val = 0
        for val in consecdict.values():
            if len(val) > max_val:
                max_val = len(val)
        return max_val
            