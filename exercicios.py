("Exercicio-1")
#print ('Olá mundo')

("Exercio-2")
# nome= input ('Seja Bem vindo,Qual o seu nome?')
#print ( 'É um prazer te conhecer!!, {} !' .format (nome))

("Exercicio-3")
#print ('--__desaio= soma__--_')
#ni1=  int (input ('Digite um numero'))
#ni2= int (input('Digite um numero'))

#soma = ni1 + ni2
#print ( 'a soma dos numeros é',soma )
"ou"
#print("a soma dos numeros {} e {} vale = {}".format(ni1,ni2,soma))
 
#Números#
# num=(int) = -7,7,-87
# num=(float) = 6.4,6.34,7.0
# num=(bool) = True,False
# num=(str) = ('Texto, ex:Olá')

'Exemplos'
(1)
#n= input ('Digite algo :') 
#print(n.isnumeric())
#confere se é numero ou não
(2)
#oi= input ('Digite algo :')
#print(oi.isalpha())
#confere se é letra
(3)
#opa3= input ('Digite algo:')
#print(opa3.isalnum())
#confere se é letra e numero junto
(4)
#opa= input ('Digite algo:')
#print(type(opa.isupper()))
#confere se esta maiusculo
(5)
#n = input('Digite algo: ')
#print(n.islower())
# Confere se está todo em minúsculas
(6)
#n = input('Digite algo: ')
#print(n.istitle())
# Confere se está no formato de título (Ex: “Python é Bom”)- ou Capitalizada
(7)
#n = input('Digite algo: ')
#print(n.isspace())
# Confere se contém apenas espaços em branco
(8)
#n = input('Digite algo: ')
#print(n.isdecimal())
# Confere se é decimal (números sem sinal nem ponto)
(9)
#n = input('Digite algo: ')
#print(n.isdigit())
# Confere se contém apenas dígitos (parecido com isnumeric)
(10)
#n = input('Digite algo: ')
#print(type(n))
# Mostra o tipo do dado digitado (sempre será string com input())
(11)
#n = input('Digite um número: ')
#n = int(n)  # converte para inteiro
#print(type(n))
# Mostra que agora é <class 'int'>
(12)
#txt = "Olá"  
#print(txt.isascii())
# ❌ False — o “á” NÃO faz parte da tabela ASCII



('Exercicio-4')
#print('_--_Desafio 04_--_')
#opa= input ('Digite algo:')
#print('O tipo primitivo desse valor é:', type(opa))
#print('Ele é uma letra ?', opa.isalpha())
#print('Ele é numerico ?',opa.isnumeric())
#print('Ele está maiusculo?',opa.isupper())
#print('Ele contem apenas espaços  ?', opa.isspace())
#print('Ele esta na escala ascii ?', opa.isascii())
#print('Está capitalizado ?',opa.istitle())
#"ou fazer todos eles com o format"
#n = input('Digite algo: ')
#print('Ele é um numero ? {}'.format(n.isnumeric())
 

('Operadores Aritméticos')
#+ - Adição 
#- - Subtração
#* - Multiplicação
#/ - Divisão 
#** - Potencia
#// - divisão inteira 
#% - Resto da divisão

"Ordem de precedencia"
(1)
'()'
'Resolve os parenteses'
(2)
'**'
'Resolve as potencias'
(3)
'*,/,//,%'
'Resove a multiploicação ou subtração ou divisão real ou a sobra da divisão'
(4)
'+,-'
'Resolve a soma ou subtração'

('Exemplo - 1')
(5+3*2 == 11)
#f= int(input(5+3*2))
#print(f)

('Exemplo - 2')
(3*5+4**2==31)
#s=int(input(3*5+4**2))
#print(s)

('Exemplo - 3')
(3*(5+4)**2==243)
#v=(3*(5+4)**2)
#print(v)
'outra forma de fazer Potencia'
#print(pow(4,3))

'Raíz Quadrada'
#g=int(input(144**(1/2)))
#print(g)

'Raíz Cubica'
#h=int(input(127**(1/3)))
#print(h)

'formas do format'
(1)
#nome= input('qual o seu nome ?')
#print('prazer em conhecer você {:20}!'.format(nome))
'cria um espaço entre os caracteres de 20 linhas'
(2)
#noma= input('qual o seu nome ?')
#print('prazer em conhecer você {:>20}!'.format(noma))
'Cria um espaço a direita do nome de 20 linhas'
(3)
#nome= input('qual o seu nome ?')
#print('prazer em conhecer você {:<20}!'.format(nome))
'Cria um espaço a esquerda'
(4)
#nome= input('qual o seu nome ?')
#print('prazer em conhecer você {:^20}!'.format(nome))
'Centraliza'
(5)
#nome= input('qual o seu nome ?')
#print('prazer em conhecer você {:=^20}!'.format(nome))
'Alem de centralizar coloca o sinal de igual em volta, ou outro sinal que vc colocar'


'Exemplos'
#del int
#n= int(input("Digite um número:"))
#sn2=int(input ('digite outro: '))
#so= n+sn2
#m= n*sn2
#d=n/sn2
#di=n//sn2
#po=n**sn2
#raíz=n**(1/2)
#print('OS resultados são, soma: {}, multiplicação :{}, divisão: {}, divisão inteira: {},potencia: {},raíz: {}'.format(so,m,d,di,po,raíz))
()
'(\n) - quebra a linha'

