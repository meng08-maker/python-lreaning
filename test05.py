i = int(input("请输入利润："))

if i<=100000:
    bonus = i*0.1
    print("奖金为：",bonus)
elif 100000<i<=200000:
    bonus = 100000*0.1+(i-100000)*0.075
    print("奖金为：",bonus)
elif 200000<i<=400000:
    bonus = 100000*0.1+100000*0.075+(i-200000)*0.05
    print("奖金为：",bonus)
