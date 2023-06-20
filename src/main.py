import pygame
import sys
import pyautogui
import os
import consts
import tools.ruler


class App:
    def __init__(self):
        self.screenshot = pyautogui.screenshot()
        self.screenshot.save(consts.SCREENSHOT_NAME)

        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(consts.CAPTION)

        self.tool = "ruler"

        self.ruler = tools.ruler.Ruler(self.screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        os.remove(consts.SCREENSHOT_NAME)
                        pygame.quit()
                        sys.exit()

            self.draw_background()

            match self.tool:
                case "ruler": self.ruler.draw()
                case _: pass

            pygame.display.flip()

    def draw_background(self):
        img = pygame.image.load(consts.SCREENSHOT_NAME)
        self.screen.blit(img, (0, 0))


if __name__ == "__main__":
    a = App()
