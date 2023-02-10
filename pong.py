import pygame,random
SIZE = 10
BAT_H = 100
WIDTH = 700
HEIGHT = 600
RYCHLOST_LOPTY = 2
BAT_SPEED = 10

def square(x, y):
    return pygame.Rect(int(x), int(y), SIZE, SIZE)
def bat(x,y):
    return pygame.Rect(int(x),int(y), SIZE, BAT_H)

def game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont("Consolas", 20)
    movement = [1,1]
    ball_x = (WIDTH - SIZE) / 2
    ball_y = HEIGHT / 2
    bat_x = WIDTH - SIZE
    bat_y = (HEIGHT / 2) - (BAT_H / 2)
    bat2_x = 0
    bat2_y = (HEIGHT / 2) - (BAT_H / 2)
    pointsL = 0
    pointsR = 0
    end = False


    while not end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        if ball_x < 0:
            pointsL +=1
            ball_x = (WIDTH - SIZE) / 2
            ball_y = HEIGHT / 2
            movement[0] = 1

        if ball_y < 0:
            movement[1] = 1

        if ball_x > (WIDTH - SIZE):
            pointsR +=1
            ball_x = (WIDTH - SIZE) / 2
            ball_y = HEIGHT / 2
            movement[0] = -1


        if ball_y > (HEIGHT - SIZE):
            movement[1] = -1



        ball_x += RYCHLOST_LOPTY * movement[0]
        ball_y += RYCHLOST_LOPTY * movement[1]

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            bat_y -= BAT_SPEED


        if pressed[pygame.K_DOWN]:
            bat_y += BAT_SPEED

        if pressed[pygame.K_w]:
            bat2_y -= BAT_SPEED


        if pressed[pygame.K_s]:
            bat2_y += BAT_SPEED



        screen.fill((0,0,0))
        ball = pygame.draw.rect(screen, (255,255,255), square(ball_x, ball_y))
        bat1 = pygame.draw.rect(screen, (255, 255, 255), bat(bat_x,bat_y))
        bat2 = pygame.draw.rect(screen, (255, 255, 255), bat(bat2_x, bat2_y))
        text_surface = my_font.render(f'{pointsR} : {pointsL}', True, (255, 255, 255))
        if pygame.Rect.colliderect(ball, bat1):
            movement[0] = -1
        if pygame.Rect.colliderect(ball, bat2):
            movement[0] = 1
        screen.blit(text_surface, ((WIDTH - text_surface.get_width())/2, 0))
        pygame.display.flip()
        clock.tick(60)





def main():
    pygame.init()
    game()
    pygame.quit()

main()