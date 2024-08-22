from funções import *
import os
import time
os.system('cls')

nome = input("Qual o seu nome? ")
if nome == "":
    nome = "usuário"
    print(f"Olá {nome}, Seja bem vindo ao DexPlayer!")
    time.sleep(1)
else:
    print(f"Olá {nome}, Seja bem vindo ao DexPlayer!")
    time.sleep(2)
os.system('cls')

Btn = btn()

pasta = r'F:\codigos gustavo\PY\Projeto_1\musicas'
arquivos = os.listdir(pasta)

while True:
    os.system('cls')
    acao = input(
                    "Escutar uma Música(1): \n"
                    "Listar Músicas(2): \n"
                    "Encerrar player(3): \n"
                    "Escolha uma opção (1, 2 ou 3): "
                    )
    if acao == "1":
        os.system('cls')
        listar_musicas()
        msc = input("Escolha uma música que deseja escutar (insira um número): ")
        if msc == "":
            print("A entrada não pode estar vazia. Tente novamente.")
            time.sleep(0.5)
        else:
            msc = int(msc)
            if msc >= 0 and msc < len(arquivos):
                Btn.play(msc)
                while True:
                    os.system('cls')
                    acao2 = input(
                                    "Menu Música\n"
                                    "Voltar para a Música anterior(1):\n"
                                    "Pausar Música(2):\n"
                                    "Pular Música(3):\n"
                                    "Início da Música(4):\n"
                                    "Parar Música(5):\n"
                                    "Escolha uma opção (1, 2, 3, 4 ou 5): ")
                    if acao2 == "1":
                        os.system('cls')
                        delay(acao2)
                        Btn.voltar()
                    elif acao2 == "2":
                        os.system('cls')
                        delay(acao2)
                        Btn.pause_despause()
                    elif acao2 == "3":
                        os.system('cls')
                        delay(acao2)
                        Btn.pular()
                    elif acao2 == "4":
                        os.system('cls')
                        delay(acao2)
                        Btn.inicio()
                    elif acao2 == "5":
                        os.system('cls')
                        delay(acao2)
                        Btn.parar()
                        break
                    else:
                        print("Valor inválido digitado!")
            else:
                print("Música inexistente!")
                os.system('cls')
    elif acao == "2":
        os.system('cls')
        listar_musicas()
        input(f"Pressione 'enter' para continuar.")
    elif acao == "3":
        os.system('cls')
        print(f"Muito obrigado por usar o DexPlayer!, {nome}.")
        break
    