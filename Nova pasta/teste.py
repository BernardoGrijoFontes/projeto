import pygame
from pygame.locals import *
from sys import exit
import os
from random import randint
from tkinter import font

pygame.init()

pygame.font.init()

fonte = pygame.font.SysFont('arial', 25, False, False)

largura = 1200
altura = 640
coracao = pygame.image.load(os.path.join('assets', 'coracao.png'))
x = largura/2
y = 480
preto = 0, 0, 0

morte = pygame.image.load(os.path.join('assets', 'morte.png'))
morte = pygame.transform.scale(morte, (370, 210))
morte_rect = morte.get_rect()
morte_rect.center = (600, 150)

gambiarra = 0

flecha = pygame.image.load(os.path.join('assets', 'flecha.png'))
flecha = pygame.transform.scale(flecha, (99, 18))
x_flecha = 900
y_flecha = randint(325, 532)

flecha2 = pygame.image.load(os.path.join('assets', 'flecha.png'))
flecha2 = pygame.transform.scale(flecha2, (99, 18))
flecha2 = pygame.transform.rotate(flecha2, 180)
x_flecha2 = 220
y_flecha2 = randint(325, 532)

flecha3 = pygame.image.load(os.path.join('assets', 'flecha.png'))
flecha3 = pygame.transform.scale(flecha3, (99, 18))
flecha3 = pygame.transform.rotate(flecha3, 90)
x_flecha3 = randint(400, 815)
y_flecha3 = 125

flecha4 = pygame.image.load(os.path.join('assets', 'flecha.png'))
flecha4 = pygame.transform.scale(flecha4, (99, 18))
flecha4 = pygame.transform.rotate(flecha4, 270)
x_flecha4 = randint(400, 815)
y_flecha4 = 620

vida = 5

dificuldade = 1

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    mensagem = f'Vidas: {vida}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
    texto_rect = texto_formatado.get_rect()
    texto_rect.center = (600, 619)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    if vida > 0:
        if pygame.key.get_pressed()[K_a]:
            if x > 400:
                x = x - 5
        if pygame.key.get_pressed()[K_d]:
            if x < 808:
                x = x + 5
        if pygame.key.get_pressed()[K_w]:
            if y > 325:
                y = y - 5
        if pygame.key.get_pressed()[K_s]:
            if y < 570:
                y = y + 5

        tela.fill(preto)

        pygame.draw.rect(tela, (255, 255, 255), (395, 320, 5, 273))
        pygame.draw.rect(tela, (255, 255, 255), (833, 320, 5, 273))
        pygame.draw.rect(tela, (255, 255, 255), (400, 320, 433, 5))
        pygame.draw.rect(tela, (255, 255, 255), (395, 593, 443, 5))


        tela.blit(flecha, (x_flecha, y_flecha))
        tela.blit(flecha2, (x_flecha2, y_flecha2))
        tela.blit(flecha3, (x_flecha3, y_flecha3))
        tela.blit(flecha4, (x_flecha4, y_flecha4))

        pygame.draw.rect(tela, (0, 0, 0), (195, 320, 200, 278))
        pygame.draw.rect(tela, (0, 0, 0), (840, 320, 200, 278))
        pygame.draw.rect(tela, (0, 0, 0), (395, 120, 443, 200))
        pygame.draw.rect(tela, (0, 0, 0), (395, 598, 443, 200))

        tela.blit(coracao, (x, y))

        tela.blit(texto_formatado, (texto_rect))

        coracao_rect = pygame.Rect(x, y, 25, 23)
        flecha_rect = pygame.Rect(x_flecha, y_flecha, 99, 18)
        flecha2_rect = pygame.Rect(x_flecha2, y_flecha2, 99, 18)
        flecha3_rect = pygame.Rect(x_flecha3, y_flecha3, 18, 99)
        flecha4_rect = pygame.Rect(x_flecha4, y_flecha4, 18, 99)

        if flecha_rect.colliderect(coracao_rect):
            x_flecha = 900
            y_flecha = randint(325, 532)
            vida -= 1
            gambiarra = 1

        if flecha2_rect.colliderect(coracao_rect):
            x_flecha2 = 220
            y_flecha2 = randint(325, 532)
            vida -= 1
            gambiarra = 2

        if flecha3_rect.colliderect(coracao_rect):
            x_flecha3 = randint(400, 815)
            y_flecha3 = 200
            vida -= 1
            gambiarra = 3

        if flecha4_rect.colliderect(coracao_rect):
            x_flecha4 = randint(400, 815)
            y_flecha4 = 620
            vida -= 1
            gambiarra = 0
            if dificuldade <= 2:
                dificuldade += 0.25

        if gambiarra == 0:
            x_flecha -= 8 * dificuldade
        
        if x_flecha < 200:
            x_flecha = 900
            y_flecha = randint(325, 532)
            gambiarra = 1
            
        if gambiarra == 1:
            x_flecha2 += 8 * dificuldade

        if x_flecha2 > 900:
            x_flecha2 = 220
            y_flecha2 = randint(325, 532)
            gambiarra = 2

        if gambiarra == 2:
            y_flecha3 += 8 * dificuldade

        if y_flecha3 > 650:
            x_flecha3 = randint(400, 815)
            y_flecha3 = 125
            gambiarra = 3

        if gambiarra == 3:
            y_flecha4 -= 8 * dificuldade

        if y_flecha4 < 150:
            x_flecha4 = randint(400, 815)
            y_flecha4 = 620
            gambiarra = 0 
            if dificuldade <= 2:
                dificuldade += 0.25

    if vida == 0:
        mensagem2 = f'Aperte ESPAÇO para tentar novamente'
        texto_formatado2 = fonte.render(mensagem2, False, (255, 255, 255))
        texto_rect2 = texto_formatado2.get_rect()
        texto_rect2.center = (600, 619)
        coracao_quebrado = pygame.image.load(os.path.join('assets', 'coracao_quebrado.png'))
        pygame.draw.rect(tela, (0, 0, 0), (395, 320, 600, 600))
        tela.blit(coracao_quebrado, (x, y))
        tela.blit(morte, (morte_rect))
        tela.blit(texto_formatado2, (texto_rect2))

        if pygame.key.get_pressed()[K_SPACE]:
            vida = 5
            gambiarra = 0
            x = largura/2
            y = 480
            dificuldade = 1

    pygame.display.flip()

    pygame.display.update()