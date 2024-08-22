import os
import pygame
import time

pygame.init()

pasta = r'F:\codigos gustavo\PY\Projeto_1\musicas'
arquivos = [nome for nome in os.listdir(pasta) if nome.lower().endswith('.mp3')]

class btn:
    def __init__(self):
        self.msc_pausada = False
        self.msc_atual = -1

    def play(self, msc):
        if msc >= 0 and msc < len(arquivos) +1:
            pygame.mixer.music.load(fr'F:\codigos gustavo\PY\Projeto_1\musicas\{arquivos[msc]}')
            print(f"Iniciando {arquivos[msc]}",end="")
            for c in range(3):
                print(".",end="")
                time.sleep(0.5)
            print()
            pygame.mixer.music.play()
            self.msc_atual = msc
        else:
            print("Música não encontrada!")
            time.sleep(2)
            os.system('cls')

    def pause_despause(self):
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    
    def parar(self):
        pygame.mixer.music.stop()
        self.msc_atual = -1

    def pular(self):
        if self.msc_atual == -1:
            print("Você não está tocando nenhuma música!")
            time.sleep(2)
            os.system('cls')
            return
        
        if self.msc_atual >= 0 and self.msc_atual < len(arquivos) - 1:
            self.play(self.msc_atual + 1)
        else:
            print("Não há próxima música.")
            time.sleep(2)
            os.system('cls')

    def voltar(self):
        if self.msc_atual == -1:
            print("Você não está tocando nenhuma música!")
            time.sleep(2)
            os.system('cls')
            return
        
        if self.msc_atual > 0:
            self.play(self.msc_atual - 1)
        else:
            print("Não há música anterior.")
            time.sleep(2)
            os.system('cls')
    
    def inicio(self):
        pygame.mixer.music.load(fr'F:\codigos gustavo\PY\Projeto_1\musicas\{arquivos[self.msc_atual]}')
        pygame.mixer.music.play()

def listar_musicas():
    os.system('cls')
    print("Suas músicas:")
    for musica in arquivos:
        print(f"{arquivos.index(musica)}: {musica}")

def delay(l1):
    if l1 == "1":
        print("Voltando Música",end="")
        for c in range(3):
            print(".",end="")
            time.sleep(0.2)
        print("")
    elif l1 == "2":
        print("Pausando Música",end="")
        for c in range(3):
            print(".",end="")
            time.sleep(0.2)
        print("")
    elif l1 == "3":
        print("Pulando Música",end="")
        for c in range(3):
            print(".",end="")
            time.sleep(0.2)
        print("")
    elif l1 == "4":
        print("Parando Música",end="")
        for c in range(3):
            print(".",end="")
            time.sleep(0.2)
        print("")