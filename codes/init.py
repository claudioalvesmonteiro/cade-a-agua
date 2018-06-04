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

# importar funcionalidades
import os
os.chdir("/home/pacha/Documents/git_projects/cade-a-agua/codes")
from processing_codes import *

# visualizar e mudar diretorio de trabalho
cwd = os.getcwd()
os.chdir("/home/pacha/Documents/git_projects/cade-a-agua/")

#================== usuarios ================#
# ABRIR EM MODO WRITE
lista_user_data = open("data/usuariosData.txt", 'r') # abrir arquivo
user_data = lista_user_data.readlines() # ler linhas
user_data = removeCaracter(user_data, "\n") # remover \n
user_data = maniUserData(user_data) # lista de infos

#================ reclamacoes =================#
lista_reclama = open("data/reclamacoes.txt", 'r+') # abrir arquivo
reclamacoes = lista_reclama.readlines() # ler linhas
reclamacoes = removeCaracter(reclamacoes, "\n") # remover \#
reclamaNew = []

#========= INICIO ==========#

# mostraR o que eh
print("O 'Cadê a Água' é uma plataforma para realizar reclamações sobre o abastecimento de água em sua cidade.\nQualquer pessoa pode inserir as informações. Garantimos seu anonimato.")

# voce já é cadastrado?
# sim -> menuObservador, não - quer se cadastrar gratuitamente ou apenas reportar o problema? ps: para ver as vantagens de ser um observador da agua, acesse: LINK
# sim -> cadastroObservador, não - Reclamacao Simples

# input user info
print("\nPrecisamos apenas de algumas informações para continuar:")
user_nome = input("Qual o seu nome? ")
user_cpf = input("Qual o seu CPF? ")
user_email = input("Qual seu email? ")

#========= RECLAMACAO SIMPLES =========#
if user_cpf not in user_data:
    Reclamacao(reclamaNew, reclamacoes, user_nome, cpf_user)

#========= USUARIO OBSERVADOR =========#
if user_cpf in user_data:
    quebra = False
    print("Olá ", user_nome, " vimos que você é um observador da água")
    senhaUser = input("Para entrar na sua conta, insira sua senha: ")
    while quebra == False:
        if senhaUser == user_data[user_data.index(user_cpf)+1]:
            menuObservador(user_data, reclamaNew, reclamacoes, user_nome, user_cpf)
            quebra = True
        else:
            senhaUser = input("Senha incorreta. Digite novamente: ")

#========= SALVAR INFOS ==========#
if reclamaNew != []:
    # reclamacoes
    reclamaNewStr = plusText(reclamaNew) # transformar lista em string com '\n'
    lista_reclama.write(reclamaNewStr) # escrever as relcamacoes
    lista_reclama.close() # fechar arquivo
    # usuarios
    if user_cpf in user_data:
        user_data_att = atualizarUser(user_data, reclamaNew, user_cpf)
        user_data_att = plusTextUser(user_data_att)
        lista_user_data.write(user_data_att)
        lista_user_data.close() # fechar arquivo

#==== mensagem final ====#
print("\nAgradecemos sua colaboração!\nSe você deseja se tornar um(a) observador(a) da água... chega mais")
