class Solution:
    def getConcatenation(self, nums: List[int], loop=2) -> List[int]:
        ans = []
        for x in range(loop):
            for i in nums:
                ans.append(i)

        return ans