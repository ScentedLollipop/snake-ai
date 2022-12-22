import pygame
import random
import numpy as np

pygame.init()

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BLOCK_SIZE = 20
font = pygame.font.Font('arial.ttf', 25)


class SnakeEnv:
    def __init__(self):
        # display setup
        self.width = 640
        self.height = 480
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake DQL')

        self.direction = None
        self.snake = []
        self.head = []
        self.game_timer = None
        self.score = None
        self.reward = None
        self.food = None

    def start(self):
        self.game_timer = 0
        self.direction = 'RIGHT'
        self.head = [self.width // 2, self.height // 2]
        self.snake = [self.head, [self.head[0] - BLOCK_SIZE, self.head[1]],
                      [self.head[0] - 2 * BLOCK_SIZE, self.head[1]]]
        self.score = 0
        self.generate_food()

    def draw_window(self):
        self.display.fill(BLACK)
        for part in self.snake:
            pygame.draw.rect(self.display, GREEN, pygame.Rect(part[0], part[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food[0], self.food[1]))
        score_txt = font.render('Score: ' + str(self.score), True, WHITE)
        self.display.blit(score_txt, [0, 0])

    def check_collision(self):
        # hits boundary
        if self.head[0] > self.width - BLOCK_SIZE or self.head[0] < 0 \
                or self.head[1] > self.height - BLOCK_SIZE or self.head[1] < 0:
            return True
        # hits itself
        if self.head in self.snake[1:]:
            return True
        return False

    def play_move(self, action):
        self.game_timer += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self.move(action)
        self.snake.insert(0, self.head)

        reward = 0

        if self.head == self.food:
            self.score += 1
            reward = 10
            self.generate_food()
        else:
            self.snake.pop()

        game_over = False
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        self.draw_window()
        return reward, game_o, self.score

    def move(self, action):
        # [straight, right, left]

        clock_wise = ['RIGHT', 'DOWN', 'LEFT', 'UP']
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]  # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]  # right turn r -> d -> l -> u
        else:  # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]  # left turn r -> u -> l -> d

        self.direction = new_dir

        if self.direction == 'RIGHT':
            self.head[0] += BLOCK_SIZE
        elif self.direction == 'LEFT':
            self.head[0] -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            self.head[1] += BLOCK_SIZE
        elif self.direction == 'UP':
            self.head[1] -= BLOCK_SIZE

    def generate_food(self):
        self.food = [random.randint((0, self.width // BLOCK_SIZE) * BLOCK_SIZE),
                     random.randint((0, self.height // BLOCK_SIZE) * BLOCK_SIZE)]
        if self.food in self.snake:
            self.generate_food()

    def play_step(self):
        self.game_timer += 1
        self.reward = 0
