# #Exercicícios de if, elif e else. 

# primeiro_numero = float(input("Digite o primeiro número: "))
# segundo_numero = float(input("Digite outro número: "))

# operacao = input("DIgite a operação que deseja: +, -, *, /: \n" )

# if  operacao == "+":
#     resultado = primeiro_numero + segundo_numero

# elif  operacao == "-":
#     resultado = primeiro_numero - segundo_numero

# elif operacao == "*":
#     resultado = primeiro_numero * segundo_numero

# elif  operacao == "/":
#     resultado = primeiro_numero / segundo_numero if segundo_numero != 0 else "Erro: Dvisão por 0. Digite outro número"

# else: 
#     resultado = "Oepração Invalida"

#     if resultado != "Operação Invalida":
#         print(f"O resultado entre {primeiro_numero} e {segundo_numero} é {resultado}")

# print(resultado)


# peça para o usuário a primeira e segunda nota. Calcule a média das duas notas e mostre a média na tela.
#Informe a situação do aluno e de acordo com as regras: 
# Média maior ou igual a 7-> Aprovado
# Média maior ou igual a 5 e menor que 7 -> Recuperação
# Mèdia menor que 5 -> Reprovado

media1 = float (input("Qual a sua primeria média:"))
media2 = float(input("Qual a sua segunda média: "))

media_Total = (media1 + media2) / 2

if media_Total  >= 7 :
    print(f"Aprovado com a média {media_Total}")

elif media_Total  >=5 :
      print(f"Recuperação com a média {media_Total}")
    
else:
    print(f"Reprovado, com a média {media_Total}")
    if media_Total <= 5:
         print ("Sinto muito mas você está reprovado")


    
    
    
    
