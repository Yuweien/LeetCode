class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #slower
        p = 0
        for p in range(len(nums)):
            if (target - nums[p]) in nums[p+1:]:
                return [p, nums[p+1:].index((target-nums[p]))+p+1]


        #faster
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]] = i
