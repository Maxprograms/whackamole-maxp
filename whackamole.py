import pygame
import random

screen = pygame.display.set_mode((640, 512))
mole_image = pygame.image.load("mole.png")

def draw_grid(screen): 
    for i in range(0, 640, 32):
        pygame.draw.line(screen, 'black', (i, 0), (i, 512))
    for i in range(0, 512, 32):
        pygame.draw.line(screen, 'black', (0, i), (640, i))

def draw_mole(x, y):
    screen.blit(mole_image, (x * 32, y * 32))

def main():
    try:
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        x, y = 0, 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_x, click_y = event.pos
                        grid_x, grid_y = click_x // 32, click_y // 32
                        if (grid_x, grid_y) == (x, y):
                            x = random.randint(0 ,19)
                            y = random.randint(0, 15)
            screen.fill("light green")
            draw_grid(screen)
            draw_mole(x, y)
            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
