# while True:
#     job = str(input('你的作业写完了吗？:'))
#     if job == '写完了':
#         print('劳逸结合，现在可以出去玩一会儿了')
#         break
#     elif job == '没有写完':
#         print('继续写作业，完成了作业才能出去玩哦')
#     else :
#         print('继续写作业')

# passward = int(input('请输入密码:'))
# while not passward == 123:
#     passward = int(input('密码不正确\n请重新输入:'))
# print('恭喜你密码正确')

# for subject in ['语文','数学','英语','物理','化学']:
    # if subject == '化学':
    #     break
    # else:
    #     print(subject)

# 逢7必过
# import random
# number =  random.randint(1,6)


# pessward=int( input('请输入6位数的密码'))
# while not pessward ==int( 123654):
#     pessward=  int(input('密码错误\n请重新输入：'))
# print('密码正确')

# pessward = int(input('请输入6位数的密码：'))
# while pessward != int(123789):
#     pessward=int(input('密码错误\n请重新输入:'))
# print('密码正确')



pessward = int(input('请输入密码：'))
number =  1
while pessward != 123123:
    if number <= 3:
        pessward = int(input('密码错误\n 请重新输入:'))
        number += 1
        print(number)
    else:
        print('密码尝试错误超过3次，账户已锁定，请明天继续尝试')
        break
if number <= 3:
    print('密码正确')

# for subjcek in ['语文','数学','英语','物理','化学']:
#     if subjcek == '英语':
#         break
#     print(subjcek)
# for subjcek in ['语文','数学','英语','物理','化学']:
#     if subjcek == '英语':
#         continue
#     print(subjcek)







