# Python3 simple code to explain
# the type() function
print(type([1,2,'3', True]) is list)

print(type(['lucas', 8,' xxx']) is not list)

print(type(()) is tuple)

print(type({}) is dict)

print(type({}) is not list)

print('============================')
listTest = ['china', 'usa', 'japan']
print(listTest)


tupleTest = ('cn', 'us', 'jp')
print(tupleTest)


dicTest = {'cny', 'usd', 'jpy'}
print(dicTest)

#https://www.scaler.com/topics/how-to-reverse-a-list-in-python/
print("===========================")
test_list = [1, 2, 3, 4, 5, 6, 7]
print(test_list[::-1]) # 倒序输出
print(test_list[::1])  # 顺序输出
print(test_list[::2])  # 输出 1，3，5，7
print(test_list[::3])  # 输出 1，4，7
print(test_list[::])   # 复制数组， 原样输出
print(test_list[0:5])  # 输出第0个到第5个数
print(test_list[1:6])  # 输出第1个到第6个数