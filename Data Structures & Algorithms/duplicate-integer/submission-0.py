class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dic = {}
        for i in range(0, len(nums)):
            if(dup_dic.get(nums[i]) != None):
                return True
            else:
                dup_dic[nums[i]] = i

        return False 
