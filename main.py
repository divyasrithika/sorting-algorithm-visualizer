import pygame
import random
import sys

pygame.init()

# Window size
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Array settings
ARRAY_SIZE = 50
array = [random.randint(50, 500) for _ in range(ARRAY_SIZE)]

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()


def draw_array(highlight1=-1, highlight2=-1):
    screen.fill(BLACK)

    bar_width = WIDTH // len(array)

    for i, value in enumerate(array):
        x = i * bar_width
        y = HEIGHT - value

        color = GREEN

        if i == highlight1 or i == highlight2:
            color = RED

        pygame.draw.rect(screen, color, (x, y, bar_width, value))

    pygame.display.update()


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def bubble_sort():
    for i in range(len(array)):
        for j in range(len(array) - i - 1):

            check_events()

            draw_array(j, j + 1)
            pygame.time.delay(20)

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def selection_sort():
    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):

            check_events()

            draw_array(min_index, j)
            pygame.time.delay(20)

            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


def insertion_sort():
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:

            check_events()

            array[j + 1] = array[j]
            j -= 1

            draw_array(j, i)
            pygame.time.delay(20)

        array[j + 1] = key


def reset_array():
    global array
    array = [random.randint(50, 500) for _ in range(ARRAY_SIZE)]


running = True

while running:

    clock.tick(60)

    draw_array()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_b:
                bubble_sort()

            if event.key == pygame.K_s:
                selection_sort()

            if event.key == pygame.K_i:
                insertion_sort()

            if event.key == pygame.K_r:
                reset_array()