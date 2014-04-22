# Implementacao do algoritmo
def quo(x, y, k):
    if k == 1:
        return 1
    return x**(k-1) + y*quo(x, y, k-1)



if __name__ == '__main__':
    # Codigo usado para testar com diferentes valores de x, y, e k
    # Uso:
    #   python 1.py x y k
    #     x - valor de x
    #     y - valor de y
    #     k - valor de k
    
    from time import time
    import sys

    EXECS_PER_LOOP = 100000
    TIME_TRESHOLD = 5

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    k = int(sys.argv[3])

    # Executa 100000 vezes a cada vez, ate passar de 5 segundos
    start = time()
    execs = 0
    while time() - start < TIME_TRESHOLD:
        execs += EXECS_PER_LOOP
        for i in range(EXECS_PER_LOOP):
            quo(x, y, k)
    end = time()
    elapsed = end - start

    # Print style 1: human-readable
    print("x = %d" % x)    
    print("y = %d" % y)    
    print("k = %d" % k)    
    print("execs = %d" % execs)    
    print("time = %.3f s" % elapsed)
    print("time/exec = %.6f ms" % (1000*elapsed/execs))
    print()

    # Print style 2: LaTeX table
    # print("%d & %d & %d & %d & %.3f s & %.6f ms \\\\" % 
    #     (x, y, k, execs, elapsed, 1000*elapsed/execs))
