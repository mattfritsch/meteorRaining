import pygame
import math
from game import Game
pygame.init() #initialise ce qu'il y a dans le package

#generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

#image de la fenetre
background = pygame.image.load('assets/bg.jpg')

#importer charger la bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
#adapter la bannière a la taille de la fenetre
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#importer un bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400,150))
#adapter bouton a la taille de la fenetre
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#charger le jeu
game = Game()


running = True

#boucle tant que cette condition est vrai (fenetre ouverte)
while running:

    #appliquer l'arrière plan du jeu
    screen.blit(background, (0, -200))

    #verifier si le jeu à commencé ou non
    if game.is_playing:
        #declencher les instructions de la partie
        game.update(screen)
    #verifier si notre jeu n'a pas commencé
    else:
        #ajouter mon ecran de bienvenu
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #mettre a jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        #verifier eveneent est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclenché
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancer
                game.start()