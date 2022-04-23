# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution:
    def twoSum(nums,target):
        complementMap = dict()
        for i in range(len(nums)):
            num=nums[i]
            complement=target-num
            if num in complementMap:
                return [complementMap[num],i]
            else:
                complementMap[complement] = i

obj=Solution

obj.twoSum([1,2,3,4,5],4)