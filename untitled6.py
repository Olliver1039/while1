# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JJ3hIYmy3Sl0KW0roVy5HWhboeS4lQoY

Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

nota = float(input("digite uma nota e conrvete o valor para um ponto flutuante: "))
while nota > 1534 or nota < 0:
    nota = float(input("digite uma senha valida: "))
print("Sucesso")

"""Entra em um loop enquanto a nota estiver fora do interval
o permitido menor que 0 ou maior que 10
"""

linhas = (input("diite um numero de um a dez: "))
nota = int(input("digite novamente o numero: "))
contador =  0,1,2,3,4,5,6,7,8,9,10
print("0,1,2,3,4,5,6,7,8,9,10")

"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações"""

nome = (input("digite um nome: "))
print("nome de usuario correto: ")
senha = (input("digite uma senha: "))
print("Sucesso")

"""Faça programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações"""

usuario = (input("digite senha de usuario: "))
print("nome de usuario incorreto")
senha = ("digite uma senha de 8 caracteres: ")
print("erro, senha nao pode ser mesma que o nome de usuario")

"""Escreva um programa que conte de 1 a 10 e imprima cada número"""

numero = int(input("digite um numero de zero a dez: "))
print("0,1,2,3,4,5,6,7,8,9,10: ")
int(input("digite"))

"""Escreva um programa que solicite ao usuário que insira um número e, em
seguida, imprima todos os números de 1 até esse número.
"""

numero = int(input("Escreva um numero que solicite ao usuario e em seguida imprima todos os numeros de 1 ate esse numero: "))
numero = ("numero escolhido e 10: ")
print("0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15: ")
while nota > 10 or nota < 0:
  print("numero digitado e?: ")

"""Escreva um programa que solicite ao usuário que insira um número e, em
seguida, imprima todos os números pares de 2 até esse número.
"""

numero = int(input("Escreva um numero que solicite ao usuario e em seguida imprima todos os numeros de 1 ate esse numero: "))
numero = ("numero escolhido e 10: ")
print("0,2,4,6,8,10: ")
while nota > 10 or nota < 0:
  print("Sucesso")

"""Escreva um programa que solicite ao usuário que insira um número e, em
seguida, imprima a tabuada desse número até 10.
"""

numero = int(input("por favor, digite um numero: "))
contador = 1
while contador <=10:
  resultado = numero * contador
  print(f"{numero} X {contador} = {resultado}")
  contador += 1

"""Escreva um programa que solicite ao usuário que insira uma senha. O
programa deve continuar solicitando a senha até que o usuário insira a senha
correta.
"""

senha = (input("digite uma senha: "))
print("senha incorreta digite a senha novamente: ")
senha = (input("digite uma senha: "))
print("senha incorreta digite a senha novamente: ")
senha = (input("digite uma senha: "))
print("Sucesso")

"""Escreva um programa que calcule a média de uma lista de números fornecida
pelo usuário.
"""

("numeros fornecido pelo o usiario serao os resultados da conta a baixo: ")
print("some os seguintes numeros 5 + 5 e digite a baixo")
numeros = (input("numeros fornecidos pelo o usuario: "))
print("some os seguintes numeros 10 + 5 e digite a baixo")
numeros = (input("numeros fornecidos pelo o usuario: "))
print("some os seguintes numeros 10 + 10 e digite a baixo")
numeros = (input("numeros fornecidos pelo o usuario: "))
print("some os seguintes numeros 10 + 15 e digite a baixo")
numeros = (input("numeros fornecidos pelo o usuario: "))
print("resultados das contas abaixo 10,15,20,25: ")

"""Escreva um programa que solicite ao usuário que insira números até que ele
insira o número 0. Em seguida, imprima a soma de todos os números inseridos.
"""
