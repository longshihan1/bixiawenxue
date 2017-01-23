from collections import deque

#划分无冲突子集
def division(m, n):
    """
    :param m: 冲突关系矩阵
    :param n: 几种动物
    :return: 返回一个栈，栈内包含了所有的笼子
    """
    res = []  # 创建一个栈
    q = deque(range(n))  # 初始化队列，里面放着动物的序号
    pre = n  # 前一个动物的下标

    while q:
        cur = q.popleft()  # 从队头出队一个动物
        if pre >= cur:  # 是否需要创建笼子
            res.append([])  # 创建一个笼子
        # 当前的动物是否与笼子内的动物有冲突
        for a in res[-1]:  # 迭代栈中最顶层的笼子
            if m[cur][a]:  # 有冲突
                q.append(cur)  # 重新放入队列的尾部
                break
        else:  # 当前动物和当前笼子中的所有动物没冲突
            res[-1].append(cur)  # 当前动物放入最上面的笼子中
        pre = cur  # 当前变成之前的
    return res



if __name__ == '__main__':
    N = 9
    R = {  # 冲突对应关系表
        (1, 4), (4, 8), (1, 8), (1, 7),
        (8, 3), (1, 0), (0, 5), (1, 5),
        (3, 4), (5, 6), (5, 2), (6, 2), (6, 4),
    }

    M = [[0] * N for _ in range(N)]  # 冲洗关系矩阵M，0代表不冲突
    for i, j in R:
        M[i][j] = M[j][i] = 1  # 1代表冲突

    result = division(M, N)
    print(result)