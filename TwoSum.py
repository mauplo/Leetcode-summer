"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

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
