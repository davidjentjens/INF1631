def quo(x, y, k):
    if k == 1:
        return 1
    return x**(k-1) + y*quo(x, y, k-1)

if __name__ == '__main__':
    # Codigo usado para testar com diferentes valores de x, y, e k
    # Uso:
    #   python ed1.py x y k n
    #     x - valor de x
    #     y - valor de y
    #     k - valor de k
    #     n - numero de execucoes
    
    import timeit
    import sys

    x = sys.argv[1] 
    y = sys.argv[2] 
    k = sys.argv[3] 
    number = int(sys.argv[4]) 

    t = timeit.timeit("quo(" + ','.join([x, y, k]) + ")", setup = "from __main__ import quo", number = number)

    print("x = " + x)    
    print("y = " + y)    
    print("k = " + k)    
    print("execs = " + str(number))    
    print("time = " + ("%.3f" % t) + ' s')
    print("time/exec = " + ("%.6f" % (1000*t/number)) + ' ms')
