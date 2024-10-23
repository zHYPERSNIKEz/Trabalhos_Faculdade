
#tela de boas vindas
print('SISTEMA DESENVOLVIDO POR ROBSON CAROLINO')

#Verificação de plano inicial do cliente e idade 
valorBase = float(input('Digite o valor base do plano: '))
idade = int(input('Digite sua idade: '))

#a parte que vai determinar à qual categoria o cliente pertence com base a sua idade
if 0 <= idade < 19 :
    percentual = 100
   
elif 19 <= idade < 29 :
   percentual = 150
   
elif 29 <= idade < 39:
   percentual = 225 
   

elif 39 <= idade < 49:
   percentual = 240 
   

elif 49 <= idade < 59:
  percentual = 350
   
else:
    percentual = 600
    
valorMensal = (valorBase * (percentual/100))

#tela de saida

print(f'O valor mensal é de : {valorMensal}')

