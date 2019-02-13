import time

# 递归解决


def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)


memo = []


def fib_2(n):
    if n == 0:
        return 0

    if n == 1:
        return 1
    # 采用记忆化搜索
    if memo[n] == -1:
        memo[n] = fib_2(n-1) + fib_2(n-2)

    return memo[n]


# 自下而上的解决，递归是自上而下解决
def fib_3(n):
    memory = [-1] * (n+1)

    memory[0] = 0
    memory[1] = 1

    for i in range(2, n+1):
        memory[i] = memory[i-1] + memory[i-2]

    return memory[n]


if __name__ == "__main__":
    n = 10
    start_time = time.clock()
    res = fib(n)
    end_time = time.clock()

    print('fib(' + str(n) + ') = ' + str(res))
    print(str(end_time - start_time) + 's')
    print('------------------')

    n = 500
    memo = [-1] * (n+1)

    start_time = time.clock()
    res = fib_2(n)
    end_time = time.clock()
    print('fib(' + str(n) + ') = ' + str(res))
    print(str(end_time - start_time) + 's')
    print('------------------')

    start_time = time.clock()
    res = fib_3(n)
    end_time = time.clock()
    print('fib(' + str(n) + ') = ' + str(res))
    print(str(end_time - start_time) + 's')

# 递归问题 --- 重叠子问题 --- 记忆化搜索（自顶向下解决） --- 动态规划（自下而上解决）
