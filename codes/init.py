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
lista_user_data = open("data/usuarios.txt", 'r+') # abrir arquivo
user_data = lista_user_data.readlines() # ler linhas
user_data = maniUserData(user_data) # dicionario de dados dos usuarios
user_data_len = len(user_data)

#================ reclamacoes ================#
lista_reclama = open("data/elementos.txt", 'r+') # abrir arquivo
reclamacoes = lista_reclama.readlines() # ler linhas
reclamacoes = maniReclamaData(reclamacoes) # criar dicionario de reclamacoes

# codigo ultima reclamacao
reclamaCod = int(reclamacoes[len(reclamacoes)-1][0])
# novas reclamacoes
reclamaNew = []

#========= INICIO ==========#

# mostrar o que eh a plataforma e input cadastro
print("O 'Cadê a Água' é uma plataforma para realizar reclamações sobre o abastecimento de água em sua cidade. Qualquer pessoa pode inserir as informações. Garantimos seu anonimato.\n")
print("Vocẽ já é cadastrado como um 'observador da água'?")
cadastro = int(input("Se sim, digite 1, se não, digite 2: "))

# testa cadastro correto
fluxo = False
while fluxo == False:
    if cadastro == 1 or cadastro == 2 or cadastro == 0:
        fluxo = True
    else:
        cadastro = int(input("Digite 1 se você é cadastrado na plataforma ou 2 se não é cadastrado: "))

#================ USUARIO SIMPLES ===============#
if cadastro == 2:
    print("Você deseja se cadastrar como um 'observador da água' ou apenas reportar um problema de abastecimento de água? Para conhecer os benefícios de ser um observador da água gratuitamente, acesse o link: https://github.com/claudioalvesmonteiro/cade-a-agua \n")
    simples = int(input("Para se cadastrar digite 1, para apenas reportar um problema digite 2: "))
    # testa cadastro correto
    fluxo = False
    while fluxo == False:
        if simples == 1 or simples == 2:
            fluxo = True
        else:
            simples = int(input("Digite 1 para se cadastrar e 2 para apenas reportar um problema: "))
    # opcoes
    if simples == 1:
        user_cpf = input("Digite seu CPF (mantemos sigilo total): ")
        cadastroObservador(user_data, user_cpf)
        print("Parabéns! Agora você faz parte do grupo de observador de água")
        cadastro = int(input("Se você deseja acessar as opções de observador digite 1. Caso queira sair, digite 2: "))
    if simples == 2:
        user_cpf = input("Digite seu CPF (mantemos sigilo total): ")
        Reclamacao(reclamaCod, reclamaNew, user_cpf)

#================ USUARIO OBSERVADOR ================#
if cadastro == 1:
    user_cpf = loginUsuario(user_data)
    # Abre menuObservador
    menuObservador(user_data, user_cpf, reclamaCod, reclamaNew, reclamacoes)

#================= USUARIO DESENVOLVEDOR ================#
if cadastro == 0:
    # verifica cpf e senha
    user_cpf = loginUsuario(user_data)
    if user_data[user_cpf][3] == "desenvolvedor":
        # menuDesenvolvedor
        fluxoDes = menuDesenvolvedor(user_data)

#========= SALVAR INFOS ==========#
if reclamaNew != []:
    saveReclamacoes(reclamaNew, lista_reclama)
# usuarios
if user_cpf in user_data:
    saveUsuarios(user_data, user_cpf, reclamaNew, lista_user_data)

#==== mensagem final ====#
print("\nAgradecemos sua colaboração! Para saber mais sobre nosso trabalho acesse: https://observatoriosar.wordpress.com/")
