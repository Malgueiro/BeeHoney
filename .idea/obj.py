import pygame


class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1
        self.tick = 0

    def draw(self, window):
        self.group.draw(window)

    def anim(self, image, tick, frames):
        self.tick += 1

        if self.tick == tick:
            self.tick = 0
            self.frame += 1

        if self.frame == frames:
            self.frame = 1

        self.sprite.image = pygame.image.load(f'assets/{image}{str(self.frame)}.png')


class Bee(Obj): # -> colocar parenteses serve para herdar ações de outras classes

    def __init__(self, image, x, y):
        super().__init__(image, x, y)  # -> indica todas as heranças que foram herdadas da classe pai

        pygame.mixer.init()
        self.soundPts = pygame.mixer.Sound('sounds/score.ogg') # -> sound vai servir para sons curtos
        self.soundBlock = pygame.mixer.Sound('sounds/bateu.ogg')

        self.life = 3
        self.pts = 0

    def moveBee(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30

    def colision(self, group, name):

        name = name
        colision = pygame.sprite.spritecollide(self.sprite, group, True)

        if name == 'Flower' and colision:
            self.pts += 1
            self.soundPts.play()
        elif name == 'Spider' and colision:
            self.life -= 1
            self.soundBlock.play()

class Text:

    def __init__(self, x, text):

        self.font = pygame.font.SysFont('Arial Bold', x)
        self.render = self.font.render(text, True, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def updateText(self, update):
        self.render = self.font.render(update, True, (255, 255, 255))

