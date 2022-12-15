# import random as rd
# computer = rd.randint(1, 100)
# while True:
#     guess = int(input('请输入整数:'))
#     if not guess.isdigit():
#         print('请输入1-100范围内的正整数')
#     elif int(guess) < 1 or int(guess)>100:
#         print('请输入1-100以内的数')
#     else:
#         if guess == computer:
#             print('你猜对了')
#         elif guess < computer:
#             print('你猜小了')
#         else:
#             print('你猜大了')
#             break
# print(computer)

# 购物：结账时 价格小于等于50元，原价付款
# 大于50小于150元打折0.9折
# 大于150元打0.8折

# price = float(input('老板多少钱：'))
# if price > 150:
#     money = (price*0.8)
#     print('小伙子，我要给你打折，打折后付{:.0f}'.format(money))
# elif price > 50 and price <150:
#     money = (price*0.9)
#     print('小伙子，我要给你打折，打折后付{}'.format(money))
# else:
#     print('小伙子，你买的东西太少了，要不要多买一点给你
#     打折要不然你就付{}'.format(price))


# 创建者:飞老师
# 创建时间:2022/11/18
# 功能说明:输出 Hello  World
# print('Hello World')


