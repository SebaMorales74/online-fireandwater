import pygame

class World:
        def __init__(self, data=[], color=(107, 95, 55)):
            self.tile_list = []
            self.color = color
            self.tileSize = 32

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        self.tile = pygame.Rect(0, 0, self.tileSize, self.tileSize)
                        self.tile.x = col_count * self.tileSize
                        self.tile.y = row_count * self.tileSize
                        self.tile_list.append(self.tile)
                    col_count += 1
                row_count += 1

        def draw(self,ventana):
            ventana.fill(self.color)
            for tile in self.tile_list:
                pygame.draw.rect(ventana, (173, 112, 71), tile)