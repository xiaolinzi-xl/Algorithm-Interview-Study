class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 采用计数排序的思想
        count = [0, 0, 0]  # 存放0，1，2这三个元素的频率
        for ele in nums:
            assert 0 <= ele <= 2
            count[ele] += 1
        # nums[0:count[0]] = [0] * count[0]
        # nums[count[0]:count[0]+count[1]] = [1] * count[1]
        # nums[count[0]+count[1]:len(nums)] = [2] * count[2]

        index = 0
        for _ in range(0, count[0]):
            nums[index] = 0
            index += 1
        for _ in range(0, count[1]):
            nums[index] = 1
            index += 1
        for _ in range(0, count[2]):
            nums[index] = 2
            index += 1

    # 采用三路快排思想
    def sortColors_2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # [0,zero] = 0,[two,n-1] = 2,[zero+1,i) = 1
        zero, i, two = -1, 0, len(nums)
        while i < two:
            if nums[i] == 0:
                nums[zero+1], nums[i] = nums[i], nums[zero+1]
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[two-1], nums[i] = nums[i], nums[two-1]
                two -= 1


'''
计数排序：遍历数组两遍
时间复杂度：O(n) 
空间复杂度：O(k) k为元素的取值范围

三路快排：遍历数组一遍
时间复杂度：O(n)
空间复杂度：O(1)
'''


def main():
    nums = [2, 0, 2, 1, 1, 0]
    nums_2 = nums.copy()
    test = Solution()
    test.sortColors(nums)
    test.sortColors_2(nums_2)
    print(nums)
    print(nums_2)


if __name__ == '__main__':
    main()
