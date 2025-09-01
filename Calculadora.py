print("Mini Calculadora")

def soma(a, b):
    return a + b
print("Soma:", soma(2, 3))

def subtracao(a, b):
    return a - b
print("Subtração:", subtracao(5, 2))

def multiplicacao(a, b):
    return a * b
print("Multiplicação:", multiplicacao(4, 3))

def divisao(a, b):
    return a / b if b != 0 else "Erro: divisão por zero"
print("Divisão:", divisao(10, 2))
