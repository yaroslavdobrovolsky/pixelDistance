import pygame
import sys
import math
import pyautogui
import os
import consts
import render_text


class App:
    def __init__(self):
        self.screenshot = pyautogui.screenshot()
        self.screenshot.save(consts.SCREENSHOT_NAME)

        pygame.init()

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
        render_text.render_text(self.screen, str(self.distance),
                                ((self.point_positions[0][0] + self.point_positions[1][0]) / 2,
                                 (self.point_positions[0][1] + self.point_positions[1][1]) / 2),
                                consts.FONT, consts.FONT_SIZE, consts.FONT_COLOR, consts.BACKGROUND_FONT_COLOR)

    def print_coordinates_on_points(self):
        render_text.render_multiple_text(self.screen,
                                         [str(self.point_positions[0][0]), str(self.point_positions[0][1])],
                                         self.point_positions[0], consts.FONT, consts.FONT_SIZE,
                                         consts.FONT_COLOR, consts.BACKGROUND_FONT_COLOR)

        render_text.render_multiple_text(self.screen,
                                         [str(self.point_positions[1][0]), str(self.point_positions[1][1])],
                                         self.point_positions[1], consts.FONT, consts.FONT_SIZE,
                                         consts.FONT_COLOR, consts.BACKGROUND_FONT_COLOR)

    def draw_background(self):
        img = pygame.image.load(consts.SCREENSHOT_NAME)
        self.screen.blit(img, (0, 0))


if __name__ == "__main__":
    a = App()
