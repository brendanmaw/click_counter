import pygame
# import pygame_widgets as pw
from pygame import font

pygame.init()
clock = pygame.time.Clock()
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Bmaw's Button Presser")
screen = pygame.display.set_mode([800, 800])
running = True
events = pygame.event.get()
game_header_font = pygame.font.SysFont('arial', 50, True)
game_header_surface = game_header_font.render("How high can you click it?", 1, (0, 0, 0))
counter_font = pygame.font.SysFont('arial', 50, True)
current_clicks = 0
mouseClicked = False

while running:
    clock.tick(60)
    screen.fill((116, 134, 142))
    # click_button.listen(events)
    # click_button.draw()
    screen.blit(game_header_surface, (90, 175))



    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseClicked = True
            if mouseClicked:
                if event.button == 1:
                    counter_font = pygame.font.SysFont('arial', 50, True)
                    current_clicks += 1
                    counter_font_surface = counter_font.render("Current Clicks: " + str(current_clicks), 1, (0, 0, 0))
                    screen.blit(counter_font_surface, (300, 675))
                else:
                    counter_font = pygame.font.SysFont('arial', 45, True)
                    counter_font_surface = counter_font.render("Invalid Input... " + str(current_clicks), 1, (0, 0, 0))

                    screen.blit(counter_font_surface, (300, 675))

            pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
