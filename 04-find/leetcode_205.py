class Solution:
    def judge(self, s, t):
        record = {}
        for i in range(len(s)):
            if s[i] in record:
                record[s[i]].append(i)
            else:
                record[s[i]] = [i]

        for k, v in record.items():
            if len(v) > 1:
                ele = t[v[0]]
                for index in v[1:]:
                    if t[index] != ele:
                        return False

        return True

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return self.judge(s,t) and self.judge(t,s)
        hashmap = {}
        ismap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in ismap:
                    return False
                hashmap[s[i]] = t[i]
                ismap[t[i]] = True
        return True
