import pygame
import sys
import math
import pyautogui
import os
import consts


class App:
    def __init__(self):
        self.screenshot = pyautogui.screenshot()
        self.screenshot.save(consts.SCREENSHOT_NAME)

        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(consts.CAPTION)

        self.distance = 0
        self.cursor_pos = pygame.mouse.get_pos()
        self.point_position = self.cursor_pos

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        os.remove(consts.SCREENSHOT_NAME)
                        pygame.quit()
                        sys.exit()

            self.draw()
            self.cursor_pos = pygame.mouse.get_pos()

    def draw(self):
        self.draw_background()
        self.get_distance()
        self.draw_line_between_point_and_cursor()
        self.make_point()
        self.print_distance_on_line()

        pygame.display.flip()

    def make_point(self):
        if pygame.mouse.get_pressed()[0]:
            self.point_position = self.cursor_pos

        pygame.draw.circle(self.screen, consts.POINT_COLOR, self.cursor_pos, consts.POINT_RADIUS)
        pygame.draw.circle(self.screen, consts.POINT_COLOR, self.point_position, consts.POINT_RADIUS)

    def get_distance(self):
        self.distance = int(math.sqrt(abs(self.point_position[0] - self.cursor_pos[0]) ** 2 +
                                      abs(self.point_position[1] - self.cursor_pos[1]) ** 2)) + 1

    def draw_line_between_point_and_cursor(self):
        pygame.draw.line(self.screen, consts.LINE_COLOR, self.point_position, self.cursor_pos, 2)

    def print_distance_on_line(self):
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render(str(self.distance), True, consts.FONT_COLOR, consts.BACKGROUND_FONT_COLOR)
        text_rect = text.get_rect()
        text_rect.center = ((self.point_position[0] + self.cursor_pos[0]) / 2,
                            (self.point_position[1] + self.cursor_pos[1]) / 2)

        self.screen.blit(text, text_rect)

    def print_coordinates_on_points(self):
        # todo: printing coordinates of points
        pass

    def draw_background(self):
        img = pygame.image.load(consts.SCREENSHOT_NAME)
        self.screen.blit(img, (0, 0))


if __name__ == "__main__":
    a = App()
