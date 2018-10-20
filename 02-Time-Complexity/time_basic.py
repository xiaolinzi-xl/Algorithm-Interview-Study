import time


def main():
    for i in range(1, 10):
        n = pow(i, 10)
        start_time = time.clock()

        sum_num = 0
        for j in range(0, n):
            sum_num += j

        end_time = time.clock()
        print("10^" + str(i) + ': ' + str((end_time - start_time)) + ' s')


if __name__ == '__main__':
    main()

'''
运行时间
0^1: 3.0000000000030003e-06 s
10^2: 4.900000000000043e-05 s
10^3: 0.0028909999999999977 s
10^4: 0.057761999999999994 s
10^5: 0.5172810000000001 s
10^6: 3.218291 s
10^7: 14.919568000000002 s
10^8: 56.788312999999995 s
10^9: 191.73284700000002 s
'''
