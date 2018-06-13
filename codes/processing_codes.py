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

#====================== PROCESSANDO AS INFOS ======================#

#======== criar dict dados usuarios =========#
def maniUserData(user_data):
    ''' Remove o '\n' da string com as informacoes. Cria uma lista com as infos,
    separadas por ';' e cria um dicionario de usuarios com o cpf como identificador e
    informacoes como conteudo de uma tupla. Retorna o dicionario.
    '''
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

# descriptografar
def descriptoOpen(reclama_data):
    chave_privada = open("chaves/chavePrivada.txt", 'r')
    chavePrivada = chave_privada.readlines()
    chavePrivada = removeCaracter(chavePrivada, "\n")
    print(chavePrivada)
    reclamacoes = []
    for info in reclama_data:
        informacao = ""
        for caracter in info:
            print(caracter)
            x = chr((int(caracter)^int(chavePrivada[0])) % int(chavePrivada[1]))
            informacao += x
        reclamacoes.append(informacao)
    return reclamacoes

def maniReclamaData(reclama_data, criptografia):
    ''' Remove o '\n' da string com as reclamacoes.
        Cria uma lista de listas, cada uma armazenando as informacoes
        de uma reclamacao.
    '''
    # remover "\n"
    reclama_data = removeCaracter(reclama_data, "\n") # remover \#
    # descriptografar
    if criptografia = True:
        reclamacoes = descriptoOpen(reclama_data)
    elif criptografia = False:
        reclamacoes = reclama_data
    # criar lista de reclamacoes
    cont = 0
    lista_reclama = []
    while cont < len(reclamacoes):
        lista_reclama.append([reclamacoes[cont], reclamacoes[cont+1], reclamacoes[cont+2], reclamacoes[cont+3]])
        cont += 4
    return lista_reclama

#====================== LOGIN ============================#
def loginUsuario(user_data):
    ''' Verifica se o CPF e a senha constam devidamente na base.
        Retora o CPF do usuario.
    '''
    # verifica cpf
    quebra = False
    user_cpf = input("Olá! Digite seu CPF para entrar na sua conta: ")
    while quebra == False:
        if user_cpf in user_data:
            user_senha = input("Agora insira sua senha: ")
            quebra = True
        else:
            user_cpf = input("CPF não consta em nossa base :( digite novamente: ")
    quebraB = False
    while quebraB == False:
        if user_senha != user_data[user_cpf][0]:
            user_senha = input("Senha incorreta. Digite novamente: ")
        else:
            quebraB = True
    return user_cpf

#======================= RECLAMACAO =====================#
def Reclamacao(reclamaCod, reclamaNew, user_cpf):
    ''' Interacao com o usuario para armazenar uma nova reclamacao na base
    '''
    print("Selecione o tipo de reclamação que você deseja fazer:\n1-Observei um vazamento de água na rua!\n2-Observei uma ligação clandestina (jacaré) na rede de abastecimento!\n3-Tá faltando água na minha casa!")
    reclama = input("Digite o número da reclamação: ")
    localiza = input("Insira o endereço em que você observou o problema (bairro, rua, número da casa à frente): ")
    codReclama = reclamaCod + 1 # codigo da ultima reclamacao registrada + 1
    rec = [str(codReclama), user_cpf, reclama, localiza]
    reclamaNew.append(rec)

#======================= CADASTRAR OBSERVADOR ===================#
def cadastroObservador(user_data, user_cpf):
    ''' Input das informacoes do usuario. Loop para testar compatibilidade de senhas inseridas.
        Armazena o novo usuario na base de usuarios.
    '''
    # input infos do usuario
    user_nome = input("Crie seu nome de usuário: ")
    user_email = input("Digite seu email: ")
    user_senha = input("Digite sua senha de acesso: ")
    user_senha2 = input("Repita a senha, por favor: ")
    # testar senhas
    fluxo = False
    while fluxo == False:
        if user_senha == user_senha2:
            fluxo = True
        else:
            print("Senhas não conferem")
            user_senha = input("Digite sua senha de acesso: ")
            user_senha2 = input("Repita a senha, por favor: ")
    # armazeanar infos
    user_data[user_cpf] = (user_senha, user_nome, user_email, "observador","", 0)