('Exercicio 5')
#del int
#no= int(input("Digite um número:"))
#print( 'analisando o valor de {}, seu antecessor é {} e seu sucessor é {}'.format(no,no -1, no +1))

('Exercicio 6')
#del int
#na= int(input("Digite um número:"))
#print('o Dobro é {} \n o Triplo  é {}\n e a Raís é {:.2f}'.format(na *2 ,na *3, na**(1/2) ))

(':.2f- coloca o tanto de numeros que quero após a virgula')

('Exercicio 7')
#del int
#no= int(input("Digite um número:"))
#ni= int(input("Digite um número:"))
#print( ' Juntanto {}, e  {} A media é {:.1f}'.format(no,ni, (no+ni)/2))


('Exercicio 8')
#no=float(input ('digite uma distancia em metros:'))
#print( 'em centimetros {}\n e em milimetros {}\n e em km {} \n em hectômetro {}\n em decâmetro{} \n em decímetro {}'.format(no *100 ,no *1000,no /100,no /100 , no /10,no *10)) 

('Exercicio 9')
#tabuada=int(input('digite um número e veja a sua tabuada:'))
#print('{} x {} = {}'.format(tabuada,1, tabuada*1))
#print('{} x {} = {}'.format(tabuada,2, tabuada*2))
#print('{} x {} = {}'.)format(tabuada,3, tabuada*3))
#print('{} x {} = {}'.format(tabuada,4, tabuada*4))
#print('{} x {} = {}'.format(tabuada,5, tabuada*5))
#print('{} x {} = {}'.format(tabuada,6, tabuada*6))
#print('{} x {} = {}'.format(tabuada,7, tabuada*7))
##print('{} x {} = {}'.format(tabuada,8, tabuada*8))
#print('{} x {} = {}'.format(tabuada,9, tabuada*9))
#print('{} x {} = {}'.format(tabuada,10, tabuada*10))
#print('-----_______---')

('Exercicio 10')
#dinheiro= float(input('digite sua quantia em R$'))
#print('Vc tem em em Dolar o valor de US${:.2f}'.format(dinheiro *0.1846))

('Exercicio 11')
#altura=float(input('Digite a altura dessa parede:'))
#largura=float(input('Agora a largura:'))
#metros=altura*largura
#print('O tamanho em Metros Quadrados é {:.0f} m² \n Então você usara {:.0f} litros.'.format(metros,metros/2))

('Exercicio 12')
#produto=float(input('Qual o preço do seu produto ? R$'))
#desconto=produto - (produto * 25/100)
#print('O produto que custava R${:.2f},com o desconto de 25% ficou R${:.2f}'.format(produto,desconto))

('Exercicio 13')
#salario=float(input('Qual o valor do se salario ? R$'))
#aumento=salario + (salario*16/100)
#print('o salario que era R${:.2f}, com 16% de aumento agora está valendo R$ {:.2f}'.format(salario,aumento))

('Praticando o Exercicio 12 -13')
#valor=float(input('Qual o valor do Produto ? R$'))
#vista= valor -(valor*50/100)
#parcelado= valor + valor*15/100
#parcela=parcelado- parcelado* 50/100
#print('Se for a vista tera um desconto de 50% e tera o valor de R${:.2f}, mas se for parcelado tera um aumento de 15% e saíra com o valor de R${:.2f}\n se for parcelado em 2x pagara o valor de R${:.2f} por mês.'.format(vista,parcelado,parcela))

('Exercicio 14')
#graus=float(input('Digite a temperatura em °C:'))
#firenit= (graus*9/5) +32
#print('A temperatura que era {:.1f} °C, Agora está {:.1f} °F'.format(graus,firenit))

('Exercico 15')
#aluguel=int(input('Quantos dias você está com o carro ?'))
#rodado=float(input('E quantos km você rodou ? '))
#print('O valor a se pagar é R${:.2f}'.format(aluguel *60 + rodado *0.15 ))

('From e Import')
#import doce 'doce = Biblioteca'
'Ele importa uma biblioteca'
#from doce import pudim
'Importa a biblioteca mas puxa um item em expecifico da blibioteca'
'math = biblioteca de matematica'
('modulos de math ')
'ceil = arredonda para cima'
'floor = arredonda para baixo'
'trunc = elimina da virgula para frente'
'pow = potencia'
'sqrt = raíz quadrada'
'factorial = fatorial'
('utilizabdo a biblioteca')
#import math
#print(math.ceil(8.5))
'Importa a Biblioteca'
#from math import sqrt
#print(sqrt(16))
'Importa a biblioteca mas eu consigo utilizar apenas oq eu quero'
#from math import sqrt, ceil
#print(sqrt (144))
#print(ceil(132.8))
'já esse importa a biblioteca + os modulos que eu escolher'
#import math
#num=int(input('Digite um numero:'))
#print(' a raiz do numero {} é {:.0f}'.format(num,math.sqrt(num)))
'metodo mais facil de se fazer a conta' 
#import math
#numero=int(input('Digite um numero:'))
#raiz=math.sqrt(numero)
#print('a raíz do número {} é {}'.format(numero,math.floor(raiz)))
'Arredonda a raiz se ela for dar um numero com virgula para menor ex=6,55 para 6'
#import math
#numero=int(input('Digite um numero:'))
#raiz=math.sqrt(numero)
#print('a raíz do número {} é {}'.format(numero,math.ceil(raiz)))
'Arredonda a raiz se ela for dar um numero com virgula para maior ex=6,55 para 7'