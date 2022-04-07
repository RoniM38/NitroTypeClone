import pygame
from button import Button

GOLD = "#bec400"
RED = "#f82a36"
WHITE = (255, 255, 255)
results_font = pygame.font.SysFont("Berlin Sans FB Demi", 80, "bold")
stats_font = pygame.font.SysFont("Arial", 30, "bold")


class Results:
    def __init__(self, surface, sentence_box, sentence, num_words, car_img):
        self.surface = surface
        self.sentence_box = sentence_box
        self.sentence = sentence
        self.num_words = num_words
        self.car_img = pygame.transform.scale(car_img, (144, 68))

        self.correct_chars = sentence_box.correct_chars
        self.typing_time = sentence_box.typing_time

        self.surface_size = surface.get_size()

        self.menu_button = Button(surface, "menu", RED, WHITE, 10, 130, 200, 80)

    def draw(self):
        self.correct_chars = self.sentence_box.correct_chars
        self.typing_time = self.sentence_box.typing_time

        self.menu_button.draw()

        self.surface.blit(results_font.render("RESULTS", True, WHITE), (self.surface_size[0]//2.9, 130))

        pygame.draw.rect(self.surface, GOLD, (0, 250, self.surface_size[0], 100))
        self.surface.blit(self.car_img, (10, 270))
        self.surface.blit(results_font.render("You", True, WHITE), (185, 250))

        wpm = self.get_wpm()
        self.surface.blit(stats_font.render(f"{wpm:.2f} WPM", True, WHITE), (400, 285))

        acc = self.get_accuracy()
        self.surface.blit(stats_font.render(f"{acc:.2f}% Acc", True, WHITE), (650, 285))

        self.surface.blit(stats_font.render(f"{self.typing_time:.2f} secs", True, WHITE), (900, 285))

    def get_wpm(self):
        return self.num_words / (self.typing_time / 60)

    def get_accuracy(self):
        return self.correct_chars / len(self.sentence) * 100
