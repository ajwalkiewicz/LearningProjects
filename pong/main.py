import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_w,
    K_s,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
from random import choice

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT = "Helvetica"


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 100))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.speed = 1
        self.score = 0


class LeftPlayer(Player):
    def __init__(self):
        super().__init__()
        self.rect = self.surf.get_rect(
            topleft=(
                0,
                (SCREEN_HEIGHT-self.surf.get_height())/2 + 50
            )
        )

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, self.speed)

        if self.rect.top <= 100:
            self.rect.top = 100
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class RightPlayer(Player):
    def __init__(self):
        super().__init__()
        self.rect = self.surf.get_rect(
            topleft=(
                SCREEN_WIDTH - self.surf.get_width(),
                (SCREEN_HEIGHT-self.surf.get_height())/2 + 50
            )
        )

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)

        if self.rect.top <= 100:
            self.rect.top = 100
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH/2,
                SCREEN_HEIGHT/2 + 50
            )
        )
        self.vx = choice((1, -1))
        self.vy = choice((1, -1))

    def update(self, left_player, right_player):
        self.rect.move_ip(self.vx, self.vy)

        if self.rect.top <= 100:
            self.rect.top = 100
            self.vy = -self.vy
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vy = -self.vy

        if self.rect.left < 0:
            left_player.score += 1
            self.reset_position()
        elif self.rect.right >= 800:
            right_player.score += 1
            self.reset_position()

    def bounce_from_player(self):
        self.vx = -self.vx

    def reset_position(self):
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH/2,
                SCREEN_HEIGHT/2 + 50
            )
        )
        self.vx = choice((1, -1))
        self.vy = choice((1, -1))


def write_scores(text, size, x=None, y=None):
    font = pygame.font.SysFont(FONT, size)
    rend = font.render(str(text), 1, (255, 255, 255))
    screen.blit(rend, (x, y))


def main():
    left_player = LeftPlayer()
    right_player = RightPlayer()
    ball = Ball()

    players = pygame.sprite.Group()
    players.add(left_player)
    players.add(right_player)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(left_player)
    all_sprites.add(right_player)
    all_sprites.add(ball)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                run = False

        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (0, 100), (800, 100))
        pygame.draw.line(screen, (255, 255, 255), (400, 100), (400, 600))

        write_scores(left_player.score, 75, 320, 10)
        write_scores(right_player.score, 75, 460, 10)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pressed_keys = pygame.key.get_pressed()

        left_player.update(pressed_keys)
        right_player.update(pressed_keys)
        ball.update(left_player, right_player)

        if pygame.sprite.spritecollideany(ball, players):
            ball.bounce_from_player()

        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main()
