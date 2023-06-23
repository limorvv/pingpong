from pygame import *

from random import randint

# разрешение для игрового объекта
SPRITE_RESOLUTION = (100, 100)
class GameSprite(sprite.Sprite):
    def __init__(self, x : int, y : int, filename : str, speed : int, resolution = SPRITE_RESOLUTION):
        super().__init__()
        self.speed = speed

        # загрузка текстуры
        self.image = transform.scale(image.load(filename), resolution)

        # настройка хитбокса
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # отображение спрайта
    def reset(self):
        window.blit(self.image, (self.rect.x , self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    # "Обновление" местоположения
    def update_l(self):

        keys = key.get_pressed()

        if keys[K_a] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.y < 615:
            self.rect.x += self.speed

    def update_r(self):

        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < 615:
            self.rect.x += self.speed

class Ball(GameSprite):
    def __init__(self,x: int, y: int, filename : str, speed : int, resolution = SPRITE_RESOLUTION):
        super().__init__(x, y, filename, speed, resolution)
        self.speed_x = speed
        self.speed_y = speed

    def update(self):
        if not (self.rect.x > 5 and self.rect.x < 1175):
            self.rect.x *= -1
        if not (self.rect.y > 5 and self.rect.y < 615):
            self.rect.y *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

RESOLUTION = (1280, 720)
window = display.set_mode(RESOLUTION)
window.fill((225, 225, 225))

player_1 = Player(0, 310, 'racket.png', 5)
player_2 = Player(0, 310, 'racket.png', 5)

ball = Ball(590, 310, 'ball.png', 5)

while game:
# Обработка событий
    # Закрытие приложения
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

        player_1.reset()
        player_2.reset()
        ball.reset()

        player_1.update()
        player_2.update()
        ball.update()






# Смена кадра
    display.update()






            
            
