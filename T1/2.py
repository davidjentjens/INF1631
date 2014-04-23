# Implementacao do algoritmo
def numbers(k, m):

    newList = []

    # Caso base
    if k == 1:
        for i in range(m):
            newList.append([i+1])
        return newList

    previousList = numbers(k-1,m)

    # para cada numero de k - 1 digitos
    for i in range(len(previousList)):
        # para cada digito entre 0 e m-1
        for j in range(m):
            # se j+1 ainda nao foi utilizado no numero corrente,
            # adicionar ao final deste e salvar na lista
            if (j+1) not in previousList[i]:
                newNumber = list(previousList[i])
                newNumber.append(j+1)
                newList.append(newNumber)

    return newList

if __name__ == '__main__':
    # Codigo usado para testar com diferentes valores de m e k
    # Uso:
    #   python 2.py m k
    #     m - valor de m
    #     k - valor de k
    
    from time import time
    import sys

    TIME_TRESHOLD = 5
    EXEC_TRESHOLD = 5

    m = int(sys.argv[1])
    k = int(sys.argv[2])

    # Executa no minimo por 5 segundos
    start = time()
    execs = 0
    while not (time() - start > TIME_TRESHOLD):
        execs += 1
        numbersList = numbers(k, m)
    end = time()
    elapsed = end - start

    # print(numbersList)
    # print("Total: %d" % len(numbersList))

    # print("Execs: %d" % execs)
    # print("Elapsed: %.3f s" % elapsed)
    # print("Time per exec: %.6f ms" % (1000*elapsed/execs))
    print("%d & %d & %d & %.3f s & %.3f ms \\\\" % (m, k, execs, elapsed, 1000*elapsed/execs))
