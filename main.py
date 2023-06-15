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

        self.font = pygame.font.Font(consts.FONT, consts.FONT_SIZE)

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(consts.CAPTION)

        self.distance = 0
        self.cursor_pos = pygame.mouse.get_pos()
        self.point_positions = [self.cursor_pos, self.cursor_pos]

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
        self.print_coordinates_on_points()
        self.print_distance_on_line()

        pygame.display.flip()

    def make_point(self):
        if pygame.mouse.get_pressed()[0]:
            self.point_positions[0] = self.cursor_pos
        if pygame.mouse.get_pressed()[2]:
            self.point_positions[1] = self.cursor_pos

    def get_distance(self):
        self.distance = int(math.sqrt((self.point_positions[0][0] - self.point_positions[1][0]) ** 2 +
                                      (self.point_positions[0][1] - self.point_positions[1][1]) ** 2)) + 1

    def draw_line_between_point_and_cursor(self):
        pygame.draw.line(self.screen, consts.LINE_COLOR, self.point_positions[0], self.point_positions[1], 1)

    def print_distance_on_line(self):
        text = self.font.render(str(self.distance), True, consts.FONT_COLOR, consts.BACKGROUND_FONT_COLOR)
        text_rect = text.get_rect()
        text_rect.center = ((self.point_positions[0][0] + self.point_positions[1][0]) / 2,
                            (self.point_positions[0][1] + self.point_positions[1][1]) / 2)

        self.screen.blit(text, text_rect)

    def print_coordinates_on_points(self):
        # todo: make coordinate render with multiple lines

        first_point_coordinates_text = self.font.render(str(self.point_positions[0]), True,
                                                        consts.FONT_COLOR, consts.BACKGROUND_FONT_COLOR)
        first_point_coordinates_text_rect = first_point_coordinates_text.get_rect()
        first_point_coordinates_text_rect.center = self.point_positions[0]

        second_point_coordinates_text = self.font.render(str(self.point_positions[1]), True,
                                                         consts.FONT_COLOR, consts.BACKGROUND_FONT_COLOR)
        second_point_coordinates_text_rect = second_point_coordinates_text.get_rect()
        second_point_coordinates_text_rect.center = self.point_positions[1]

        self.screen.blit(first_point_coordinates_text, first_point_coordinates_text_rect)
        self.screen.blit(second_point_coordinates_text, second_point_coordinates_text_rect)

    def draw_background(self):
        img = pygame.image.load(consts.SCREENSHOT_NAME)
        self.screen.blit(img, (0, 0))


if __name__ == "__main__":
    a = App()
