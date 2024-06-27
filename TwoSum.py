class Solution(object):
    def twoSum(self, nums, target):
        # declare a hashmap 
        nums_map = {} 
        # fill hashmap with the given numbers and their indices
        for i in range(len(nums)):
            num = nums[i]
            # check if current num and existing num in hashmap add up to target
            if target - num in nums_map:
                return[i, nums_map[target - num]]
            nums_map[num] = i
