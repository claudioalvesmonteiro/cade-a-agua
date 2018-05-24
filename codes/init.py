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

#========== importar usuarios ==========#

# visualizar e mudar diretorio de trabalho
import os
cwd = os.getcwd()
os.chdir("/home/pacha/Documents/git_projects/cade-a-agua/")

# carrega lista de usuarios
listaUser = open("data/usuarios.txt")

# ler a lista e armazenar as infos em um dicionario
observadores = 

#========= inicio ==========#

# mostra o que eh
print("O 'Cadê a Água' é um programa para realizar reclamações sobre o abastecimento de água em sua cidade. Qualquer pessoas pode inserir as informações. Garantimos seu anonimato")

# input user info
print("Precisamos apenas de algumas informações para continuar")
nomeUser = input("Qual o seu nome? ")
cpfUser = input("Qual o seu CPF? ")
emailUser = input("Qual seu email? ")

#if cpfUser in observadores:
#    import observador_da_agua from *

# funcao da reclamacao
def reclama():
    tipo = ""
    localiza = ""
    reclama = int(input("1-Observei um vazamento de água na rua! /n 2-Observei uma ligação clandestina (jacaré) na rede de abastecimento! /n 3-Tá faltando água na minha casa!"))
    localiza = input("Insira o endereço em que você observou o problema (bairro, rua, número da casa à frente): ")

#========= USUARIO SIMPLES =========#

# executa usuario simples
if nomeUser not in observadores:
    print("Olá ", nomeUser, "Selecione o tipo de reclamação que você deseja fazer: ")
    reclama()

#========= USUARIO OBSERVADOR =========#

# executa observador da algumas
if nomeUser in observadores:
