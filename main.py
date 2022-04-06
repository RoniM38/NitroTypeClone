import pygame
import sys
import random
pygame.init()

from background import BackGround
from textbox import TextBox
from button import Button

WINDOW_SIZE = (1100, 550)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Nitro Type Clone")

MENU_BG = "#e8e7ef"
SKY_BLUE = "#afecf4"
WHITE = (255, 255, 255)
TEXTBOX_BG = "#a2a2a2"
RED = "#f82a36"
GREEN = "#00bb77"

# Road Image
road = pygame.image.load("road.png")
original_size = road.get_size()
scale = WINDOW_SIZE[0]//original_size[0]
road = pygame.transform.scale(road, (WINDOW_SIZE[0], original_size[1] * scale))

# Car Image
car_img = pygame.image.load("car.png")

# game logo
logo = pygame.image.load("NitroTypeLogo.png")

countdown_font = pygame.font.SysFont("Franklin Gothic Heavy", 150)


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


def quit_game():
    pygame.quit()
    sys.exit(0)


def main():
    car = Car(window, car_img, 390, 330)

    clock = pygame.time.Clock()

    scrollSpeed = 0
    background = BackGround(window, 0, WINDOW_SIZE[1]-road.get_height()+5, scrollSpeed, road)

    with open("words.txt", "r") as f:
        content = f.readlines()

    num_words = random.randint(10, 50)
    sentence = " ".join(random.sample(content, num_words)).replace("\n", "")

    sentence_box = TextBox(window, WHITE, TEXTBOX_BG, 300, 0, 500, 250, sentence, 20, WHITE)

    # time waited between each number in the countdown
    wait_time = 1000
    start = pygame.time.get_ticks()
    countdown_list = ["3", "2", "1", "GO"]
    countdown_index = 0
    countdown = True

    countdown_sound = pygame.mixer.Sound("Mario Kart Race Countdown - Sound Effect.mp3")
    countdown_sound.play()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    countdown_sound.stop()
                    menu()
                else:
                    if not countdown:
                        sentence_box.letter_typed(event.key)

        window.fill(SKY_BLUE)
        background.scroll()
        background.draw()

        clock.tick(60)

        car.draw()
        sentence_box.draw()

        if countdown:
            if countdown_index == len(countdown_list) - 1:
                x = WINDOW_SIZE[0] // 2 - 100
            else:
                x = WINDOW_SIZE[0] // 2 - 50

            if countdown_index < len(countdown_list):
                window.blit(countdown_font.render(countdown_list[countdown_index], True, GREEN),
                            (x, WINDOW_SIZE[1] // 2 - 50))
            else:
                countdown = False

            now = pygame.time.get_ticks()
            if now - start >= wait_time:
                countdown_index += 1
                start = pygame.time.get_ticks()

        pygame.display.update()

    quit_game()


def menu():
    play_button = Button(window, "Play!", RED, WHITE, 420, 430, 200, 80)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    main()

        window.fill(MENU_BG)
        window.blit(logo, (330, 20))
        play_button.draw()

        pygame.display.update()

    quit_game()


if __name__ == "__main__":
    menu()
