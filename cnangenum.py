#!/use/bin/env python
# _*_ coding:utf-8 _*_

from collections import deque

#数字变换

def atob(a, b):
    """
    :param a: 开始的数字
    :param b: 最终转换之后的数字
    :return: 最小匹配的次数
    """
    q = deque([(a, 0)])  # a=当前数字，0=操作的次数
    checked = {a}  # 已经检查过的数据
    while True:
        s, c = q.popleft()
        if s == b:
            break
        if s < b:  # 要计算的数小于计算之后的数字
            if s + 1 not in checked:  # 如果要计算的数字+1不在已检查过的数据集合中
                q.append((s + 1, c + 1))  # 要计算的数+1，转换次数+1
                checked.add(s + 1)  # 把计算过的数添加到checked集合中
            if s * 2 not in checked:
                q.append((s * 2, c + 1))
                checked.add(s * 2)
        if s > 0:  # 要计算的数大于0
            if s - 1 not in checked:
                q.append((s - 1, c + 1))
                checked.add(s - 1)
    return q.popleft()[-1]

if __name__ == '__main__':
    result = atob(3, 11)
    print(result)