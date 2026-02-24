# salario_hora = 20
# horas_trabalhadas = 40
# bonus = 100.00


# salario_semanal = (salario_hora*horas_trabalhadas) + bonus

# print ("Meu salário semanal é ", salario_semanal)

# salario_mensal = salario_semanal * 4

# print ("O seu salário mensal é ", salario_mensal)


#Como concatecar (as informações tem que ser string(texto))

# mes = "12"
# ano = "2026"
# print(mes+ ano)

# #como escrever uma string com uma variavel junto, sem ter que ficar separando por "" e virgulas


# mes = "12"
# ano = "2026"
# print(f"Qual mês estamos {mes} e no ano {ano}")



# valor1 = 10
# valor2 = 20

# somar= valor1+valor2
# subtrair = valor1 - valor2
# divisao=valor1 / valor2
# multiplicacao = valor1 * valor2
# resto_da_divisao = valor1 // valor2

# print(somar, divisao, subtrair,divisao, multiplicacao)


# idade = input ("Qual é a sua idade? ")
# if idade ==10:
#     print(idade)
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")


# valor = 10

# if valor == 1:
#     print ("Os valores são iguais")
    

# if valor != 5:
#     print("Os valores são diferentes")

# if valor > 10:
#     print ("Os valores são diferentes")



#     valor1 =int (input ("Digite um número: "))
#     valor2 = float (input("Digite um número quebrado: "))
#     nome = input("Digite seu nome: ")
#     print(valor1, valor2, nome)


#Ex 01 - Iremos somar dois valores inteiros, peça dois valores ao usuário, some, subtraia, multiplique e divida esses dois valores e exiba o resultado desses valores com o texto 
# "A soma dos valores é" coloque a variavel


nmr1 = int(input("Digite um valor: "))
nmr2 = int (input ("Digite outro valor: "))

soma = nmr1+nmr2
sub = nmr1-nmr2
mult = nmr1*nmr2
div = nmr1 = nmr2

print ("A soma {}, subtração {}. a multiplicação {} e a divisão {} dos valores é ".format(soma, sub, mult,div))

