import random


class Solution:

    def partition(self, nums, l, r):
        swap_index = random.randint(l, r)
        nums[l], nums[swap_index] = nums[swap_index], nums[l]

        # nums[l+1,k] < v,nums[k+1,r] >= v
        k = l
        for i in range(l + 1, r + 1):
            if nums[i] < nums[l]:
                k += 1
                nums[k], nums[i] = nums[i], nums[k]
        nums[k], nums[l] = nums[l], nums[k]
        return k

    def find(self, nums, l, r, index):
        point = self.partition(nums, l, r)
        if point == index:
            return nums[point]
        elif point < index:
            return self.find(nums, point + 1, r, index)
        else:
            return self.find(nums, l, point - 1, index)

    def findKthLargest(self, nums, k):
        assert 1 <= k <= len(nums), 'k 不在合法范围'
        index = len(nums) - k
        return self.find(nums, 0, len(nums) - 1, index)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))
