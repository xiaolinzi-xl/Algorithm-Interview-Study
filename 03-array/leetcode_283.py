class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonzero_idx = 0  # [0,nonzero_idx) 全是非0元素
        for ele in nums:
            if ele != 0:
                nums[nonzero_idx] = ele
                nonzero_idx += 1
        for i in range(nonzero_idx, len(nums)):
            nums[i] = 0


'''
时间复杂度：O(n)
空间复杂度：O(1)
'''


def main():
    test = Solution()
    arr = [0, 1, 0, 3, 12]
    test.moveZeroes(arr)
    print(arr)


if __name__ == '__main__':
    main()
