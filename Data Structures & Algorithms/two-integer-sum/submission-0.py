class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)

        for i in range(0,n):
            remain = target - nums[i]
            if remain in hash_map:
                return [hash_map[remain],i]
            hash_map[nums[i]] = i
        