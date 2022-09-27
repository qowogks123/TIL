"""
167

아래와 같은 출력 결과가나오도록 하시오

num = 10

while num<= 18:
    (   a   )

result
10
12
14
16
18

"""

# My answer 
num = 10

while num <=18 :
    print(num)
    num += 2
 



""" 
168

1부터 100이하까지 2의 배수를 출력하시오

"""

# My answer

num = 1

while num <= 100:
    print(num, end = '')
    num *=2

"""
169

While문을 활용하여 영문자 q가 입력될 때까지 계속 반복하는 프로그램을 작성핫이ㅗ

"""
# My answer

while True:
    alph = input('Enter the alphabet:')
    if alph == 'q':
        break
print('Finish')




""" 
170
while문을 활용하여, 두 수를 입력받아, 작은 수에서 큰 수까지 5의 배수를 순서대로 출력하는 프로그램을 작성하시오

"""

#Failed to fix the problem
a = int(input('first num:'))
b = int(input('second num:'))

if a>b :
    c =a
    a =b
    b =c

i = a
while i<b:
    if i%5 ==0:
        print(i)
    i += 1





