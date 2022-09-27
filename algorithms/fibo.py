def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_mem():
    cache = {
            0:0, 
            1:1
            }
    def func(n):
        if n not in cache:
            cache[n] = func(n-1) + func(n-2)
        return cache[n]
    return func




if __name__=='__main__':
    user_num = int(input("Enter num: "))
    fibo_m = fibo_mem()
    print(fibo_m(user_num))