#============== Ferramentas Gerais ===============#

# retorna uma lista de objetos, sem um determinado caracter
def removeCaracter(lista,caracter):
    ''' Cria uma lista que recebe as informacoes da uma lista dada,
        sem um determinado caracter.
    '''
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
    ''' Retorna uma lista com os objetos de uma dada lista,
        acrescentado um '\n' ao final de cada objeto na lista.
    '''
    stringLista = ""
    for caso in lista:
        casoNovo = ""
        casoNovo = caso + "\n"
        stringLista += casoNovo
    return stringLista

#======================== FUNCIONALIDADES OBSERVADOR =======================#

#========== Visualizar Ranking =========#
def visuRanking(user_data):
    ''' Cria uma lista que recebe o nome de cada usuario e suas respectivas
    contagens de reclamacoes. Cria uma lista que recebe os valores da lista anterior ordenado.
    Dar um print na tela com os usuarios e o numero de contribuicoes, ordenado do maior para o menor
    '''
    rankLista = []
    for usuario in user_data:
        rankLista.append([user_data[usuario][1], user_data[usuario][5]])
    # lista de contagem
    listaCont = []
    listaContB = []
    for caso in rankLista:
        listaCont.append(caso[1])
        listaContB.append(caso[1])
    # lista ordenada
    listaOrd = []
    while len(listaOrd) < len(rankLista):
        maximo = max(listaContB)
        listaOrd.append(rankLista[listaCont.index(maximo)])
        listaContB.remove(maximo)
    print("\n")
    for usuario in listaOrd:
        print(usuario[0], ": ", usuario[1], "Contribuições")

#========== Visualizar Infos Pessoais =========#
def visuInfoUser(user_data, user_cpf):
    print("\n", "CPF: ", user_cpf, "\n" ,
    "Nome de Observador: ", user_data[user_cpf][1], "\n" ,
    "Nível de acesso: ",  user_data[user_cpf][3], "\n",
    "Email: ", user_data[user_cpf][2], "\n" ,
    "Número de contribuições realizadas: ",  user_data[user_cpf][5], "\n")

#========== Baixar Dados das Reclamacoes =========#
def downloadReclamacoes(reclamacoes):
    # criar string a ser escrita no aquivo
    dataReclama = "codigo_reclamacao;tipo_reclamacao;endereco_reclamacao;"
    for reclama in reclamacoes:
        for info in reclama:
            if info != reclama[1]:
                dataReclama += info + ";"
        dataReclama += "\n"
    # criar base de reclamacoes
    base_reclama = open("data/base_reclamacoes.csv", 'w') # abrir arquivo
    base_reclama.write(dataReclama)
    base_reclama.close()
    print("Dados das reclamações baixados!")

