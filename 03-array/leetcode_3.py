class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 256
        # 滑动窗口 s[l,r] 中无重复字符
        l, r = 0, -1
        res = 0
        while l < len(s):
            if r+1 < len(s) and freq[ord(s[r+1])] == 0:
                r += 1
                freq[ord(s[r])] = 1
            else:
                res = max(r-l+1, res)
                freq[ord(s[l])] = 0
                l += 1
        return res


def main():
    s = 'pwwke'
    print(Solution.lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()
