import pygame
import random

pygame.init()

# Установка размеров окна игры
WIDTH = 800
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид")

# Цвета
Black = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
brick_image = pygame.image.load("i2.jpg")


# Класс для создания платформы игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - self.width) // 2
        self.rect.y = HEIGHT - self.height - 10
        self.speed = 5

    def update(self):
        # Движение платформы влево и вправо при нажатии клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Ограничение движения платформы по границам окна
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


# Класс для создания шарика
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = -3

    def update(self):
        # Движение шарика
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Отскок от стенок окна
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

        # Проверка на столкновение с платформой игрока
        if pygame.sprite.collide_rect(self, player):
            self.speed_y *= -1

        # Проверка на столкновение с кирпичиками
        brick_hit = pygame.sprite.spritecollide(self, bricks_group, True)
        if brick_hit:
            self.speed_y *= -1

        if self.rect.bottom > HEIGHT:
            game_over()

    # Функция для отображения "GAME OVER" и завершения игры


def game_over():
    window.fill(Black)
    font = pygame.font.Font(None, 60)
    text = font.render("GAME OVER", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()


# Класс для создания кирпичиков
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(brick_image, (70, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Группы спрайтов
all_sprites = pygame.sprite.Group()
bricks_group = pygame.sprite.Group()

# Создание платформы игрока
player = Player()
all_sprites.add(player)

# Создание шарика
ball = Ball()
all_sprites.add(ball)

# Создание кирпичиков
for row in range(4):
    for col in range(10):
        brick = Brick(1 + col * 80, 25 + row * 25)
        all_sprites.add(brick)
        bricks_group.add(brick)

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
while running:
    # Ограничение FPS
    clock.tick(60)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление спрайтов
    all_sprites.update()

    # Отрисовка спрайтов и фона
    window.fill(Black)
    all_sprites.draw(window)

    # Проверка окончания игры
    if ball.rect.bottom >= HEIGHT:
        # Перезапуск игры
        ball = Ball()
        all_sprites.add(ball)

    pygame.display.flip()

pygame.quit()