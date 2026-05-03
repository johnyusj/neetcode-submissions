class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_dict = {}
        comp = 0
        large_i = 0
        for i in range(0, len(nums)):
            comp = target - nums[i]
            large_i = i
            if (comp_dict.get(nums[i]) != None):
                break;
            else:
                comp_dict[comp] = i
        
        return [comp_dict.get(nums[i]), large_i]