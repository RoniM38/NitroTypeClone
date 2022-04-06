import pygame

CORRECT_CHAR = pygame.Color("dodgerblue2")
WRONG_CHAR = "#ff4749"

class TextBox:
    def __init__(self, surface, border_color, bg_color, x, y, width, height,
                 sentence, font_size, font_color):
        self.surface = surface
        self.border_color = border_color
        self.bg_color = bg_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sentence = sentence
        self.font_size = font_size
        self.font_color = font_color

        self.font = pygame.font.SysFont("Franklin Gothic Demi", self.font_size)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.highlight_color = CORRECT_CHAR
        self.char_index = 0

    def draw(self):
        pygame.draw.rect(self.surface, self.bg_color, self.rect)
        pygame.draw.rect(self.surface, self.border_color, self.rect, 3)

        sentence_list = self.sentence.split()

        x = self.x + self.font_size
        y = self.y + self.font_size
        for i, word in enumerate(sentence_list):
            word_index = range(self.sentence.index(word), self.sentence.index(word)+len(word))
            word_label = self.font.render(word, True, self.font_color)

            if x + word_label.get_width() >= self.x + self.width:
                y += self.font_size
                x = self.x + self.font_size

            for i_c, c in enumerate(word):
                if self.char_index in word_index and i + i_c == self.char_index:
                    c_label = self.font.render(c, True, self.highlight_color)
                else:
                    c_label = self.font.render(c, True, self.font_color)

                self.surface.blit(c_label, (x, y))

                x += c_label.get_width()
            if self.sentence[self.char_index] == " " and i + len(word) == self.char_index:
                pygame.draw.rect(self.surface, self.highlight_color, (x, y+10, 5, 10))
            x += 5

    def letter_typed(self, key):
        # if a key that doesn't appear in the ascii table is pressed, a ValueError is raised
        # this exception handling is meant to prevent the ValueError from stopping the game
        try:
            letter = chr(key)

            if (letter.isalpha() or letter == " ") and letter == self.sentence[self.char_index]:
                if self.char_index < len(self.sentence):
                    self.highlight_color = CORRECT_CHAR
                    self.char_index += 1
            else:
                self.highlight_color = WRONG_CHAR
        except ValueError:
            pass
