import  pygame
from projectile import Projectile

#creer une premiere classe qui va representer le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.velocity = 3
        self.image = pygame.image.load('assets/player.png')
        #rectangle qui se deplace et qui sert de hitbox
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500
        self.all_projectile = pygame.sprite.Group()

    def damage(self, amount):
        if self.health - amount > amount:
             self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        # dessiner l'arriere de la barre de vie (surface, couleur, position)
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        #dessiner la barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def launch_projectile(self):
        #creer une instance de la classe
        self.all_projectile.add(Projectile(self))

    def move_right(self):
        #si le joueur n'est pas en collision avec une entité monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity