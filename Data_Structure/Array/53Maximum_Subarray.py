"""Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array."""

#Brute force
#time: O(n2)
#space: O(1)
nums = [-2,1,-3,4,-1,2,1,-5,4]
sums = []
for i in range(len(nums)):
    for j in range(len(nums)+1):
        sums.append(sum(nums[i:j]))

max(sums)

#Better Brute force

nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = 0

if max(nums) < 0:
    max_sum = max(nums) #deal with situation when the list contains only negativee number(s)
for i in range(len(nums)):
    if nums[i] > 0:
        for j in range(i+1,len(nums)+1):
            if sum(nums[i:j]) < 0:
                break
            elif sum(nums[i:j]) > max_sum:
                max_sum = sum(nums[i:j])
max_sum
