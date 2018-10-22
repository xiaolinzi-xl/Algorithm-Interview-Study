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

    def moveZeroes_2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0  # [0,k) 全是非0元素
        # [k,i） 全为0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1


'''
时间复杂度：O(n)
空间复杂度：O(1)
'''


def main():
    test = Solution()
    arr = [0, 1, 0, 3, 12]
    arr2 = arr.copy()
    test.moveZeroes(arr)
    test.moveZeroes_2(arr2)
    print(arr)
    print(arr2)


if __name__ == '__main__':
    main()
