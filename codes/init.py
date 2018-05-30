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

#=== usuarios ===#
listaUser = open("data/usuariosChaves.txt", 'r') # abrir arquivo
listaUser = listaUser.readlines() # ler linhas
usuarios = removeCaracter(listaUser, "\n") # remover \#
usuarios = listaDict(usuarios) # transformar em dicionario

#=== reclamacoes ===#
listaReclama = open("data/reclamacoes.txt", 'w') # abrir arquivo
reclamacoes = listaReclama.readlines() # ler linhas
reclamacoes = removeCaracter(listaReclama, "\n") # remover \#

#========= INICIO ==========#

# mostraR o que eh
print("O 'Cadê a Água' é um programa para realizar reclamações sobre o abastecimento de água em sua cidade. Qualquer pessoas pode inserir as informações. Garantimos seu anonimato")

# input user info
print("Precisamos apenas de algumas informações para continuar")
nomeUser = input("Qual o seu nome? ")
cpfUser = input("Qual o seu CPF? ")
emailUser = input("Qual seu email? ")

#========= USUARIO SIMPLES =========#
if cpfUser not in usuarios:
    print("Olá ", nomeUser, "Selecione o tipo de reclamação que você deseja fazer: ")
    reclama = int(input("1-Observei um vazamento de água na rua! /n 2-Observei uma ligação clandestina (jacaré) na rede de abastecimento! /n 3-Tá faltando água na minha casa!"))
    localiza = input("Insira o endereço em que você observou o problema (bairro, rua, número da casa à frente): ")
    codReclama = int(reclamacao[len(reclamacao)-4]) + 1 # codigo da ultima reclamacao registrada + 1
    reclamacao = [codReclama, cpfUser, reclama, localiza]
    reclamacoes.append(reclamacao)

#========= USUARIO OBSERVADOR =========#
#if cpfUser in usuarios:
#    quebra = false
#    senhaUser = input("Olá ", nomeUser, " vimos que você é um observador da água. Para entrar na sua conta insira sua senha: ")
#    while quebra == false:
#        if senhaUser == usuarios[cpfUser]:
#            menuObservador():
#            quebra = true
#        else:
#            input("Senha incorreta. Digite novamente: ")

#========= SALVAR INFOS ==========#

#==== reclamacoes ====#
reclamacoesString = plusText(reclamacoes) # transformar lista em string com '\n'
listaReclama.write(reclamacoesString) # escrever as relcamacoes
listaReclama.close() # fechar arquivo

#==== usuarios ====
