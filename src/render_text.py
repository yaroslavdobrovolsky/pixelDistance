import pygame


def render_text(surface: pygame.Surface, text: str, coordinates: tuple[int or float, int or float], font: str,
                font_size=20,
                color: tuple[int, int, int] = (255, 255, 255), background_color: tuple[int, int, int] = (0, 0, 0)):
    font = pygame.font.Font(font, font_size)
    text_to_render = font.render(text, True, color, background_color)
    text_to_render_rect = text_to_render.get_rect()
    text_to_render_rect.center = coordinates

    surface.blit(text_to_render, text_to_render_rect)


def render_multiple_text(surface: pygame.Surface, text: list[str], coordinates: tuple[int or float, int or float],
                         font: str,
                         font_size=20,
                         color: tuple[int, int, int] = (255, 255, 255),
                         background_color: tuple[int, int, int] = (0, 0, 0)):

    font = pygame.font.Font(font, font_size)

    for i in range(0, len(text)):
        count = i

        if i > len(text)/2:
            count = -count

        text_to_render = font.render(text[i], True, color, background_color)
        text_to_render_rect = text_to_render.get_rect()
        text_to_render_rect.center = (coordinates[0], (coordinates[1]+i*font_size)-(font_size*len(text))/2)

        surface.blit(text_to_render, text_to_render_rect)
