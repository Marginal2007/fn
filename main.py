import os
import sys

import pygame
import requests


running = True

map_request = "http://static-maps.yandex.ru/1.x/?ll=46.707,-18.9875&spn=10,10&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while running:
    if pygame.event.wait().type == pygame.QUIT:
        running = False
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)