import logging
import sys

import pygame

import logger.custom_logger as cl
from src import level, settings


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )
        pygame.display.set_caption('Sprout land')
        self.clock = pygame.time.Clock()
        self.level = level.Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


def main():
    cl.setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Game started.")

    game = Game()
    game.run()


if __name__ == '__main__':
    main()
