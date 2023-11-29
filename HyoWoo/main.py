import pygame 
 
pygame.init() 
 
WHITE = (255,255,255)
size = [400,300]
screen = pygame.display.set_mode(size)
 
done= False
clock= pygame.time.Clock()
 
airplane = pygame.image.load('https://github.com/kanglossom/includePrac/blob/e220941254fb6e03093249152ba009c0e8b20709/HyoWoo/plane.png')
airplane = pygame.transform.scale(airplane, (60, 45))
 
def runGame():
    global done, airplane
    x = 20
    y = 24
 
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 10
                elif event.key == pygame.K_DOWN:
                    y += 10
    
        screen.blit(airplane, (x, y))
        pygame.display.update()
