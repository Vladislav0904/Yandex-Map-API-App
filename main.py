import os
import pygame
import requests

data = ['61.390953,55.164724', '0.01,0.01']

toponym_to_find = data
search_api_server = "https://static-maps.yandex.ru/1.x/"
search_params = {
    "ll": toponym_to_find[0],
    "spn": toponym_to_find[1],
    "l": "map"
}
response = requests.get(search_api_server, params=search_params)
map_api_server = "http://static-maps.yandex.ru/1.x/"
pygame.init()
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
font = pygame.font.Font(None, 20)
# text = 'Адрес:'
# text_screen = font.render(text, True, (100, 50, 255))
# screen.blit(text_screen, (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
