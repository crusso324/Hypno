import pygame
import sys
import math
import argparse
import itertools


def parse_args():
    parser = argparse.ArgumentParser(description="Hypnotic spiral generator")
    parser.add_argument('--width', type=int, default=800, help='Window width')
    parser.add_argument('--height', type=int, default=600, help='Window height')
    parser.add_argument('--text', type=str, default='', help='Overlay text')
    parser.add_argument('--text-color', type=str, default='white', help='Text color name')
    parser.add_argument('--flash-rate', type=float, default=0.0, help='Flash frequency in Hz')
    parser.add_argument('--show-dots', action='store_true', help='Overlay rotating dots')
    parser.add_argument('--show-cross', action='store_true', help='Overlay rotating cross')
    parser.add_argument('--speed', type=float, default=0.05, help='Spiral rotation speed (radians/frame)')
    return parser.parse_args()


def draw_spiral(surface, angle, color=(255, 255, 255)):
    cx, cy = surface.get_width() // 2, surface.get_height() // 2
    max_radius = min(cx, cy) - 10
    points = []
    theta = 0.0
    while theta < 10 * math.pi:
        r = max_radius * theta / (10 * math.pi)
        x = cx + r * math.cos(theta + angle)
        y = cy + r * math.sin(theta + angle)
        points.append((x, y))
        theta += 0.1
    if len(points) > 1:
        pygame.draw.lines(surface, color, False, points, 2)


def draw_overlay_text(surface, text, color):
    if not text:
        return
    font = pygame.font.SysFont(None, 48)
    text_surf = font.render(text, True, pygame.Color(color))
    rect = text_surf.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
    surface.blit(text_surf, rect)


def draw_dots(surface, angle, color=(0, 255, 0)):
    cx, cy = surface.get_width() // 2, surface.get_height() // 2
    radius = min(cx, cy) // 2
    for i in range(8):
        theta = angle + i * math.pi / 4
        x = cx + radius * math.cos(theta)
        y = cy + radius * math.sin(theta)
        pygame.draw.circle(surface, color, (int(x), int(y)), 5)


def draw_cross(surface, angle, color=(255, 0, 0)):
    cx, cy = surface.get_width() // 2, surface.get_height() // 2
    length = min(cx, cy) // 2
    for i in range(4):
        theta = angle + i * math.pi / 2
        x = cx + length * math.cos(theta)
        y = cy + length * math.sin(theta)
        pygame.draw.line(surface, color, (cx, cy), (int(x), int(y)), 3)


def main():
    args = parse_args()
    pygame.init()
    screen = pygame.display.set_mode((args.width, args.height))
    clock = pygame.time.Clock()

    angle = 0.0
    flash_states = itertools.cycle([(0,0,0), (255,255,255)]) if args.flash_rate > 0 else None
    next_flash_time = 0.0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        angle += args.speed

        if flash_states:
            current_time = pygame.time.get_ticks() / 1000.0
            if current_time >= next_flash_time:
                flash_color = next(flash_states)
                next_flash_time = current_time + 1.0 / args.flash_rate
            screen.fill(flash_color)
        else:
            screen.fill((0, 0, 0))

        draw_spiral(screen, angle)
        if args.show_dots:
            draw_dots(screen, angle)
        if args.show_cross:
            draw_cross(screen, angle)
        draw_overlay_text(screen, args.text, args.text_color)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
