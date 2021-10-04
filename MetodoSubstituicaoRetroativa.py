def matriz (n):
    """ Função que faz a criação da Matriz """
    x=[0]*n
    for i in range (0, n):
        x[i] = [0]*n
    for i in range(0, n):
        for j in range (0, n):
            x[i][j] = 0.0
    return x

def vetor (n):
    """ Função que cria um vetor de tamanho N """
    x=[0]*n
    for i in range(0, n):
        x[i]=0.0
    return x

def substituicaoret (n, mat, c):  #Principal função
    x=vetor(n)
    x[n-1] = c[n-1]/mat[n-1][n-1]
    for i in range(n-2, -1, -1):
        soma=0
        for j in range(i+1, n):
            soma=soma+mat[i][j] * x[j]
        x[i] = ((c[i] - soma)/mat[i][i])

    return x

def main():
    n= int(input("Numero de termos: "))
    mat = matriz(n)
    c = vetor(n)
    print("Insira os termos da matriz: ")
    for i in range (0, n):
        for j in range (0, n):
            mat[i][j] = float(input())
    print("Insira os termos do vetor independente: ")
    for i in range (0, n):
        c[i] = float(input())
    x = substituicaoret(n, mat, c)
    print("[", end=" ")
    for i in range (0, n):
        print(x[i], end="  ")
    print("]")
    return

main()

#    MATRIZ UTILIZADA PARA TESTE:
#    |  4 -6   5  | |X1|    |  29 |
#    |  0  5  1.5 | |X2| =  |-0.5 |
#    |  0  0  1.2 | |X3|    | 3.6 |
#    Resultado esperado: [2, -1, 3]


#    |  5 -2  6   1 | |X1|    | 1 |
#    |  0  3  7  -4 | |X2| =  |-2 |
#    |  0  0  4   5 | |X3|    |28 |
#    |  0  0  0   2 | |X4|    | 8 |
#    Resultado esperado: [-3, 0, 2, 4]