# Author:Louis Chu

# 1.all方法 接收可迭代的数据 如果数据里面只要有一个数据不为真
#        则返回false  如果全部为真 则返回true

print(all([1,2,3])) #true
print(all([0,2,6])) #false

#any 方法 只要数据中有一个数据为真的，那么这个返回的额就是true
print(any([0,1,3])) #True

#bin 方法是返回一个二进制
print(bin(8))  #0b1000

#
