class Solution:
    def twoSum(self, nums, res, l, mid, r):
        pass

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        record = set()
        for i in range(n):
            if nums[i] > target and nums[i] >= 0:
                break
            for j in range(i+1, n):
                tmp = nums[i] + nums[j]
                if tmp > target and nums[j] >= 0:
                    break
                l, r = j+1, n-1
                while l < r:
                    if nums[l] + nums[r] == target - tmp:
                        if (nums[i], nums[j], nums[l], nums[r]) not in record:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                            record.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > target - tmp:
                        r -= 1
                    else:
                        l += 1

        return res
