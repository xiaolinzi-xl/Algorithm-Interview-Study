class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        record = {}
        res = []
        for ele in strs:
            tmp = 1
            for char in ele:
                tmp *= ord(char) * (ord(char) - ord('a') + 1)
            if tmp in record:
                record[tmp].append(ele)
            else:
                record[tmp] = [ele]

        for v in record.values():
            res.append(v)

        return res
