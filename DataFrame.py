from pandas import DataFrame

print ('使用字典生成DataFrame，key为列名字。')
data = {'state':['ok', 'ok', 'good', 'bad'],
        'year':[2000, 2001, 2002, 2003],
        'pop':[3.7, 3.6, 2.4, 0.9]}
print (DataFrame(data)) # 行索引index默认为0，1，2，3
'''
   pop state  year
0  3.7    ok  2000
1  3.6    ok  2001
2  2.4  good  2002
3  0.9   bad  2003
'''
# 指定列索引columns,不匹配的列为NaN
print (DataFrame(data, columns = ['year', 'state', 'pop','debt']) )
'''
   year state  pop
0  2000    ok  3.7
1  2001    ok  3.6
2  2002  good  2.4
3  2003   bad  0.9
'''
print ('指定行索引index')
x = DataFrame(data,
                    columns = ['year', 'state', 'pop', 'debt'],
                    index = ['one', 'two', 'three', 'four'])
print (x)
'''
       year state  pop debt
one    2000    ok  3.7  NaN
two    2001    ok  3.6  NaN
three  2002  good  2.4  NaN
four   2003   bad  0.9  NaN
'''