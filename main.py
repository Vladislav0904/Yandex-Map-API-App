import os
import pygame
import requests

if __name__ == '__main__':
    data = ['61.390953,55.164724', ['0.01', '0.01']]
    toponym_to_find = data
    search_api_server = "https://static-maps.yandex.ru/1.x/"
    def map():
        search_params = {
            "ll": toponym_to_find[0],
            "spn": ','.join(toponym_to_find[1]),
            "l": "map"
        }
        print(toponym_to_find[1][1])
        response = requests.get(search_api_server, params=search_params)
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        pygame.init()
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        screen = pygame.display.set_mode((600, 450))
        screen.blit(pygame.image.load(map_file), (0, 0))
        font = pygame.font.Font(None, 20)
        return map_file
    running = True
    map()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        toponym_to_find_float1 = float(toponym_to_find[1][0])
        toponym_to_find_float2 = float(toponym_to_find[1][1])
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_PAGEUP]:
                toponym_to_find_float1 += 0.01
                toponym_to_find_float2 += 0.01
                map()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_PAGEDOWN]:
                toponym_to_find_float1 -= 0.01
                toponym_to_find_float2 -= 0.01
                map()
        toponym_to_find[1][0] = str(toponym_to_find_float1)
        toponym_to_find[1][1] = str(toponym_to_find_float2)

        print(toponym_to_find[1][0])
# text = 'Адрес:'
# text_screen = font.render(text, True, (100, 50, 255))
# screen.blit(text_screen, (0, 0))
        pygame.display.flip()

    pygame.quit()
    os.remove(map())
