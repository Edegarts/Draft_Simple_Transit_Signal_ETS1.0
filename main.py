import pygame
pygame.init()
color_red_circle = 10
color_green_circle = 100
color_blue_circle = 10

posit_x_initial = 270  #range (250 - 290)
posit_y_initial = 450  # range (100-450)


color_line_base = (150,10,0)
background = pygame.image.load('Background002.png')
srbol_happy = pygame.image.load('Mr_bolacha_001.png')
srbol_saddly = pygame.image.load('Mr_bolacha_S001.png')
red_car = pygame.image.load('red_car.png')
blue_car = pygame.image.load('blue_car.png')
red_signal = pygame.image.load('red_signal.png')
yellow_signal = pygame.image.load('yellow_signal.png')
green_signal = pygame.image.load('green_signal.png')
velocidade = 7
velocidade_bots_red = 12
velocidade_bots_blue = 4
pos_red_x = 80
pos_red_y = 100
pos_blue_x = 80
pos_blue_y = 130
color_sign = 1
count_time= 1
color_signal = 'green'

janela = pygame.display.set_mode ((800,600)) # aka surface to draw method
pygame.display.set_caption("Testando gráficos Python")
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        posit_y_initial -= velocidade
    if comandos[pygame.K_DOWN]:
        posit_y_initial += velocidade
    if comandos[pygame.K_RIGHT]:
        if (posit_x_initial < 320):
            posit_x_initial += velocidade
    if comandos[pygame.K_LEFT]:
        if (posit_x_initial > 200):
            posit_x_initial = posit_x_initial - velocidade
    if (pos_red_x >300) and (pos_red_x < 370) and (color_signal == 'red'):
        velocidade_bots_red = 0
    pos_red_x+= velocidade_bots_red
    if (pos_blue_x > 300) and (pos_blue_x < 370) and (color_signal == 'red'):
        velocidade_bots_blue = 0
    pos_blue_x += velocidade_bots_blue
    if (pos_red_x >= 850):
        pos_red_x = -20
    if (pos_blue_x >= 820):
        pos_blue_x = -20

    janela.blit(background,(0,0))

    if (color_sign == 1):
        velocidade_bots_red = 10
        velocidade_bots_blue = 5
        janela.blit(green_signal, (410, 0))
        count_time = count_time + 1
        color_signal = 'green'
        if (count_time > 90):
            color_sign = color_sign + 1
            count_time = count_time + 1

    if (color_sign == 2):
        janela.blit(yellow_signal, (410, 0))
        count_time = count_time + 1
        color_signal = 'yellow'
        if (count_time > 120):
            color_sign = color_sign + 1
            count_time = count_time + 1
    if (color_sign == 3):
        janela.blit(red_signal, (410, 0))
        count_time = count_time + 1
        color_signal = 'red'
        if (count_time > 190):
            color_sign = color_sign + 1
            count_time = 1
            color_sign = 1

    janela.blit(red_car, (pos_red_x, pos_red_y))
    janela.blit(blue_car, (pos_blue_x, pos_blue_y))
    janela.blit(srbol_happy, (posit_x_initial, posit_y_initial))
   #pygame.draw.circle(janela, (color_red_circle,color_green_circle,color_blue_circle), (posit_x_circle, posit_y_circle), radius_circle)
   #pygame.draw.line(janela, color_line_base, (50, 250), (50, 50), 5)
    pygame.display.update()

pygame.quit()
