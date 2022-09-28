"""
176
입력받은 두 수 사이에 있는 3의 배수의 합을 구하는 프로그램 
"""
a = int(input('Enter the 1st number :'))
b = int(input('Enter the 2nd number :'))

if a>b:
    c = a
    b = a
    b = c
    
sum = 0

for i in range(a,b):
    if i % 3 ==0:
        sum += i 
        
print(sum)
    
"""
177

for 문을 활용해, 1부터 입력한 숫자 n까지의 합을 구하는 프로그램 
"""

a = int(input('정수를 하나 입력하시오 :'))

sum = 0
for i in range(1,a+1):
    sum += i
    
print(f'1부터 7까지의 합은 : {sum}')

"""
180

입력받은 수가 소수인지 판별해주는 프로그램 작성
"""
a = int(input('숫자를 입력하세요'))
b = 0

for i in range(2,a):
    if a%i == 0:
        b=1
        
if b==0:
    print('소수입니다')
else:
    print('소수가 아닙니다.')

"""
181
입력한 수의각 자리수를 더하는 프로그램 작성
예를 들어, 12345를 입력하면 1+2+3+4+5 = 15를 출력
"""
num = input('Enter the number :')

sum = 0

for j in num:

    sum += int(j)


print(f'{num}의 각 자리수의 합은 : {sum}')

"""
182
입력한 문자열이 숫자인지 판별해주는 프로그램 작성

"""
num = input('Enter the number:')

numbers = ['1','2','3','4','5','6','7','8','9','0']
num_dot = 0
isNum = True

for i in num:
    if not(i in numbers):
        num_dot += 1
        if num_dot == 2 :
            isNum = Falsed
            break
    else:
        isNum = False
        break
        
print(num +'is numbers?', isNum)


"""
183

입력받은 두 자연수 a,b 사이의 구간에 대해서 홀수는 더하고 짝수는 빼는 식을 보여준 후 결과를 출력하는 프로그램
"""
a = int(input('Enter the 1st number'))
b = int(input('Enter the 2st number'))

if a>b:
    c = a
    b = a
    b = c
sum = 0
for i in range(a,b+1):
    if i % 2 != 0:
        print(f'+{i} ', end ='')
        sum +=i
        
    else:
        print(f'-{i}',end = '')
        sum -=i

        
print(f'= {sum}')

"""
184
1 + (-2) + 3 + (-4) + 5 ... 와 같은 방식으로 계속 더해나갈때, 총합이 100이상이
되는 마지막 수가 무엇인지 프로그램 작성
"""
sum = 0

for i in range(1,1000):
    if i % 2 ==0:
        i = i*(-1)
        sum +=i
  
    else:
        sum +=i

        
        
    if sum >= 100:
        break
        
print(i)

"""
185
HandsomeQ 수열은 자연수 n에 대하여 아래와 같은 규칙을 가진다.

n -> n/2 (n이 짝수)
n -> 2n+2(n이 홀수)

n = 13일때, 이를 가지고 만든 HandsomeQ 수열은 13->28->14->7->16->8->4->2->1
일때 길이가 9인 수열이 된다. HandsomeQ수열의 길이를 출력하는 프로그램 작성

"""
n = int(input('Enter the number :'))

lens = 0

for i in range(10000):
    if n % 2 == 0:
        n = n//2
        lens += 1 
    else:
        n = (2*n) +2
        lens +=1
    if n == 1:
        lens +=1
        print(lens)
        break
    
# another answer 

num = int(input('Enter the number:'))
len =1
while num != `:
    if num%2 ==0:
        num =num//2
    else:
        num = 2*num +2
    len += 1
print(len)





















