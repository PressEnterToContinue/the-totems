"""The application window and main loop."""

import pygame

# Window
SCREEN_SIZE = 800, 600

# Colors
DESKTOP = (0, 128, 128)  # Teal

# Misc
FPS = 60


def run() -> None:
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("The Totems")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(DESKTOP)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
