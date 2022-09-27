"""
159

두 자리 랜덤한 정수를 발생하는 프로그램 작성

# My answer 

import random

num = randrange(10,99)

result = int(num)
print(result)


# Another answer

import random

ran_num = random.randrange(10,100)
print(ran_num)

"""

"""

160

소수 첫 째 자리까지 가진 0과 10 사이의 수를 랜덤으로 발생하는 프로그램 작성


# My answer

import random

n1 = random.randrange(0,10)
n2 = random.random()

num = n1 + n2

print(round(num,1))

# another answer

import random
num = round(random.random()*10,1)
print(num)

"""


"""
161

두 수를 입력받고, 입력 받은 두 수 사이의 정수를 랜덤으로 출력하는 프로그램 

# My answer - Failed to resolve(correct answer)

import random

num1 = int(input('두 정수를 입력하시오:'))
num2 = int(input())

if abs(num1-num2) < 1:
    print('no integer between two numbers')
else:
    ran_num = (min(num1,num2) + random.randrange(1,abs(num2-num1)))
    print(ran_num)

"""

"""
162

10 이상 20 이하의 정수형 난수 4개를 발생시켜, 이들의 평균이 15 이상이면 Big, 아니면 Small를 출력하는 프로글매

# My answer

import random

list_num = []
for i in range(4):
    list_num.append(random.randrange(10,20))

avg = (list_num[0] + list_num[1] + list_num[2] + list_num[3] / len(list_num)

print(f'4가지 수 :{list_num}')
print(f'평균 : {avg}')
if avg >= 15:
    print('Big')
else:
    print('Small')

# another answer
import random
numbers = range(10,21)

rand_nums = [random.choice(numbers) for i in range(0,4)]

print('4가지 수:",rand_nums)
mean = sum(rand_nums)/len(rand_nums)
print('평균 :' mean)

if mean>=15:
    print('Big')
else:
    print('Small')

"""

"""
163
컴퓨터가 랜덤으로 발생한 난수를 맞추는 게임을 하려고 한다. 다음 게임 규칙에 맞게 프로그램을 작성하시오

1단계 : 1과 2 중에 하나의 숫자를 맞춘다.
2단계: 1~4중에 하나의 숫자를 맞춘다.
3단계 : 1~8중에 하나의 숫자를 맞춘다.

실패하면 'Failure'를 출력한다

# My answer

import random 

number = int(input('level1(1~2):'))
level_1 = random.randint(1,2)
level_2 = random.randint(1,4)
level_3 = random.randint(1,8)

suc = 0


if number == level_1:
    print('Correct')
    suc+=1
    number1 = int(input('level1(1~4):'))
    if number1 == level_2 :
        print('Correct')
        suc+=1
        number2 = int(input('level1(1~8):'))
        if number2 == level_3:
            print('Correct')
            suc+=1
        else:
            print('Fail')
    else:
        print('Fail')
else:
    print('Fail')
    
print(f'Answer is : {suc}')


# another answer 
import random
min_n =1 
max_n = 2
level = 0

while level<3:
    level+=1
    ans=random.randrange(min_n, max_n+1)
    num = int(input('level{}({}~{}) :'.format(level,min_n,max_n)))
    if ans == num :
        print('Correct!')
        max_n=max_n*2
    else:
        print('Failure!")
        print('Answer is :' , ans)
        break
    if max_n>8:
        print('Lucky')


"""

"""
164

cars라는 이름의 리스트에 Hyundai, Kia, BMW, Benz를 원소로 저장한다. 이 리스트를 random모듈의 함수를 이용하여
섞어준 다음, 가장 첫 번째의 원소가 Hyundai라면 True를 출력하는 프로그램을 작성하시오

# My answer 

cars = ['Hyundai', 'Kia', 'BMW' , 'Benz']

print(f'original : {cars}')

random.shuffle(cars)

print(f'change : {cars}')

if cars[0] == 'Hyundai':
    print('True')
else:
    'False'

# another answer 

cars = ['Hyundai' , 'Kia' , 'BMW' , 'Benz')
random.shuffle(cars)
print(cars[0] == 'Hyundai')
"""

