import pygame
import sys
import random
pygame.init()

from background import BackGround
from textbox import TextBox

WINDOW_SIZE = (1100, 550)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Nitro Type Clone")

SKY_BLUE = "#afecf4"
WHITE = (255, 255, 255)
TEXTBOX_BG = "#a2a2a2"

# Road Image
road = pygame.image.load("road.png")
original_size = road.get_size()
scale = WINDOW_SIZE[0]//original_size[0]
road = pygame.transform.scale(road, (WINDOW_SIZE[0], original_size[1] * scale))

# Car Image
car_img = pygame.image.load("car.png")


class Car:
    def __init__(self, surface, img, x, y):
        self.surface = surface
        self.img = img
        self.x = x
        self.y = y

        self.hitbox = self.get_hitbox()

    def draw(self):
        self.surface.blit(self.img, (self.x, self.y))

        # Code for testing the hitbox
        # pygame.draw.rect(self.surface, (255, 0, 0), self.hitbox, 3)

    def get_hitbox(self):
        w, h = self.img.get_size()
        return pygame.Rect(self.x, self.y, w, h)


def main():
    car = Car(window, car_img, 390, 330)

    scrollSpeed = 0
    background = BackGround(window, 0, WINDOW_SIZE[1]-road.get_height()+5, scrollSpeed, road)

    with open("words.txt", "r") as f:
        content = f.readlines()

    num_words = random.randint(10, 50)
    sentence = " ".join(random.sample(content, num_words)).replace("\n", "")

    sentence_box = TextBox(window, WHITE, TEXTBOX_BG, 300, 0, 500, 250, sentence, 20, WHITE)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                sentence_box.letter_typed(event.key)

        window.fill(SKY_BLUE)
        background.scroll()
        background.draw()

        car.draw()
        sentence_box.draw()

        pygame.display.update()

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
