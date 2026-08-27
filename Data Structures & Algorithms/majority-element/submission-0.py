class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans_dict = {}

        for num in nums:
            if num in ans_dict:
                ans_dict[num] += 1
            else:
                ans_dict[num] = 1
        
        highest_num = max(ans_dict, key = ans_dict.get)
        return highest_num
