import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close Window
            pygame.quit()  # End pygame