class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for x in nums:
            counts[x] +=1

        colors = [0, 1, 2]
        i = 0
        for x in colors:
            for y in range(counts[x]):
                nums[i] = x
                i += 1
