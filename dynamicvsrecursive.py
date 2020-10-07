def fib(x):
    if x==1 or x==2:
        return 1
    else:
        return fib(x-1)+fib(x-2)
def recursive(x):
    import time
    start_time = time.time()
    print("Answer:",fib(x))
    print("Time: %s seconds" % (time.time() - start_time))
def dynamic(x):
    import time
    start_time = time.time()
    fib=[1,1]
    for i in range(2,x):
        fib.append(fib[i-1]+fib[i-2])
    print("Answer:",fib[x-1])
    print("Time: %s seconds" % (time.time() - start_time))

n=int(input("Enter Fibbonacci Index: "))
print("")
print("Recursive Solution:")
recursive(n)
print("")
print("Dynamic Solution:")
dynamic(n)
print("")
