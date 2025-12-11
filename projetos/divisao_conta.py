print('Divisão De Conta')
pergunta=int(input('Quantas pessoas irão dividir está conta ? '))
total=float(input('Qual o valor total da conta ? R$ '))
calcula= total/pergunta
print(f'O Valor a ser dividido é R${calcula :.2f}')

'Versão que só aceita numeros possiveis'
#while True:
 #pergunta=int(input('Quantas pessoas irão dividir está conta ? '))
 #if pergunta <= 0:
  #print('Este Valor não se pode ser divido ')
  #continue
 #total=float(input('Qual o valor total da conta ? R$ '))
 #calcula= total/pergunta
 #print(f'O Valor a ser dividido é R${calcula :.2f}')
 #break