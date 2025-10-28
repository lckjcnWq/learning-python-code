import time
from pydoc import describe

# print('hello world')
# print('this is a test')
# print(0x100)
#
# a=45
# b=12
# print(a+b)
# print(a*b)
# print(str(a))
# print(float(b))
# print(bool(a))
#
# flag0 =  1==1
# print(flag0)
# flag1 = 3>1
# print(flag1)
#
# # 判断条件
#
# height = float(input('please input your height: '))
# width = float(input('please input your width: '))
# bmi = height/ (width /100) ** 2
# print(bmi)
# if 18.5 <= bmi <= 25:
#     print('你的身材很棒')
# else:
#     print('你的身材不够标准！')
#
# status_code = int(input('please input your status code: '))
# match status_code:
#     case 1: describe='good'
#     case 2: describe='bad'
#     case 3: describe='ok'
#     case _: describe='error'
# print(describe)

# 循环条件
for i in range(3600):
    print(i)
    time.sleep(1)