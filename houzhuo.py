#!/use/bin/env python
# _*_ coding:utf-8 _*_

#建立一个栈来存储待计算的操作数；
# 遍历字符串，遇到操作数则压入栈中，遇到操作符号则出栈操作数(n次)，进行相应的计算，计算结果是新的操作数压回栈中，等待计算
# 按上述过程，遍历完整个表达式，栈中只剩下最终结果；
operators = {  # 运算符操作表
    '+': lambda op1, op2: op1 + op2,
    '-': lambda op1, op2: op1 - op2,
    '*': lambda op1, op2: op1 * op2,
    '/': lambda op1, op2: op1 / op2,
}
def evalPostfix(e):
    """
    :param e: 后缀表达式
    :return: 正常情况下栈内的第一个元素就是计算好之后的值
    """
    tokens = e.split()  # 把传过来的后缀表达式切分成列表
    stack = []
    for token in tokens:  # 迭代列表中的元素
        if token.isdigit():  # 如果当前元素是数字
            stack.append(int(token))  # 就追加到栈里边
        elif token in operators.keys():  # 如果当前元素是操作符
            f = operators[token]  # 获取运算符操作表中对应的lambda表达式
            op2 = stack.pop()  # 根据先进后出的原则，先让第二个元素出栈
            op1 = stack.pop()  # 在让第一个元素出栈
            stack.append(f(op1, op2))  # 把计算的结果在放入到栈内
    return stack.pop()  # 返回栈内的第一个元素
if __name__ == '__main__':
    result = evalPostfix('2 3 4 * +')
    print(result)
# 14