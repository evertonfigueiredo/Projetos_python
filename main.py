import time

AlturaMaxima = float(1.5)

nome = str(input('Qual o seu nome? '))
print('Olá',nome,'como você esta?')

time.sleep(1.5)
print('Vamos saber se você pode acessar esse brinquedo...')

time.sleep(1.5)
altura = float(input('Digite sua altura: '))

print('Analisando................')
time.sleep(2.5)
print("")

if altura >= AlturaMaxima:
    print(nome,', você esta autorizado a acessar esse brinquedo!!! - DIVIRTASSE -')
else:
    print(nome,' desculpe mas sua altura é de ',altura,', altura incompativel com esse brinquedo. - SINTO MUITO')