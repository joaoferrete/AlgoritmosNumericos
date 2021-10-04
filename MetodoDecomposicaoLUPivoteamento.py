"""
    Implementação do método de Decomposição LU com Pivoteamento
    Para resolução de sistemas de equações lineares
"""

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

def substituicaoret (n, mat, c):
    """ Implementação do Método das Substituições Retroativas """
    
    x=vetor(n)
    x[n-1] = c[n-1]/mat[n-1][n-1]
    for i in range(n-2, -1, -1):
        soma=0
        for j in range(i+1, n):
            soma=soma+mat[i][j] * x[j]
        x[i] = ((c[i] - soma)/mat[i][i])

    return x

def substituicaosuc (n, matriz, c):
    """ Implementação do Método das Substituições Sucessivas """
    x=vetor(n)
    x[0] = c[0]/matriz[0][0]
    for i in range(1, n):
        soma=0
        for j in range(0, i):
            soma=soma+matriz[i][j] * x[j]
        x[i] = ((c[i] - soma)/matriz[i][i])
    return x


def decLU(n, mat, c):
    """ Implementação da Decomposição LU com Pivoteamento """

    p = vetor(n)
    l = matriz(n)
    u = matriz(n)
    x = vetor(n)
    for i in range(0, n):
        p[i] = i
    for j in range(0, n-1):
        max = abs(mat[j][j])
        a = j
        for k in range(j+1, n):
            if abs(mat[k][j]) > max:
                max = abs(mat[k][j])
                a = k
        if j != a:
            for k in range(0, n):
                t = mat[j][k]
                mat[j][k] = mat[a][k]
                mat[a][k] = t
            t = p[j]
            p[j] = p[a]
            p[a] = t
        if abs(mat[j][j]) != 0:
            for i in range(j+1, n):
                m = mat[i][j]/mat[j][j]
                mat[i][j] = m
                for k in range(j+1, n):
                    mat[i][k] = mat[i][k] - m*mat[j][k]

    l, u = decL(mat, n)
    for i in range(0, n):
        x[i] = c[p[i]]

    x = substituicaosuc(n, l, x)
    x = substituicaoret(n, u, x)
    return x


def decL(l, n):  # Função auxiliar que separa a matriz L e a Matriz U
    u = matriz(n)
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                u[i][j] = l[i][j]
                l[i][j] = 1
            elif j > i:
                u[i][j] = l[i][j]
                l[i][j] = 0
            else:
                u[i][j] = 0

    return l, u


def main():
    n = int(input("Numero de linhas da matriz: "))
    mat = matriz(n)
    c = vetor(n)
    p = vetor(n)
    print("Insira os termos da matriz: ")
    for i in range(0, n):
        for j in range(0, n):
            mat[i][j] = float(input())
    print("Insira o vetor independente:")
    for i in range(0, n):
        c[i] = float(input())
    p = decLU(n, mat, c)

    print("[ ", end=" ")
    for i in range(0, n):
        print(p[i], end="  ")
    print("]")
    return


main()

#    MATRIZ UTILIZADA PARA TESTE:
#    |  1  -3   2  | |X1|    |  11 |
#    | -2   8  -1  | |X2| =  | -15 |
#    |  4  -6   5  | |X3|    |  29 |
#    Resultado esperado: [2, -1, 3]

#    |  2   1  -1  | |X1|    |  3 |
#    |  1   3   2  | |X2| =  |  4 |
#    |  3  -2   1  | |X3|    | -5 |
#    Resultado esperado: [0, 2, -1]

#    |  1   1   1  | |X1|    |  6 |
#    |  1   2   2  | |X2| =  |  9 |
#    |  2   1   3  | |X3|    | 11 |
#    Resultado esperado: [3, 2, 1]


#    |  1 -3  3   7 | |X1|    | 6 |
#    | -6  0  3   1 | |X2| =  |-5 |
#    | -5  2  1   1 | |X3|    | 1 |
#    | -6  4  7   8 | |X4|    | 9 |
#    Resultado esperado: [ 0.4856596558317399, 1.4053537284894846, -1.3518164435946463, 1.9694072657743782 ]
