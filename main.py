import pygame

def main():
    pygame.init()
    screen_height, screen_width = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Color changing rectangle')  

    color = {
        "red": pygame.Color('red'),
        "green": pygame.Color('green'),
        "blue": pygame.Color('blue'),
        "yellow": pygame.Color('yellow'),
        "purple": pygame.Color('purple'),
        "white": pygame.Color('white')  
    }    

    current_colour = color['purple']

    x, y = 30, 30
    sprite_height, sprite_width = 40, 40

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        elif pressed[pygame.K_DOWN]: y += 3
        elif pressed[pygame.K_LEFT]: x -= 3
        elif pressed[pygame.K_RIGHT]: x += 3

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        if x == 0: 
            current_colour = color['blue']  
        elif x == screen_width - sprite_width: 
            current_colour = color['red']  
        elif y == 0: 
            current_colour = color['green']  
        elif y == screen_height - sprite_height: 
            current_colour = color['yellow']  
        else:
            current_colour = color['white']  

        screen.fill((0, 0, 0))  
        pygame.draw.rect(screen, current_colour, (x, y, sprite_width, sprite_height))
        pygame.display.flip()  
        clock.tick(90)

    pygame.quit()  
if __name__ == "__main__":
    main()