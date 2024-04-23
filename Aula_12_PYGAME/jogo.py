import pygame
from pygame.locals import *
from sys import *

pygame.init()

altura = 480
largura = 640

# Criando a janela:
tela = pygame.display.set_mode((largura, altura))

# Título da janela:
pygame.display.set_caption("Criando Jogos")

while True:
    
    # Colocando os eventos no Pygame:
    for event in pygame.event.get():
        
        # Evento de saída
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    # Atualizar o jogo a cada 
    pygame.display.update()