import pygame
import random

#definir la notion du monstre
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1000, 1300)
        self.rect.y = 540
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si son nouveau nombre de point de vie est inferieur ou egale à 0
        if self.health <= 0:
            #Recreer un monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health

    def update_health_bar(self, surface):

        # dessiner l'arriere de la barre de vie (surface, couleur, position)
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        #dessiner la barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        #le deplacement ne se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            #si le monstre est en collision avec le monstre
        else:
            #infliger des degats aux joueurs
            self.game.player.damage(self.attack)