#=============== Atualizar Infos ================#
def atualizaInfos(user_data, user_cpf):
    ''' Dar um print das opcoes disponíveis e pede input da opcao selecionada.
        Opcao 1 Atualiza as senhas do usuario na base. Opcao 2 atualiza o nome de usuarios
        Opcao 3 atualiza o email do usuario e opcao 4 sai da funcao.
    '''
    fluxo = True
    while fluxo == True:
        print("Qual das seguintes informações você deseja atualizar:\n1-Senha\n2-Nome de Observador\n3-Email\n4-Sair")
        atualiza = int(input("Digite o número da ação: "))
        # atualizar senha
        if atualiza == 1:
            senhaNova = input("Digite a nova senha: ")
            senhaNovaB = input("Repita a senha, por favor: ")
            # testar senhas
            qubra = False
            while quebra == False:
                if senhaNova == senhaNovaB:
                    qubra = True
                else:
                    print("Senhas não conferem")
                    user_senha = input("Digite sua senha de acesso: ")
                    user_senha2 = input("Repita a senha, por favor: ")
            user_data[user_cpf] = (senhaNova, user_data[user_cpf][1], user_data[user_cpf][2], user_data[user_cpf][3], user_data[user_cpf][4], user_data[user_cpf][5])
            print("Senha atualizada!")
        # atualizar nome de usuario
        elif atualiza == 2:
            nomeNovo = input("Digite seu novo nome de observador: ")
            user_data[user_cpf] = (user_data[user_cpf][0], nomeNovo, user_data[user_cpf][2], user_data[user_cpf][3], user_data[user_cpf][4], user_data[user_cpf][5])
            print("Nome de usuário atualizado!")
        # atualizar email
        elif atualiza == 3:
            emailNovo = input("Digite seu novo email: ")
            user_data[user_cpf] = (user_data[user_cpf][0], user_data[user_cpf][1], emailNovo, user_data[user_cpf][3], user_data[user_cpf][4], user_data[user_cpf][5])
            print("Email atualizado!")
        # sair
        elif atualiza == 4:
            fluxo = False

#========== menu observador ============#
def menuObservador(user_data, user_cpf, reclamaCod, reclamaNew, reclamacoes):
    ''' Menu do usuario Observador. Dar print na tela das opcoes.
        Opcao1 chama a funcao de reclamacao. Opcao 2 chama a opcao de
        visualizar o Ranking de Observadores. Opcao 3 chama funcao para
        visualizar informacoes do usuario. Opcao 4 chama funcao para
        atualizar informacoes do usuario e Opcao 5 salva as reclamacoes em formato
        de planilha .CSV e opcao 6 encerra a funcao.
    '''
    pare = False
    while pare == False:
        print("\nMenu do Observador da Água: \n1-Fazer uma reclamação\n2-Visualizar o ranking de observadores da Água\n3-Visualizar minhas informações pessoais\n4-Atualizar informações pessoais\n5-Baixar dados de reclamacoes\n6-Sair")
        fazer = int(input("Digite o numero da ação: "))
        # opcoes
        if fazer == 1:
            Reclamacao(reclamaCod, reclamaNew, user_cpf)
        elif fazer == 2:
            visuRanking(user_data)
        elif fazer == 3:
            visuInfoUser(user_data, user_cpf)
        elif fazer == 4:
            atualizaInfos(user_data, user_cpf)
        elif fazer == 5:
            downloadReclamacoes(reclamacoes)
        elif fazer == 6:
            pare = True
        else:
            print("Código de ação inválido")

#======================== FUNCIONALIDADES DESENVOLVEDOR =======================#

#=============== Remover Observador da Base ================#
def removeObservador(user_data):
    ''' Input do CPF do usuario a ser removido da base.
        Verifica se CPF exite na base. Remove usuario do CPF dado, da base de usuarios.
    '''
    remove_cpf = input("Digite o número de CPF do Observador a ser retirado: ")
    quebra = False
    while quebra == False:
        if remove_cpf in user_data:
            user_data.pop(remove_cpf, None)
            print("Observador removido com sucesso")
            quebra = True
        else:
            remove_cpf = input("CPF não consta na base. Digite novamente: ")

#=============== Transformar Observador em Desenvolvedor ================#
def transDesenvolvedor(user_data):
    ''' Input do CPF de um observador a ser transformado em desenvolvedor.
        Transforma o tipo de de usuario para desenvolvedor.
    '''
    desenvolve_cpf = input("Digite o número de CPF do Observador a ser transformado em Desenvolvedor: ")
    quebra = False
    while quebra == False:
        if desenvolve_cpf in user_data:
            user_data[desenvolve_cpf] = (user_data[desenvolve_cpf][0], user_data[desenvolve_cpf][1], user_data[desenvolve_cpf][2], "desenvolvedor" , user_data[desenvolve_cpf][4], user_data[desenvolve_cpf][5])
            print("Observador atualizado para Desenvolvedor")
            quebra = True
        else:
            desenvolve_cpf = input("CPF não consta na base. Digite novamente: ")

