class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = defaultdict(int)
        result = []
        for n in nums:
            frequencyMap[n] += 1
        sortedMap = dict(sorted(frequencyMap.items(), key=lambda item: item[1], reverse=True))
        sortedMapKey = list(sortedMap.keys())

        return sortedMapKey[:k]