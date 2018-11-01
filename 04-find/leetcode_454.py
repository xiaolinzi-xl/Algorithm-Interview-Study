class Solution:
    @staticmethod
    def fourSumCount(A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        record = {}
        res = 0
        for c_ele in C:
            for d_ele in D:
                if c_ele + d_ele in record:
                    record[c_ele+d_ele] += 1
                else:
                    record[c_ele+d_ele] = 1

        for a_ele in A:
            for b_ele in B:
                if -a_ele-b_ele in record:
                    res += record[-a_ele-b_ele]

        return res


def main():
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(Solution.fourSumCount(A, B, C, D))


if __name__ == '__main__':
    main()
