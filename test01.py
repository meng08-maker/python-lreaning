
# print("hello world")

# #基本运算
# x=int(input ("请输入第一个数字："))
# y=int(input ("请输入第二个数字："))
# i=x+y
# if i>=20 and i<40:
#     print("结果大于等于20且小于40")
# elif i>=40:
#     print("结果大于等于40")
# else:
#     print("结果小于20")

# #while循环
# a=int(input("请输入一个数字："))
# b=int(input("请输入另一个数字："))
# z=a*b

# while z<1000:
#     print("计算结果为：",z)
#     print("最终结果<1000\n继续计算")
#     z=z*2
# else:
#     print("最终结果>=1000\n结束计算")
# print("最终结果为：",z)

yes_account = "18888888888" 
yes_password = "88888888"

account = input("请输入账号：")
password = input("请输入密码：")

while account != yes_account or password != yes_password:
    print("账号或密码错误，请重新输入")
    account = input("请输入账号：")
    password = input("请输入密码：")
else:
    print("登陆成功")