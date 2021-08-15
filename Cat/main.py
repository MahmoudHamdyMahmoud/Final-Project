import pygame
YELLOW = (255, 228, 196)
BLUE = (30, 144, 255)
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH = 117.6
HEIGHT = 117.6
MARGIN = 3
grid = []
for row in range(5):
    grid.append([])
    for column in range(5):
        grid[row].append(0)
grid[0][0] = 1
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.init()
win = pygame.display.set_mode((800, 800))
win.fill(YELLOW)
pygame.draw.rect(win, BLUE, [50, 50, 700, 700])
pygame.draw.rect(win, BLACK, [100, 100, 600, 600])

for row in range(5):
    for column in range(5):
        color = GREEN
        if grid[row][column] == 1:
            color = GREEN
        pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * (column + 0.81) + MARGIN,
                          (MARGIN + HEIGHT) * (row + 0.81) + MARGIN,
                          WIDTH,
                          HEIGHT])
image = pygame.image.load('Image/cat2.png')
win.blit(image, (110, 110))
image = pygame.image.load('Image/mouse.png')
win.blit(image, (220, 220))

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()