#====================== Menu Desenvolvedor ========================#
def menuDesenvolvedor(user_data):
    ''' Menu Desenvolvedor. Dar print das opcoes na tela. Input das opcoes disponiveis.
        Opcao 1 chama funcao para remover observador. Opcao 2 transforma observador em desenvolvedor.
        Opcao 3 encerra a funcao.
    '''
    pare = False
    valido = True
    while pare == False:
        print("\nMenu Desenvolvimento: \n1-Remover Observador dos usuários\n2-Transformar Observador em Desenvolvedor\n3-Sair")
        if valido == True:
            fazer = int(input("Digite o numero da ação: "))
        # opcoes
        if fazer == 1:
            removeObservador(user_data)
        elif fazer == 2:
            transDesenvolvedor(user_data)
        elif fazer == 3:
            pare = True
        else:
            fazer = int(input("Digite um numero de ação válido: "))
            valido = False

#=========================== SALVAR INFOS ===========================#

#====================== reclamacoes =====================#

# criptografia
def encriptSave(reclamaNew):
    ''' Abre chave publica. Executa calculo de criptografia RAS
        para cada caracter da lista reclamaNew. Retorna lista de
        reclamacoes criptografada.
    '''
    # abrir chaves
    chavePublica = open("chaves/chavePublica.txt")
    chavesPub = chavePublica.readlines()
    chavePublica.close()
    chavesPub = removeCaracter(chavesPub,"\n")
    # executar calculo
    criptoReclamacoes =[]
    for reclama in reclamaNew:
        reclamaEncript = []
        for info in reclama:
            infoEncript = ""
            for caracter in info:
                criptoCaracter = str(ord(caracter)^int(chavesPub[0]) % int(chavesPub[1]))
                infoEncript += criptoCaracter
            reclamaEncript.append(infoEncript)
        criptoReclamacoes.append(reclamaEncript)

# escrever reclamacoes
def stringReclamacoes(reclamaNew, criptografia):
    ''' Transforma lista de novas reclamacoes em string e salva no
        arquivo de reclamacoes de forma criptografada ou não.
    '''
    # criptografia
    if criptografia = True:
        lista_reclama = encriptSave(reclamaNew)
    elif criptografia = False:
        lista_reclama = reclamaNew
    # criar string
    stringReclamacao = ""
    for reclamacao in lista_reclama:
        for info in reclamacao:
            stringReclamacao += info + "\n"
    return stringReclamacao



#=========  usuarios ==========#
def stringUsuarios(user_data, user_cpf, reclamaNew, lista_user_data, criptografia):
    ''' Verifica se infos dos usuarios precisam serem atualizadas,
        com base em novas reclamacoes. Cria uma string a ser escrita
        em formato de leitura .CSV. Escreve string no arquivo e fecha o mesmo.
    '''
    # atualizar user_data por reclamacoes
    if len(reclamaNew) > 0 and user_cpf in user_data:
        for reclama in reclamaNew:
            user_data[reclama[1]] = (user_data[reclama[1]][0], user_data[reclama[1]][1], user_data[reclama[1]][2],
            user_data[reclama[1]][3], str(user_data[reclama[1]][4]+ str(reclama[0])), str(user_data[reclama[1]][5]+1))
    # string write
    userDataWrite = ""
    for usuario in user_data:
        userDataWrite += usuario + ";" + user_data[usuario][0] + ";" +user_data[usuario][1] + ";" +user_data[usuario][2] + ";" +user_data[usuario][3] + ";" +user_data[usuario][4] + ";" + str(user_data[usuario][5])+";\n"
    return userDataWrite
