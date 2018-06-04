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
#============ Input Reclamacao ===========#
def reclamacao(reclamacoes, user_nome, cpf_user):
    reclamacao = []
    print("Olá ", user_nome, "Selecione o tipo de reclamação que você deseja fazer:\n1-Observei um vazamento de água na rua!\n2-Observei uma ligação clandestina (jacaré) na rede de abastecimento!\n3-Tá faltando água na minha casa!")
    reclama = str(int(input("Digite o número da reclamação: ")))
    localiza = input("Insira o endereço em que você observou o problema (bairro, rua, número da casa à frente): ")
    codReclama = str(int(reclamacoes[len(reclamacoes)-4])+1) # codigo da ultima reclamacao registrada + 1
    reclamacao = [codReclama, cpf_user, reclama, localiza]
    return reclamacao

#============ PROCESSANDO AS INFOS =================#

#======== manipular dados usuarios =========#
def maniUserData(user_data):
    listaUser = []
    for usuario in user_data:
        usuarioInfo = ""
        for caracter in usuario:
            if caracter == ";":
                listaUser.append(usuarioInfo)
                usuarioInfo = ""
            else:
                usuarioInfo += caracter
    return listaUser


#============== Ferramentas Gerais ===============#

# retorna uma lista de objetos, sem um determinado caracter
def removeCaracter(lista,caracter):
    listaFinal = []
    for objeto in lista:
        objetoMani = ""
        for caract in objeto:
            if caract != caracter:
                objetoMani += caract
        listaFinal.append(objetoMani)
    return listaFinal

# acrescenta texto ao fim de cada objeto numa lista
def plusText(lista):
    stringLista = ""
    for caso in lista:
        casoNovo = ""
        casoNovo = caso + "\n"
        stringLista += casoNovo
    return stringLista

#================= FUNCIONALIDADES OBSERVADOR ==============#

#========== Visualizar Hanking =========#
#

#========== Visualizar Infos Pessoais =========#

#========== Baixar base de dados das Reclamacoes =========#

#========== MENU OBSERVADOR ============#
#def menuObservador():
#    senhaUser = input("Olá ", nomeUser, " vimos que você é um observador da água. Para entrar na sua conta insira sua senha: ")
#    if senhaUser

# trasnforma lista em dicionario em pares
#def dictUserCount(lista):
#    cont = 0
#    dicionario = {}
#    while (cont*2+1) < len(lista):
#        dicionario[lista[cont*2]] = lista[cont*2+1]
#        cont += 1
#    return dicionario
