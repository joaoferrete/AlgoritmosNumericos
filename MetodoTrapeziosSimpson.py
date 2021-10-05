"""
    Implementação dos métodos dos trapezios repetidos 
    e de 1/3 de Simpson repetido e 3/8 de Simpson repedido
    para calculo de integral de funções polinomiais.
"""


import sympy
vari = sympy.Symbol('X')

def funcao(x, func, g):
    """ Função que calcula o valor de X no polinômio """
    soma=0
    for i in range(0, g):
        soma+=func[i]*x**i
    return soma


def trapeziosrep(func, g, a, b, n):
    """ Implementação do método dos trapézios repetidos """

    h=(b-a)/n
    x=a
    soma=0;

    for i in range(0, n+1):
        if i==0 or i==n: soma+=funcao(x, func, g)
        else: soma+=2*funcao(x, func, g)
        x+=h
    print("O resultado aproximado para a integral pelo método dos trapézios repetidos é {}".format(soma*h/2))
    return soma*h/2


def simpson1(func, g, a, b, n):
    """ Implementação do método 1/3 de Simpson """

    if n%2!=0:                      #Verifica se é divisivel por 2
        print("Não é possivel calcular com esse numero de subintervalos! Insira um multiplo de 2!\n")
        return

    h=(b-a)/n
    x=a
    soma=0

    for i in range(0, n+1):
        if i==0 or i==n: soma+=funcao(x, func, g)
        elif i%2==0: soma+=2*funcao(x, func, g)
        else: soma+=4*funcao(x, func, g)
        x+=h
    print("O resultado aproximado para a integral pelo método 1/3 de Simpson Repetido é {}".format(soma*h/3))
    return soma*h/3


def simpson3(func, g, a, b, n):
    """ Implementação do método 3/8 de Simpson """

    if n%3!=0:                              #Verifica se é divisivel por 3
        print("Não é possivel calcular com esse numero de subintervalos! Insira um multiplo de 3!\n")
        return
    h=(b-a)/n
    x=a
    soma=0

    for i in range(0, n+1):
        if i==0 or i==n: soma+=funcao(x, func, g)
        elif i%3==0: soma+=2*funcao(x, func, g)
        else: soma+=3*funcao(x, func, g)
        x+=h
    
    print("O resultado aproximado para a integral pelo método 3/8 de Simpson Repetido é {}".format(soma*h*3/8))
    return soma*h*3/8


def main():
    g=int(input("Insira o grau do polinômio: "))
    g=g+1
    func=[0]*(g)
    for i in range(g-1, -1, -1):                        #Inserção do Polinômio
        if i!= 0: func[i] = float(input("Insira o coeficiente que multiplica x^{}: ".format(i)))
        else: func[i] = float(input("Insira o coeficiente independente: "))

    print("\nO polinômio é: {}".format(sympy.expand(funcao(vari, func, g))))

    a=int(input("Insira o limite de integração inferior: "))
    b= int(input("Insira o limite de integração superior: "))

    while True:
        print("\n\nQual método deseja utilizar?")
        print("1 - Método dos Trapézios repetidos ")
        print("2 - Método de 1/3 de Simpson repetido")
        print("3 - Método de 3/8 de Simpson repetido")
        print("0 - Sair")
        op=int(input())

        if op==1:                       #Método dos Trapézios
            n=int(input("Insira o número de subintervalos: "))
            
            trapeziosrep(func, g, a, b, n)

            print("\n\nDeseja fazer outra operação? ")
            print("1 - SIM")
            print("2 - NÃO")
            op1=int(input())
            if op1==2: return
        
        elif op==2:                 #Método 1/3 de Simpson
            n=1
            while (n%2!=0): n=int(input("Digite o numero de sub-intervalos (Deve ser um multiplo de 2): "))
            simpson1(func, g, a, b, n)

            print("\n\nDeseja fazer outra operação? ")
            print("1 - SIM")
            print("2 - NÃO")
            op1=int(input())
            if op1==2: return
        
        elif op==3:                 #Método de 3/8 de Simpson
            n=1
            while (n%3!=0): n=int(input("Digite o numero de sub-intervalos (Deve ser um multiplo de 3): "))
            simpson3(func, g, a, b, n)

            print("\n\nDeseja fazer outra operação? ")
            print("1 - SIM")
            print("2 - NÃO")
            op1=int(input())
            if op1==2: return
        
        elif op==0:             #Sair do programa
            return

    return

main()