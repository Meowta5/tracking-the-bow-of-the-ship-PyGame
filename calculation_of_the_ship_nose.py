from sys import exit
import math

import pygame

# Инициализация Pygame
pygame.init()

clock = pygame.time.Clock()

# Создание окна
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Отслеживание положения носа космического корабля")

# Загрузка изображения космического корабля
spaceship_img = pygame.image.load('versi1.png').convert_alpha()

# Квадрат космического корабля
spaceship_rect = spaceship_img.get_rect(center=(600, 300))

# Установка шрифта
font = pygame.font.Font(None, 36)

# Угол поворота
angle = 0


# Смена половин списка
def switch_lists(lst):
    half = len(lst) // 2
    new_lst = lst[half:] + lst[:half]
    return new_lst


# Создание круга координат
def create_invisible_circle(radius, center):
    points = []

    num_points = 360
    angle_increment = 2 * math.pi / num_points
    center_x, center_y = center

    for i in range(num_points):
        angle = i * angle_increment
        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        points.append((x, y))
    return points


# Поворот изображения
def rotate_towards_cursor(image, image_rect, cursor_pos):
    angle = math.degrees(math.atan2(cursor_pos[1] - image_rect.centery, cursor_pos[0] - image_rect.centerx))
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)
    return rotated_image, rotated_rect, int(angle)



# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Поворот корабля
    rotated_spaceship_img, rotated_spaceship_rect, angle = rotate_towards_cursor(spaceship_img, spaceship_rect, pygame.mouse.get_pos())


    point_circle = create_invisible_circle(spaceship_rect.center[0] - spaceship_rect.midright[0], spaceship_rect.center)

    nose_x, nose_y = switch_lists(point_circle)[angle]

    # Фон
    screen.fill((235, 255, 245))

    # Отображение корабля
    screen.blit(rotated_spaceship_img, rotated_spaceship_rect)

    # Отображение точки носа корабля
    pygame.draw.circle(screen, 'red', (nose_x, nose_y), 5)


    # Отображение координат носа на экране
    text = font.render(f"Nose Position: ({nose_x}, {nose_y})", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Рендер
    pygame.display.update()
    clock.tick(60)