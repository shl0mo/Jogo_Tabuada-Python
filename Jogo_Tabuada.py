import logging
logging.basicConfig(filename='Jogo_Tabuada.log', level=logging.DEBUG,
                       format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')

from random import randint

def num_ad_sub(acertos):
    if (acertos >= 15 and acertos <= 40): return randint(10,99)
    elif (acertos > 40 and acertos < 150): return randint(100,999)
    elif (acertos >= 150): return randint(1000,9999)

def num_1_mult_div(acertos):
    if (acertos >= 15 and acertos <= 40): return randint(10,99)
    elif (acertos > 40 and acertos < 150): return randint(100,999)
    elif (acertos >= 150): return randint(1000,9999)

def num_2_mult_div(acertos):
    if (acertos >= 15 and acertos <= 40): return randint(1,9)
    elif (acertos > 40 and acertos < 150): return randint(10,99)
    elif (acertos >= 150): return randint(100,999)

def resposta_errada(lista_pontos, acertos, jogador, lista_jogadores, lista_pontos_geral):
    print("Resposta incorreta.")
    logging.info('Resposta incorreta.')
    lista_pontos.append(acertos)
    print("")
    lista_pontos.sort()
    lista_pontos.reverse()
    print("Pontos ", jogador, ": ", lista_pontos)
    print("")
    logging.debug('paramethers: lista_pontos = {}'.format(lista_jogadores))
    continuar = input("Deseja continuar jogando? [S/N] ")
    while (continuar != "S" and continuar != "s" and continuar != "N" and continuar != "n"):
        print("Insira uma opção válida.")
        continuar = input("Deseja continuar jogando? [S/N] ")
    return continuar

def continua_a(continuar):
  if(continuar == "N" or continuar == "n"):
      logging.info('O jogador optou por nao jogar novamente')
      return False
  else: return True

def continua_acertos(a): 
  if (a):
      logging.info('O jogador optou por jogar novamente')
      return 0

def esvazia_lista(lista):
  i = 0
  while (i <= len(lista) - 1):
    lista.remove(lista[i])

def novo_jogo(a, lista_pontos, lista_pontos_geral):
  if (a == False):
    novo_jogo = input("Deseja iniciar um novo jogo para um novo jogador? [S/N] ")
    logging.debug('paramethers: novo_jogo = {}'.format(novo_jogo))
    while (novo_jogo != "S" and novo_jogo != "s" and novo_jogo != "N" and novo_jogo != "n"):
        print("Insira uma opção válida.")
        novo_jogo = input("Deseja iniciar um novo jogo para um novo jogador? [S/N] ")
        logging.debug('paramethers: novo_jogo = {}'.format(novo_jogo))
    if (novo_jogo == "N" or novo_jogo == "n"):
      logging.info('O jogador optou por finalizar o jogo.')
      lista_pontos_geral.append([])
      for i in lista_pontos:
        lista_pontos_geral[len(lista_pontos_geral) - 1].append(i)
      logging.debug('paramethers: lista_jogadores = {}'.format(lista_jogadores))
      logging.debug('paramethers: lista_pontos_geral = {}'.format(lista_pontos_geral))
      print("")
      print("Histórico de pontos: ")
      for i in range(0,len(lista_jogadores)):
          print(lista_jogadores[i], ": ", lista_pontos_geral[i])
      print("")
      return False
    else:
      logging.info('O jogador optou por iniciar o jogo para um novo jogador.')
      lista_pontos_geral.append([])
      for i in lista_pontos:
        lista_pontos_geral[len(lista_pontos_geral) - 1].append(i)
      esvazia_lista(lista_pontos)
      print("")
      return True

lista_pontos = []
lista_pontos_geral = []
lista_jogadores = []
novo_jogador = True
num_1 = 0
num_2 = 0
while (novo_jogador):
  jogador = input("Nome do jogador: ")
  logging.debug('paramethers: jogador = {}'.format(jogador))
  lista_jogadores.append(jogador)
  logging.debug('paramethers: lista_jogadores = {}'.format(lista_jogadores))
  a = True
  logging.debug('paramethers: a = {}'.format(a))
  acertos = 0
  logging.debug('paramethers: acertos = {}'.format(acertos))
  while (a):
    if(acertos < 15):
        if (acertos == 0):
            if (len(lista_pontos) == 0):
                print("")
                print("O jogo começa no nível FÁCIL")
                logging.info('O jogo começa no nível FÁCIL')
            else:
                print("")
                print("O jogo recomeça do nível FÁCIL ")
                logging.info('O jogo recomeça do nível FÁCIL')
        num_1 = randint(1,9)
        logging.debug('paramethers: num_1 = {}'.format(num_1))
        num_2 = randint(1,9)
        logging.debug('paramethers: num_2 = {}'.format(num_2))
    elif (acertos == 15):
            print("")
            print("Você avançou de nível. Está agora no nível INTERMEDIÁRIO")
            logging.info('O jogador avançou de nível. Está agora no nível INTERMEDIÁRIO')
    elif(acertos == 41):
            print("")
            print("Você avançou de nível. Está agora no nível DIFÍCIL")
            logging.info('O jogador avançou de nível. Está agora no nível DIFÍCIL')
    elif(acertos == 150):
            print("")
            print("Você avançou de nível. Está agora no nível MUITO DIFÍCIL")
            logging.info('O jogador avançou de nível. Está agora no nível MUITO DIFÍCIL')
    operacao = randint(1,4)
    logging.debug('paramethers: operacao = {}'.format(operacao))
    if (operacao == 1):
        if (acertos >= 15):
          num_1 = num_ad_sub(acertos)
          logging.debug('paramethers: num_1 = {}'.format(num_1))
          num_2 = num_ad_sub(acertos)
          logging.debug('paramethers: num_2 = {}'.format(num_2))
        print(num_1, " + ", num_2, " = ")
        resposta = int(input())
        logging.debug('paramethers: resposta = {}'.format(resposta))
        if (resposta == (num_1 + num_2)):
            acertos = acertos + 1
            logging.debug('paramethers: acertos = {}'.format(acertos))
        else:
            continuar = resposta_errada(lista_pontos, acertos, jogador, lista_jogadores, lista_pontos_geral)
            a = continua_a(continuar)
            acertos = continua_acertos(a)
            novo_jogador = novo_jogo(a, lista_pontos, lista_pontos_geral)
    elif (operacao == 2):
        if (acertos >= 15):
          num_1 = num_ad_sub(acertos)
          logging.debug('paramethers: num_1 = {}'.format(num_1))
          num_2 = num_ad_sub(acertos)
          logging.debug('paramethers: num_2 = {}'.format(num_2))
        print(num_1, " - ", num_2, " = ")
        resposta = int(input())
        logging.debug('paramethers: resposta = {}'.format(resposta))
        if (resposta == (num_1 - num_2)):
            acertos = acertos + 1
            logging.debug('paramethers: acertos = {}'.format(acertos))
        else:
            continuar = resposta_errada(lista_pontos, acertos, jogador, lista_jogadores, lista_pontos_geral)
            a = continua_a(continuar)
            acertos = continua_acertos(a)
            novo_jogador = novo_jogo(a, lista_pontos, lista_pontos_geral)
    elif (operacao == 3):
        if (acertos >= 15):
          num_1 = num_1_mult_div(acertos)
          logging.debug('paramethers: num_1 = {}'.format(num_1))
          num_2 = num_2_mult_div(acertos)
          logging.debug('paramethers: num_2 = {}'.format(num_2))
        print(num_1, " * ", num_2, " = ")
        resposta = int(input())
        logging.debug('paramethers: resposta = {}'.format(resposta))
        if (resposta == (num_1 * num_2)):
            acertos = acertos + 1
            logging.debug('paramethers: acertos = {}'.format(acertos))
        else:
            continuar = resposta_errada(lista_pontos, acertos, jogador, lista_jogadores, lista_pontos_geral)
            logging.debug('paramethers: continuar = {}'.format(continuar))
            a = continua_a(continuar)
            logging.debug('paramethers: a = {}'.format(a))
            acertos = continua_acertos(a)
            logging.debug('paramethers: acertos = {}'.format(acertos))
            novo_jogador = novo_jogo(a, lista_pontos, lista_pontos_geral)
    else:
        if(acertos < 15):
            while (num_1 % num_2 != 0):
                num_1 = randint(1,9)
                num_2 = randint(1,9)
        else:
            num_1 = num_1_mult_div(acertos)
            logging.debug('paramethers: num_1 = {}'.format(num_1))
            num_2 = num_2_mult_div(acertos)
            logging.debug('paramethers: num_2 = {}'.format(num_2))
            while(num_1 % num_2 != 0):
              num_1 = num_1_mult_div(acertos)
              logging.debug('paramethers: num_1 = {}'.format(num_1))
              num_2 = num_2_mult_div(acertos)
              logging.debug('paramethers: num_2 = {}'.format(num_2))
        print(num_1, " / ", num_2, " = ")
        resposta = int(input())
        logging.debug('paramethers: resposta = {}'.format(resposta))
        if (resposta == (num_1 / num_2)):
            acertos = acertos + 1
            logging.debug('paramethers: acertos = {}'.format(acertos))
        else:
            continuar = resposta_errada(lista_pontos, acertos, jogador, lista_jogadores, lista_pontos_geral)
            a = continua_a(continuar)
            acertos = continua_acertos(a)
            novo_jogador = novo_jogo(a, lista_pontos, lista_pontos_geral)
print("Fim de Jogo")
