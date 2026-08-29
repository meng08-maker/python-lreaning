
# 密码设置
while True:
    num = input("请输入密码：")
    n = input("请再次输入密码：")
    if num == n:
        print("密码设置成功")
        break
    else:
        print("两次密码不一致，请重新设置密码")

