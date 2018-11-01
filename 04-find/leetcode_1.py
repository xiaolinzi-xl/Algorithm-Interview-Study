class Solution:
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 查找表
        # 不能将所有元素全放进去，这样相同元素会覆盖前面的索引
        # 将当前元素之前的元素放入查找表中进行查找
        nums_map = {}
        for i, ele in enumerate(nums):
            if target-ele in nums_map:
                return [nums_map[target-ele], i]
            else:
                nums_map[ele] = i


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution.twoSum(nums, target))


if __name__ == '__main__':
    main()
