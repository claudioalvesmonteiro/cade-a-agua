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

#============== funcionalidades ==============#
import os
os.chdir("/home/pacha/Documents/git_projects/cade-a-agua/codes")
from processing_codes import *
os.chdir("/home/pacha/Documents/git_projects/cade-a-agua/")

#================= usuarios ==================#
lista_user_data = open("data/usuariosData.txt", 'r') # abrir arquivo
user_data = lista_user_data.readlines() # ler linhas
user_data = maniUserData(user_data) # dicionario de dados dos usuarios

#================ reclamacoes ================#
lista_reclama = open("data/reclamacoes.txt", 'r+') # abrir arquivo
reclamacoes = lista_reclama.readlines() # ler linhas
reclamacoes = maniReclamaData(reclamacoes) # criar dicionario de reclamacoes

# codigo ultima reclamacao
reclamaCod = lista_reclama[len(lista_reclama)-1][0]
# novas reclamacoes
reclamaNew = []

#========= INICIO ==========#

# mostrar o que eh a plataforma e input cadastro
print("O 'Cadê a Água' é uma plataforma para realizar reclamações sobre o abastecimento de água em sua cidade.\nQualquer pessoa pode inserir as informações. Garantimos seu anonimato.")
print("Vocẽ já é cadastrado como um 'observador da água'?")
cadastro = int(input("Se sim, digite 1, se não, digite 2: "))

# testa cadastro correto
while cadastro != 1 or cadastro != 2 or cadastro != 0:
    cadastro = int(input("Digite 1 se você é cadastrado na plataforma ou 2 se não é cadastrado: "))

#========= USUARIO OBSERVADOR =========#
if cadastro == 1:
    # verifica cpf
    quebra = False
    user_cpf = input("Olá! Digite seu CPF para entrar na sua conta: ")
    while quebra == False:
        if user_cpf in user_data:
            user_senha = input("Agora insira sua senha: ")
            quebra = True
        else:
            user_cpf = input("CPF não consta em nossa base :( digite novamente: ")
    # verifica senha e abre menuObservador
    quebraB = False
    while quebraB == False:
        if user_senha == user_data[user_data.index(user_cpf)+1]:
            menuObservador(user_data, reclamaNew, reclamacoes, user_nome, user_cpf)
            quebraB = True
        else:
            senhaUser = input("Senha incorreta. Digite novamente: ")

#========= USUARIO SIMPLES =========#
if cadastro == 2:
    print("Você deseja se cadastrar como um 'observador da água' ou apenas reportar um problema de abastecimento de água?")
    print("Para conhecer os benefícios de ser um observador da água gratuitamente, acesse o link: ")
    simples = int(input("Para se cadastrar digite 1, para apenas reportar um problema digite 2: "))
    while simples != 1 or simples != 2:
        simples = int(input("Digite 1 para se cadastrar e 2 para apenas reportar um problema: "))
#    if simples == 1:
#        cadastroObservador()
    if simples == 2:
        cpf_user = input("Digite seu CPF (mantemos sigilo total): ")
        Reclamacao(reclamaNew, reclamacoes, user_cpf)

#========= USUARIO DESENVOLVEDOR =========#
#if cadastro == 0:
#    menuDesenvolvedor()

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
