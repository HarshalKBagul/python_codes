# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution:
    def twoSum(self, nums: list[int], target: int):
        
        dict_nums= {}
        
        for idx,num in enumerate(nums):
            dict_nums[num]= idx

        for idx,num in enumerate(nums):
            if target - num in dict_nums and idx != dict_nums[target-num]:
                return [idx,dict_nums[target-num]]