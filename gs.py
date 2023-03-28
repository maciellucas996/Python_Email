import random
import string

tamanho = int(input('Digite o tamanho de senha que voce deseja: '))

#ascii envolve letrar maiusculas e minusculas, podendo escolher entre elas com ascii upper ou ascii lower
chars = string.ascii_letters + string.digits + '!@#$%¨&*()-_+'

rnd = random.SystemRandom() #os.urandom = gera numeros aleatorios a partir de fontes fornecidas pelo sistema operacional

print(''.join(rnd.choice(chars) for i in range(tamanho)))
#rnd.choice retornar uma lista com caracteres randomicos
#essa linha manda o python pegar essa lista de caracteres genericos, gerados pela variavel 'chars'
#o for i in range(tamanho) diz que a cada i dentro do tamanho = 16, ele vai gerar um novo caracter
#resultando em uma senha aleatoria de 16 caracteres