from obj import Obj, Bee, Text
import random


class Game:

    def __init__(self):

        self.bg = Obj('assets/bg.png', 0, 0)
        self.bg2 = Obj('assets/bg.png', 0, -640)

        self.spider = Obj('assets/spider1.png', random.randrange(0, 300), -50)
        self.flower = Obj('assets/florwer1.png', random.randrange(0, 300), -50)
        self.bee = Bee('assets/bee1.png', 150, 600 )

        self.changeScene = False

        self.score = Text(70, '0')
        self.lifes = Text(30, '3')

    def draw(self, window):

        self.bg.draw(window)
        self.bg2.draw(window)
        self.bee.draw(window)
        self.spider.draw(window)
        self.flower.draw(window)
        self.score.draw(window, 170, 50)
        self.lifes.draw(window, 320, 20)



    def update(self):

        self.moveBg()
        self.spider.anim('spider', 8, 5 )
        self.flower.anim('florwer', 8, 3)
        self.bee.anim('bee', 2, 5)
        self.moveSpiders()
        self.moveFlower()
        self.bee.colision(self.spider.group, 'Spider')
        self.bee.colision(self.flower.group, 'Flower')
        self.gameOver()
        self.score.updateText(str(self.bee.pts))
        self.lifes.updateText(str(self.bee.life))



    def moveBg(self):
        self.bg.sprite.rect[1] += 10
        self.bg2.sprite.rect[1] += 10

        if self.bg.sprite.rect[1] > 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] > 0:
            self.bg2.sprite.rect[1] = -640

    def moveSpiders(self):
        self.spider.sprite.rect[1] += 11

        if self.spider.sprite.rect[1] >= 650:
            self.spider.sprite.kill()
            self.spider = Obj('assets/spider1.png', random.randrange(0, 300), -50)

    def moveFlower(self):
        self.flower.sprite.rect[1] += 6

        if self.flower.sprite.rect[1] >= 650:
            self.flower.sprite.kill()
            self.flower = Obj('assets/florwer1.png', random.randrange(0, 300), -50)


    def gameOver(self):
        if self.bee.life <= 0:
            self.changeScene = True



