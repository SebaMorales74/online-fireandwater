from pygame import K_d, K_a, K_w, Rect
import pygame


class Player:
    def __init__(self,
                 velocidad=5,
                 color=(255, 255, 255),
                 derecha=K_d,
                 izquierda=K_a,
                 arriba=K_w,
                 character="firedude"):
        self.hitbox = Rect(0, 0, 32, 58)
        self.hitbox.center = (400, 300)
        self.velocidad = velocidad
        self.color = color
        self.gravedad = 0.5
        self.accVertical = 0
        self.derecha = derecha
        self.izquierda = izquierda
        self.arriba = arriba
        self.orientation = "right"
        self.character = character

    def move(self, world):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[self.derecha]:
            dx += self.velocidad
            self.orientation = "right"
        if keys[self.izquierda]:
            dx -= self.velocidad
            self.orientation = "left"
        if keys[self.arriba] and self.hitbox.bottom >= 600:
            self.accVertical = -10

        if self.hitbox.bottom < 600:
            self.accVertical += self.gravedad
        else:
            self.accVertical -= self.gravedad

        if self.accVertical > 10:
            self.accVertical = 10
        dy += self.accVertical

        for tile in world.tile_list:
            if tile.colliderect(self.hitbox.x, self.hitbox.y + dy, self.hitbox.width, self.hitbox.height):
                dy = 0
                self.accVertical = 0
                if keys[self.arriba]:
                    self.accVertical = -10
            if tile.colliderect(self.hitbox.x + dx, self.hitbox.y, self.hitbox.width, self.hitbox.height-1):
                dx = 0

        self.hitbox.x += dx
        self.hitbox.y += dy

    def draw(self, ventana):
        # # self.image = pygame.image.load("./assets/sprites/firedude.png")
        # # self.image = pygame.transform.scale(self.image, (58, 32))
        # # self.image.set_colorkey((255, 255, 255))

        # if self.orientation == "right":
        #     pygame.draw.rect(ventana, self.color, self.hitbox)
        #     # ventana.blit(self.image, self.hitbox)
        # elif self.orientation == "left":
        #     pygame.draw.rect(ventana, self.color, self.hitbox)
        #     # ventana.blit(pygame.transform.flip(
        #     #     self.image, True, False), self.hitbox)
        pass
