import pygame
from pygame.locals import *
from sys import *
from random import *

pygame.init()

# Definindo posição e tamanho do Objeto:
altura = 480
largura = 640
pos_y_retangulo = altura / 2
pos_x_retangulo = largura / 2
largura_retangulo = 30
altura_retangulo = 30

# Definindo posição e tamanho do circulo:
pos_y_circulo = 40
pos_x_circulo = 40
raio_circulo = 10

# Definindo Fonte
fonte = pygame.font.SysFont("arial", 20 , True, False)

# Criando a janela:
tela = pygame.display.set_mode((largura, altura))

# Título da janela:
pygame.display.set_caption("Criando Jogos")

# Contador de Pontos:
pontos = 0

# Modificar a taxa de atualização de Pixels/segundo
relogio = pygame.time.Clock()

while True:
    
    # Ajustando a velocidade
    relogio.tick(20)
    
    # Para pintar a tela de preto a cada atualização
    tela.fill((0,0,0))
    
    # Contador de Pontos
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    
    # Colocando os eventos no Pygame:
    for event in pygame.event.get():
        
        # Evento de saída
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        # Evento de Movimento
        
        #if event.type == KEYDOWN:
        #    if event.key == K_UP:        
        #        pos_y_retangulo = pos_y_retangulo - 10
        #    if event.key == K_DOWN: 
        #        pos_y_retangulo = pos_y_retangulo + 10      
        #    if event.key == K_LEFT:        
        #        pos_x_retangulo = pos_x_retangulo - 10      
        #    if event.key == K_RIGHT:        
        #        pos_x_retangulo = pos_x_retangulo + 10 
        
    if pygame.key.get_pressed()[K_w]:     
        pos_y_retangulo = pos_y_retangulo - 10
    elif pygame.key.get_pressed()[K_s]:
        pos_y_retangulo = pos_y_retangulo + 10     
    elif pygame.key.get_pressed()[K_a]:  
        pos_x_retangulo = pos_x_retangulo - 10   
    elif pygame.key.get_pressed()[K_d]:  
        pos_x_retangulo = pos_x_retangulo + 10   
            
    # Definindo retangulo        
    retangulo = pygame.draw.rect(tela, (0, 0, 255), (pos_x_retangulo, pos_y_retangulo, largura_retangulo, altura_retangulo))
    
    #definindo circulo
    circulo = pygame.draw.circle(tela, (255, 0, 255), (pos_x_circulo, pos_y_circulo), raio_circulo)
    
    if retangulo.colliderect(circulo):
        pos_x_circulo = randint (40, 600) # Espaço de 40 para os limites da tela
        pos_y_circulo = randint (50, 430) # Espaço de 50 para os limites da tela
        pontos = pontos + 1
        
    tela.blit(texto_formatado, (400,40))
            
    # Atualizar o jogo a cada interação
    pygame.display.update()