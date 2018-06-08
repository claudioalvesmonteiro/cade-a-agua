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

#====================== PROCESSANDO AS INFOS =====================#

#======== criar dict dados usuarios =========#
def maniUserData(user_data):
    # remover "\n"
    user_data = removeCaracter(user_data, "\n")
    # criar lista das infos
    listaUser = []
    for info in user_data:
        usuarioInfo = ""
        for caracter in info:
            if caracter == ";":
                listaUser.append(usuarioInfo)
                usuarioInfo = ""
            else:
                usuarioInfo += caracter
    # criar dicionario das infos
    dict_user = {}
    cont = 7
    while cont < len(listaUser):
        dict_user[listaUser[cont]] = (listaUser[cont+1],listaUser[cont+2],listaUser[cont+3], listaUser[cont+4],listaUser[cont+5], int(listaUser[cont+6]))
        cont += 7
    return dict_user

#======== criar lista dados reclamacoes ========#
def maniReclamaData(reclamacoes):
    # remover "\n"
    reclamacoes = removeCaracter(reclamacoes, "\n") # remover \#
    # criar lista de reclamacoes
    cont = 0
    lista_reclama = []
    while cont < len(reclamacoes):
        lista_reclama.append([reclamacoes[cont], reclamacoes[cont+1], reclamacoes[cont+2], int(reclamacoes[cont+3])])
        cont += 4
    return lista_reclama

#======================= RECLAMACAO =====================#

def Reclamacao(reclamaNew, reclamacoes, user_nome, user_cpf):
    print("Selecione o tipo de reclamação que você deseja fazer:\n1-Observei um vazamento de água na rua!\n2-Observei uma ligação clandestina (jacaré) na rede de abastecimento!\n3-Tá faltando água na minha casa!")
    reclama = str(int(input("Digite o número da reclamação: ")))
    localiza = input("Insira o endereço em que você observou o problema (bairro, rua, número da casa à frente): ")
    codReclama = str(int(reclamacoes[len(reclamacoes)-4])+1) # codigo da ultima reclamacao registrada + 1
    rec = [codReclama, user_cpf, reclama, localiza]
    for info in rec:
        reclamaNew.append(info)

#========= salvar infos de usuarios ==========#
# Atencao!! INCLUIR POSSIBILIDADE DE MAIS DE UMA RECLAMACAO
def atualizarUser(user_data, reclamaNew, user_cpf):
    user_data_att = user_data
    # att lista de codigos reclamacao
    codes_rec = user_data[user_data.index(user_cpf)+5]
    codes_rec += "," + reclamaNew[0]
    user_data_att[user_data.index(user_cpf)+5] = codes_rec
    # att contagem de reclamacoes
    cont_rec = int(user_data[user_data.index(user_cpf)+6]) + 1
    user_data_att[user_data.index(user_cpf)+6] = cont_rec
    # retornar
    return user_data_att

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

# ATENCAO DESENVLVER PARA user_data
# acrescenta texto ao fim de cada objeto numa lista
def plusTextUser(lista):
    stringLista = ""
    for caso in lista:
        casoNovo = ""
        casoNovo = caso + "\n"
        stringLista += casoNovo
    return stringLista

#================= FUNCIONALIDADES OBSERVADOR ==============#

#========== Visualizar Ranking =========#

# contar quantas no total (ultima rec + 1)
# contar quantas vezes cada cpf se repete
# parear com infos de usuarios
# obsevadoresAnonimos = total - totalDosObservadores
# lista contagem por nome do observador + obsevadoresAnonimos

#========== Visualizar Infos Pessoais =========#
def visuInfoUser(user_data, user_cpf):
    infos = user_data[user_data.index(user_cpf):user_data.index(user_cpf)+7]
    print("\n", "CPF: ", user_cpf, "\n" ,"Nome: ", infos[2], "\n" ,"Nível de acesso: ", infos[3], "\n",
    "Email: ", infos[4], "\n" ,"Número de reclamações realizadas: ", infos[6], "\n")

#========== Baixar base de dados das Reclamacoes =========#

#========== MENU OBSERVADOR ============#
def menuObservador(user_data, reclamaNew, reclamacoes, user_nome, user_cpf):
    pare = False
    while pare == False:
        print("Olá, ", user_nome, "! Bem vind@ de volta. O que você deseja?\n1-Visualizar minhas informações pessoais\n2-Fazer uma reclamação\n3-Sair")
        fazer = int(input("Digite o numero da ação: "))
        if fazer == 1:
            visuInfoUser(user_data, user_cpf)
        elif fazer == 2:
            Reclamacao(reclamaNew, reclamacoes, user_cpf)
        elif fazer == 3:
            pare = True
        else:
            print("Código de ação inválido")

# trasnforma lista em dicionario em pares
#def dictUserCount(lista):
#    cont = 0
#    dicionario = {}
#    while (cont*2+1) < len(lista):
#        dicionario[lista[cont*2]] = lista[cont*2+1]
#        cont += 1
#    return dicionario
