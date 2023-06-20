import pygame
import src.consts as consts
import math
import src.render_text as render_text


class Ruler:
    def __init__(self, surface: pygame.Surface):
        self.screen = surface
        self.distance = 0
        self.cursor_pos = pygame.mouse.get_pos()
        self.point_positions = [self.cursor_pos, self.cursor_pos]

    def draw(self):
        self.get_distance()
        self.draw_line_between_point_and_cursor()
        self.make_point()
        self.print_coordinates_on_points()
        self.print_distance_on_line()
        self.cursor_pos = pygame.mouse.get_pos()

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
