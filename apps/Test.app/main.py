import pygame, tools

class App:
    def __init__(self):
        self.background = pygame.image.load("MenuData/background.png").convert_alpha()
        self.font = pygame.font.SysFont("Arial", 48)
        self.text = self.font.render("Youtube is now under construction \nCome back again! \n\n\nPress O to go back to the menu", True, (255, 255, 255))

    def update(self, event):
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == tools.O_BUTTON: return 1

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.text, (400, 400))