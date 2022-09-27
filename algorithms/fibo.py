def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

if __name__=='__main__':
    user_num = int(input("Enter num: "))
    print(fibo(user_num))

