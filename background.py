class BackGround:
    def __init__(self, surface, x, y, scrollSpeed, img):
        self.surface = surface
        self.x = x
        self.y = y
        self.scrollSpeed = scrollSpeed
        self.img = img

        self.x2 = self.x + self.img.get_width()
        self.y2 = self.y

        self.startX = self.x

    def draw(self):
        self.surface.blit(self.img, (self.x, self.y))
        self.surface.blit(self.img, (self.x2, self.y2))

    def scroll(self):
        if self.x <= 0 and self.x2 <= 0:
            self.x = self.startX
            self.x2 = self.x + self.img.get_width()
        else:
            self.x -= self.scrollSpeed
            self.x2 -= self.scrollSpeed
