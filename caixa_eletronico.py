"""
 Este problema foi utilizado em 600 Dojo(s).

Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:

    Entregar o menor número de notas;
    É possível sacar o valor solicitado com as notas disponíveis;
    Saldo do cliente infinito;
    Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
    Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

Exemplos:

    Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
    Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00. 

"""

notas = [100, 50, 20, 10]


def subtrair(valor, nota):
	items = []
	while valor >= nota:
		valor = valor - nota
		items.append(nota)
	return valor, items


def sacar(valor):
    items = []
    i = 0
    while valor != 0 and i < len(notas):
        valor, items_nota = subtrair(valor, notas[i])
        items.extend(items_nota)
        i += 1
    return items

assert sacar(100) == [100]
assert sacar(30) == [20, 10]
assert sacar(80) == [50, 20, 10]
assert sacar(180) == [100, 50, 20, 10]

assert sacar(300) == [100, 100, 100]
assert sacar(40) == [20, 20]
assert sacar(20) == [20]
assert sacar(60) == [50, 10]
assert sacar(70) == [50, 20]
