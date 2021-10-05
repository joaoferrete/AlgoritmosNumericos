"""
    Implementação dos métodos da Bissecção, Newton e Secante
    para encontrar uma raiz aproximada para uma função
"""

import sympy
vari = sympy.Symbol('X')

def funcao(x, func, g):
    """ Função que calcula o valor de X no polinômio """
    soma=0
    for i in range(0, g):
        soma+=func[i]*x**i
    return soma

def bisseccao(a, b, er, func, g):
    """ Implementação do metodo da bissecção """

    if funcao(a, func, g)*funcao(b, func, g)<=0:
        x=(a+b)/2
        erro=1
        i=0
        while (funcao(x, func, g)!=0 and erro>er and i<=50):
            x=(a+b)/2
            print("\n  | ITERAÇÃO",i, "|")
            print("X: ", x)
            print("F(x): ", funcao(x, func, g))
            if funcao(a, func, g)*funcao(x, func, g)<0: b=x
            else: a=x
            i+=1
            erro=abs(b-a)
            print("Erro: ", erro)

        print("\nA aproximação para X pelo método da bissecção é: ", x)    
        return x
    
    print("\nNão é possível determinar a raiz no intervalo inserido.")
    return

def newton(a, er, func, deriv, g):
    """ Implementação do método de Newton """

    x=a
    erro=1
    i=1
    while ((funcao(x, func, g)!=0 and erro>er) and i<=50):
        x=a-(funcao(a, func, g)/funcao(a, deriv, g-1))
        erro=abs(funcao(x, func, g))
        print("\n  | ITERAÇÃO",i, "|")
        print("X: ", x)
        print("F(x): ", funcao(x, func, g)) 
        a=x
        i+=1
    print("\nA aproximação para X pelo método de Newton é: ", x)    
    return x

def chamaNewton(func, g):
    """ Função que pede os dados necessários para a chamada do método de Newton """

    print("Insira os coeficientes da derivada: ")
    der=[0]*(g-1)
    for i in range(g-2,-1, -1):                     #Inserção da derivada da função
        if i!= 0: der[i] = float(input("Insira o coeficiente que multiplica x^{}: ".format(i)))
        else: der[i] = float(input("Insira o coeficiente independente: "))
    print("\nA Derivada é: {}".format(sympy.expand(funcao(vari, der, g-1))))
    a=float(input("Insira a aproximação inicial para X: "))
    er=float(input("Insira um limitante para o erro: "))
    return newton(a, er, func, der, g)              #Chamada do método de Newton

def secante(a, b, er, func, g):
    """ Implementação do método de Secante """

    x=a
    erro=1
    i=0
    while ((funcao(x,func, g)!=0 and erro>er) and i<=50):
        x=(a*funcao(b, func, g) - b*funcao(a, func, g))/(funcao(b, func, g)-funcao(a, func, g))
        
        print("\n  | ITERAÇÃO",i, "|")
        print("X: ", x)
        print("F(x): ", funcao(x, func, g))
        
        a=b
        b=x
        i+=1
        erro=abs(b-a)
        print("Erro: ", erro)

    print("\nA aproximação para X pelo método das secantes é: ", x)    
    return x

def main():
    g=int(input("Insira o grau do polinômio: "))
    g=g+1
    func=[0]*(g)
    for i in range(g-1, -1, -1):                        #Inserção do Polinômio
        if i!= 0: func[i] = float(input("Insira o coeficiente que multiplica x^{}: ".format(i)))
        else: func[i] = float(input("Insira o coeficiente independente: "))

    print("\nO polinômio é: {}".format(sympy.expand(funcao(vari, func, g))))

    while True:
        print("\n\nQual método deseja utilizar?")
        print("1 - Método da Bissecção")
        print("2 - Método de Newton")
        print("3 - Método da Secante")
        print("0 - Sair")
        op=int(input())

        if (op==1): #Metodo da bissecção
            print("\nInsira o intervalo que deseja calcular:")
            a=float(input("Insira o valor inferior: "))
            b=float(input("Insira o valor superior: "))
            er=float(input("Insira o limitante para o erro: "))
            bisseccao(a, b, er, func, g)

            print("\n\nDeseja fazer outra operação? ")
            print("1 - SIM")
            print("2 - NÃO")
            op1=int(input())
            if op1==2: return

        elif (op==2): #Método de Newton
            chamaNewton(func, g)

            print("\n\nDeseja fazer outra operação? ")
            print("1 - SIM")
            print("2 - NÃO")
            op1=int(input())
            if op1==2: return

        elif op==3:   #Metodo da Secante
            a=float(input("Insira a primeira aproximação para X: "))
            b=float(input("Insira a segunda aproximação para X: "))
            er=float(input("Insira o limitante para o erro: "))
            secante(a, b, er, func, g)

            print("\n\nDeseja fazer outra operação? ")
            print("1 - SIM")
            print("2 - NÃO")
            op1=int(input())
            if op1==2: return

        elif op==0: #Sair do programa
            return

    return


main()
