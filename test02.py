# 设置账号密码
yes_account = input("请输入手机号或账号：")
yes_password = input("请输入密码：")
re_password = input("请再次输入密码：")
# 检验两次密码是否一致
while yes_password != re_password:
    print("两次密码不一致，请重新设置密码")
    yes_password = input("请输入密码：")
    re_password = input("请再次输入密码：")
else:
    print("账号密码设置成功")
print("\n\n\n\n" + "*" * 30)

# 登录
account = input("请输入账号或手机号：")
password = input("请输入密码：")

while account != yes_account or password != yes_password:
    print("账号或密码错误，请重新输入")
    account = input("请输入账号或手机号：")
    password = input("请输入密码：")
else:
    print("登陆成功！")