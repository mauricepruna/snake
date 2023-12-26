import time

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(None, 25)
        self.screen = pygame.display.set_mode((800, 400))

    def draw(self):
        self.screen.fill("Blue")
        for x in range(20):
            for y in range(15):
                pygame.draw.rect(
                    self.screen, "Black", (x * 21 + 25, y * 21 + 25, 20, 20)
                )
                self.draw_text("SCORE: ", "Green", 500, 25)

    def draw_text(self, text, color, x, y):
        text_image = self.font.render(text, True, color)
        self.screen.blit(text_image, ((x, y)))


if __name__ == "__main__":
    game = Game()
    while True:
        game.draw()
        time.sleep(1 / 10)
