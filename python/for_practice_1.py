"""
187
다중반복문을 활용하여 구구단을 1단부터 9단까지 출력하는 프로그램 작성
"""
for i in range(1,9+1):
    for j in range(1,9+1):
        print(f'{i} * {j} = {i*j}' , end ='')
    print()

"""
188

문자열을 입력 받아 문자 하나씩 순서대로 합쳐서 출력

"""

a = input("Enter the sentence :")

for i in range(0,len(a)):
    for j in range(0,i+1):
        print(a[j], end ='')
    print()

"""
189
11층 피라미드 출력하는 프로그램 작성(1)
*
**
***
****
*****
******
*******
********
*********
**********
***********
"""
for i in range(1,11+1):
    print('*' * i)

"""
190
11층 피라미드 출력하는 프로그램 작성(2)

           *
          **
         ***
        ****
       *****
      ******
     *******
    ********
   *********
  **********
 ***********
"""
for i in range(0,11):
    print(' ' * (11-i-1),'*' * (i+1))

"""
191
다음과 같은 피라미드 출력하는 프로그램 작성(3)
*
***
*****
*******
*********
***********
***********
***********
***********
***********
***********
"""
for i in range(1,11+1):
    if i % 2 == 1 :
        a = '*' * i
        print(a)

for i in range(5):
    print(a)

"""
192
다음과 같은 피라미드 출력하는 프로그램 작성(4)
          *          
         ***         
        *****        
       *******       
      *********      
     ***********     
    *************    
   ***************   
  *****************  
 ******************* 
*********************
"""
for i in range(11):
    print(' ' * (10-i), end ='')
    print('*'*(2*i+1), end = '')
    print(' ' * (10-i), end = '')
    print()
"""
193
다음과 같은 피라미드 출력하는 프로그램 작성(5)
          *
         ***
        *****
       *******
      *********
     ***********
      *********
       *******
        *****
         ***
          *  
"""
odd = 11

for i in range(odd):
    for j in range(odd*2 - 1):
        if i<=5:
            if j in range(odd -1-i, odd+i):
                print('*', end ='')
            else:
                print(' ', end = '')
        else :
            if j in range(i,odd*2-1-i):
                print('*', end = '')
            else:
                print(' ', end ='')
    print()


"""
194
임의의 양수를 입력받고 이 정수보다 작은 소수중에 가장 큰 수를 출력하는 함수 작성
"""
num = int(input('Enter the positive number :'))
biggest_prime = 1

for i in range(1,num):
    isTrue = True
    for j in range(2,j):
        if i%j ==0:  # 2이상의 수로 나눠지면
            isTrue = False # 소수가 된다.
    if isTrue:
        biggest_prime = i
print('biggest prime number under', num ,'is', biggest_prime)
















