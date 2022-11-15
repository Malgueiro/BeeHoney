import pygame
from menu import Menu, GameOver
from game import Game


class Main:

    def __init__(self):

        pygame.init()

        pygame.mixer.init()
        pygame.mixer.music.load('sounds/bg.ogg')
        pygame.mixer.music.play(-1)



        self.window = pygame.display.set_mode([360, 640])
        self.title = pygame.display.set_caption('Bee Honey')

        self.loop = True
        self.fps = pygame.time.Clock()

        self.startScreen = Menu('assets/start.png')
        self.game = Game()
        self.gameOver = GameOver('assets/gameover.png')

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            if not self.startScreen.changeScene:
                self.startScreen.event(event)
            elif not self.game.changeScene:
                self.game.bee.moveBee(event)
            else:
                self.gameOver.event(event)



    def draw(self):
        self.window.fill([0, 0, 0])
        if not self.startScreen.changeScene:
            self.startScreen.draw(self.window)
        elif not self.game.changeScene:
            self.game.draw(self.window)
            self.game.update()
        elif not self.gameOver.changeScene:
            self.gameOver.draw(self.window)
        else:
            self.startScreen.changeScene = False
            self.game.changeScene = False
            self.gameOver.changeScene = False
            self.game.bee.life = 3
            self.game.bee.pts = 0

    def updates(self):

        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()

Main().updates()
