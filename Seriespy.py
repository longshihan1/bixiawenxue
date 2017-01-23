import pandas as pd
from pandas import Series,DataFrame

print ('使用字典来生成Series')
data = {'a':1, 'b':2, 'd':3, 'c':4}
x = Series(data)
print (x)
'''
a    1
b    2
c    4
d    3
'''
print ('使用字典生成Series,并指定额外的index，不匹配的索引部分数据为NaN。')
exindex = ['a', 'b', 'c', 'e']
y = Series(data, index = exindex) # 类似替换索引
print( y)
'''
a    1.0
b    2.0
c    4.0
e    NaN
'''
print( 'Series相加，相同行索引相加，不同行索引则数值为NaN')
print( x+y)
'''
a    2.0
b    4.0
c    8.0
d    NaN
e    NaN
'''
print( '指定Series/索引的名字')
y.name = 'weight of letters'
y.index.name = 'letter'
print( y)
'''
letter
a    1.0
b    2.0
c    4.0
e    NaN
Name: weight of letters, dtype: float64
'''
print( '替换index')
y.index = ['a', 'b', 'c', 'f']
print( y )# 不匹配的索引部分数据为NaN
'''
a    1.0
b    2.0
c    4.0
f    NaN
Name: weight of letters, dtype: float64
'''