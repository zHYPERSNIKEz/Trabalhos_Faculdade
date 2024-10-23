#MADEIREIRA 

#variavel para validação correta do usario
def validaMadeira():
    while True:
        print('Entre com o tipo de madeireia desejada')
        print('PIN - Tora de Pinheiro')
        print('PER - Tora de Peroba')
        print('MOG - Tora de Mogno')
        print('IPE - Tora de Ipê')
        print('IMB - Tora de Imbulia')
        tipoMadeira = input('>>').upper()
        #verificação
        if tipoMadeira == 'PIN':
            return 150.40
        elif tipoMadeira =='PER': 
            return 170.20
        elif tipoMadeira =='MOG':
            return 190.90
        elif tipoMadeira =='IPE':
            return 210.10
        elif tipoMadeira =='IMB':
            return 220.70
        else:
            print('Digite um tipo de madeira valido')#mensagem de erro 

#variavel para verificar se a quantidade é valida
def validaQuantidade():
    while True:
        try:
            qtdTora = int(input('Digite a quantidade desejada de toras em (m³): '))
            if 0 < qtdTora <=2000:
                return qtdTora
            else:
                print('Por valor digite uma quantidade valida de no minimo 1 m³ e no máximo 2000 m³')
        except ValueError:
            print('Digite um numero valido')

#variavel do desconto     
def desconto(qtdTora):
    try:
        if qtdTora > 2000:
            return 0
        elif 100 <= qtdTora < 500:
            return 0.04
        elif 500 <= qtdTora < 1000:
            return 0.09
        else:
            return 0.16
    except ValueError:
         print("Por favor, digite um número inteiro para a quantidade de toras.")
    return 0   

def validatransporteporte():
    while True:
        print('')
        print ('Escolha um tipo de transporteporte')
        print("1 - transporteporte Rodoviário - R$ 1000.00")
        print("2 - transporteporte Ferroviário - R$ 2000.00")
        print("3 - transporteporte Hidroviário - R$ 2500.00")
        transporte = input('>>')
        if transporte == '1':
            return 1000
        elif transporte == '2':
            return 2000
        elif transporte == '3':
            return 2500
        else:
            print('Digite uma altenativa ')
            

#codigo princial (MAIN)
print('\nBEM VINDO A MADEIREIRA DO LENHADOR ROBSON CAROLINO')
if __name__== '__main__':

    tipoMadeira = validaMadeira()#VALIÇÃO DO TIPO DE MADEIRA

    qtdTora = validaQuantidade()#VALIDÇÃO DA QUANNTIDADE

    transporte = validatransporteporte()#VALIDAÇÃO DO TRANSPORTE

    desconto = desconto(qtdTora)#VALIDÇÃO DO DESCONTO 

    total = (tipoMadeira * qtdTora * (1 - desconto)) + transporte #Calculo total 
    #Valor final 
    print(f'O total á pagar: R$ {total:.2f}')