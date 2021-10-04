"""
    Implementação do método de Gauss com Pivoteamento
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

def gauss_pivo(n, mat, c): 
    """ Implementação do Método de Gauss com Pivoteamento """

    for k in range(0, n-1):
        maior = abs(mat[k][k])
        if n < 3:
            r = k
        for i in range(k+1, n):
            if abs(mat[i][k]) > maior:
                maior = abs(mat[i][k])
                r = i
        for i in range(0, n):
            aux = mat[k][i]
            mat[k][i] = mat[r][i]
            mat[r][i] = aux
        aux = c[k]
        c[k] = c[r]
        c[r] = aux
        for i in range(k+1, n):
            m = (-1)*mat[i][k]/mat[k][k]
            for j in range(k, n):
                mat[i][j] = mat[i][j] + (m*mat[k][j])
            c[i] = c[i] + m*c[k]
    return substituicaoret(n, mat, c)


def main():
    n = int(input("Numero de termos: "))
    mat = matriz(n)
    c = vetor(n)
    print("Insira os termos da matriz:")
    for i in range(0, n):
        for j in range(0, n):
            mat[i][j] = float(input())
    print("Insira os termos do vetor independente:")
    for i in range(0, n):
        c[i] = float(input())
    x = gauss_pivo(n, mat, c)
    print("[", end=" ")
    for i in range(0, n):
        print(x[i], end="  ")
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

#    |  1   2  -3  | |X1|    | 10 |
#    |  2   1   1  | |X2| =  |  3 |
#    | -3   2   1  | |X3|    | -6 |
#    Resultado esperado: [2, 1, -2]

#    |  1   1   1  | |X1|    |  6 |
#    |  1   2   2  | |X2| =  |  9 |
#    |  2   1   3  | |X3|    | 11 |
#    Resultado esperado: [3, 2, 1]
