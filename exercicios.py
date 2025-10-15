"Exercicio-1"
#print ('Olá mundo')

"Exercio-2"
''' nome= input ('Seja Bem vindo,Qual o seu nome?')
print ( 'É um prazer te conhecer!!, {} !' .format (nome))'''

"Exercicio-3"
#print ('--__desaio= soma__--_')
#ni1=  int (input ('Digite um numero'))
#ni2= int (input('Digite um numero'))

#soma = ni1 + ni2
#print ( 'a soma dos numeros é',soma )
"ou"
#print("a soma dos numeros {} e {} vale = {}".format(ni1,ni2,soma))
 
#Números#
num=(int) = -7,7,-87
num=(float) = 6.4,6.34,7.0
num=(bool) = True,False
num=(str) = ('Texto, ex:Olá')

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



'Exercicio-4'
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
del int
n= int(input("Digite um número:"))
sn2=int(input ('digite outro: '))
so= n+sn2
m= n*sn2
d=n/sn2
di=n//sn2
po=n**sn2
raíz=n**(1/2)
print('OS resultados são, soma: {}, multiplicação :{}, divisão: {}, divisão inteira: {},potencia: {},raíz: {}'.format(so,m,d,di,po,raíz))