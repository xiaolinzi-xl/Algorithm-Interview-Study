class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        record = {}
        for ele in s:
            if ele in record:
                record[ele] += 1
            else:
                record[ele] = 1

        nums_map = {}
        for k, v in record.items():
            if v in nums_map:
                nums_map[v].append(k)
            else:
                nums_map[v] = [k]

        sort_index = sorted(nums_map, reverse=True)
        res = ''
        for index in sort_index:
            for ele in nums_map[index]:
                res += ele * index
        return res
