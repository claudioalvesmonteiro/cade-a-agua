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

#========== importar usuarios e funcoes ==========#

# importar funcionalidades
import os
os.chdir("/home/pacha/Documents/git_projects/cade-a-agua/codes")
from observador_da_agua import *
from processing_codes import *

# visualizar e mudar diretorio de trabalho
cwd = os.getcwd()
os.chdir("/home/pacha/Documents/git_projects/cade-a-agua/")

# carregar e ler lista de usuarios
listaUser = open("data/usuariosChaves.txt")
listaUser = listaUser.readlines()

# remover \n e criar dicionario
usuarios = removeCaracter(listaUser, "\n")

for i in usuarios:


# separar as infos dos usuarios
#usuariosInfo = []
#for user in listaUser:
#    info = ""
#    for caracter in user:
#        if caracter != ";":
#            info += caracter
#        else:
#            usuariosInfo.append(info)
#            info = ""

#========= INICIO ==========#

# mostraR o que eh
print("O 'Cadê a Água' é um programa para realizar reclamações sobre o abastecimento de água em sua cidade. Qualquer pessoas pode inserir as informações. Garantimos seu anonimato")

# input user info
print("Precisamos apenas de algumas informações para continuar")
nomeUser = input("Qual o seu nome? ")
cpfUser = input("Qual o seu CPF? ")
emailUser = input("Qual seu email? ")

#========= USUARIO SIMPLES =========#

# funcao da reclamacao
def reclama():
    tipo = ""
    localiza = ""
    reclama = int(input("1-Observei um vazamento de água na rua! /n 2-Observei uma ligação clandestina (jacaré) na rede de abastecimento! /n 3-Tá faltando água na minha casa!"))
    localiza = input("Insira o endereço em que você observou o problema (bairro, rua, número da casa à frente): ")

# executa usuario simples
if nomeUser not in observadores:
    print("Olá ", nomeUser, "Selecione o tipo de reclamação que você deseja fazer: ")
    reclama()

#========= USUARIO OBSERVADOR =========#

# executa observador da algumas
if nomeUser in observadores:
    senhaUser = input("Olá ", nomeUser, " vimos que você é um observador da água. Para entrar na sua conta insira sua senha: ")
    if senhaUser

#========= ARMAZENAR INFOS ==========#
