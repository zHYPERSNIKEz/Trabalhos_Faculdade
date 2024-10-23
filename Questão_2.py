#PIZZARIA 

#Validação de sabor
def validaSabor(sabor):
    return sabor in ['PS', 'PD']

def validaTamanho(sabor, tamanho):
    tamanhosValidos = {
        'PS': {'P': 30, 'M': 45, 'G': 60},
        'PD': {'P': 34, 'M': 48, 'G': 66}
    }
    return tamanho in tamanhosValidos[sabor]

def obterSabor():
    while True:
        sabor = input('Digite um sabor válido (PS/PD): ').upper()
        if validaSabor(sabor):
            return sabor
        print('Sabor inválido. Digite um sabor válido.')

def obterTamanho(sabor):
    while True:
        tamanho = input('Digite o tamanho (P/M/G): ').upper()
        if validaTamanho(sabor, tamanho):
            return tamanho
        print('Tamanho inválido. Por favor, escolha um tamanho válido (P/M/G).')

def calcularPreco(sabor, tamanho):
    tamanhosValidos = {
        'PS': {'P': 30, 'M': 45, 'G': 60},
        'PD': {'P': 34, 'M': 48, 'G': 66}
    }
    return tamanhosValidos[sabor][tamanho]


#TELA INICIAL
print('-'* 20,'Bem-Vindo a Pizarria do Robson','-' *20)
print('-'*30,'Cardápio','-'*30)
print('-'*80)
print('-'*3,'| Tamanho |  Pizzas Salgadas (PS)  | Pizzas Doces (PD) |', '-'*3)
print('-'*3,'|    P    |     R$ 30.00           |      R$ 34.00     |', '-'*3)
print('-'*3,'|    M    |     R$ 45.00           |      R$ 48.00     |', '-'*3)
print('-'*3,'|    G    |     R$ 60.00           |      R$ 66.00     |', '-'*3)
print('-'*80)

#INICIO DE PROGRAMA


sabores = {'PS': 'pizza salgada', 'PD': 'pizza doce'}
valorTotal= 0

while True:
    sabor = obterSabor()
    tamanho = obterTamanho(sabor)
    preco = calcularPreco(sabor, tamanho)

    # Mostra o sabor e o valor da pizza antes de continuar
    if sabor == 'PS':
        tipo_pizza = 'salgada'
    else:
        tipo_pizza = 'doce'
    print(f'Você escolheu uma pizza {tipo_pizza} de tamanho {tamanho} no valor de R$ {preco:.2f}')

    valorTotal += preco

    continuar = input('Deseja continuar? (S/N): ').upper()
    if continuar == 'N':
        break

# Ao final, mostramos apenas o valor total
print(f'\nO valor total da sua compra é R$ {valorTotal:.2f}')

#função para escolher o sabor
def escolherSabor():
    while True:
        sabor = input('Entre com o sabor desejado (PS/PD): ').upper()
        if sabor in ['PS', 'PD']:
            return sabor
        else:
            print('Sabor inválido. Tente novamente')  # Mensagem de erro ao digitar sabor inválido

#função para escolher o tamanho
def escolherTamanho():
    while True:
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
        if tamanho in ['P', 'M', 'G']:
            return tamanho
        else:
            print('Tamanho inválido. Tente novamente')  # Mensagem de erro ao digitar tamanho inválido


