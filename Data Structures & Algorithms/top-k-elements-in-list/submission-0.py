class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for x in nums:
            counts[x] += 1
        
        frequency = [[] for _ in range(len(nums) + 1)]

        for x, freq in counts.items():
            frequency[freq].append(x)
        
        results = []

        for freq in range(len(nums), 0, -1):
            for x in frequency[freq]:
                results.append(x)
                if len(results) == k:
                    return results
