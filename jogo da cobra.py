import pygame
from random import randint

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (46, 139, 87)
azul = (0, 0, 255)


############Inicialização############################
try:
    pygame.init()
except:
    print('O modulo pygame não foi iniciado com sucesso!')
    #########################################################
###########   Variaveis da tela  ##################
largura = 320
altura = 240

tamanho = 10

 ###########################   FPS  ###########################

relogio = pygame.time.Clock() # inicializado assim define a velocidade de pixel por segundo
################### Desenhando os Personagem e cenario #############
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo Da Cobrinha')
font = pygame.font.SysFont(None,20)

def texto(msg,cor):
    texto1 = font.render(msg,True,cor)
    fundo.blit(texto1, [largura/10,altura/2])
def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, verde, [XY[0],XY[1] , tamanho, tamanho])


def maca(pos_x,pos_y):
    pygame.draw.rect(fundo, branco, [pos_x, pos_y, tamanho, tamanho])

############# Funções #################
def jogo():
    sair = True # variavel de flag
    fimdejogo = False
    ####################Player######################
    pos_x = randint(0, (largura - tamanho) / 10) * 10
    pos_y = randint(0, (altura - tamanho) / 10) * 10
    maca_x = randint(0, (largura - tamanho) / 10) * 10
    maca_y = randint(0, (altura - tamanho) / 10) * 10
    velocidade_x = 0
    velocidade_y = 0
    #################################################
    contador = 0
    speedsnaker = 10

    #################Comprimento da cobra############################
    CobraXY = []
    CombraComp = 1
    ###################### Evento de criação de tela ############
    while sair:
        while fimdejogo:
            fundo.fill(verde)
            texto("Você perdeu :Click se deseja para continuar:",branco)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                        jogo()
       ################  Evento para sair do jogo #######################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

            #######################################################################
            ### Movimento
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = - tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = + tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = - tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = + tamanho

        fundo.fill(preto)
        ####################################################################
        ############# Inicializador ###########
        pos_x += velocidade_x
        pos_y += velocidade_y
        #########################

        CobraInicio = []
        CobraInicio.append(pos_x) #aqui é colocado na lista o valor da posx da cobra
        CobraInicio.append(pos_y) # e o valor Y
        CobraXY.append(CobraInicio) # atribui a lista a posX e PosY da cobra assim definido a cabeca
        if len(CobraXY)> CombraComp: # se o tamanho da cobraXY for maior que a Comprimento da cobra
            del CobraXY[0] #Vamos excluir o 1* elemento da cobra, pq o ultimo elemento da lista e a cabeça



        ##############Colisão da cobra ###############################
        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]): # verificamos se a da lista toca no restante do bloco
##Se algum bloco for igual a incio da cobra, depois vamos verificar se o bloco toca alguma vez na cabeça que é o incio da cobra
          fimdejogo = True; # caso for verdadeiro se encerra o jogo

        cobra(CobraXY) #chamada da função cobra

        ############Pegar a maçam#################
        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randint(0, (largura - tamanho) / 10) * 10
            maca_y = randint(0, (altura - tamanho) / 10) * 10
            CombraComp +=3 #faz que a cobra aumente seu tamanho
            contador +=1
            print(contador)
            if contador == 3:
                speedsnaker +=3
                contador = 0



        maca(maca_x,maca_y)
        pygame.display.update()

       #######FPS#########################
        relogio.tick(speedsnaker) ### Definição do Fps


        ## colisão de atravessar a parede##
        if pos_x == largura:
            pos_x = 0  # D > PRA >
        if pos_x < 0:  # E < PRA <
            pos_x = largura - tamanho
        if pos_y > altura:  # baixo
            pos_y = 0
        if pos_y < 0:
            pos_y = altura - tamanho  # î î

        ### Tocou morreu ####
       # if pos_x >= largura:
        #    fimdejogo = True
        #if pos_x < 0:
         #  fimdejogo = True
        #if pos_y > altura:
         #   fimdejogo = True
        #if pos_y <0:
         #   fimdejogo = True
    #######################################################

jogo()
pygame.quit()#termina o programa