"""
UNIVERSIDADE FEDERAL DE PERNAMBUCO (UFPE) (https://www.ufpe.br/)
CENTRO DE FILOSOFIA E CIENCIAS HUMANAS
Graduando em Ciencia Politica
IF968 - Programacao I

Autor(a): Claudio Luis Alves Monteiro
Email: claudiomonteirol.a@gmail.com
Data: 2018-05-21

Copyright(c) 2018 Claudio Luis Alves Monteiro
"""

# carrega lista de usuarios

# mostra o que e
print("O 'Cadê a Água' é um programa para realizar reclamações sobre o abastecimento de água em sua cidade. Qualquer pessoas pode inserir as informações. Garantimos seu anonimato")

# input user info
print("Precisamos apenas de algumas informações para continuar")
nomeUser = input("Qual o seu nome? ")
CPFuser = input("Qual o seu CPF? ")

# identificar o tipo de usuario
#if CPFuser in listaUser:
#    senha = input("Olá ", nomeUser, "! ", "vimos que você é um Observador da Água. Para prosseguir na acumulação de pontos, insira sua senha: ", )

# input tipo te informacao
print("1 - Vazamento de água /n 2 - Ligação clandestina")
tipoInfo = int(input("Digite o numero da informação que você quer inserir: "))

