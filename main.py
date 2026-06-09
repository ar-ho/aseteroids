import pygame
import sys
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import *
from logger import log_event

def main():
    print("Starting Asteroids with pygame version: " + pygame.__version__)
    print(f"Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #creates the updatable, drawable groups and asteroids

    Player.containers = (updatable, drawable)
    #adds the player class to the updatable and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable)
    #adds the asteroid class to the updatable and drawable groups
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000
        ''''    
        print(f"{dt}")
        dt stands for delta time
        the amount of time that has passed since the last frame was drawn
        time between frames in seconds
        '''
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        pygame.display.flip()
        '''
        The sequence of the above code is important:
        Fill the screen with black first.
        Draw the player on top of that black background.
        Finally, call flip() to show the result.

        What does flip() do?
        Computer graphics use a technique called double buffering. 
        Imagine you have a double-sided chalkboard:
        Back Buffer: You are busy drawing, erasing, and filling the screen with black on the side of the board that is currently facing away from the audience.
        Front Buffer: This is the side currently facing the audience (the monitor).
        When you call pygame.display.flip(), it quickly flips the chalkboard around. Everything you just drew on the "back" becomes visible to the player all at once.
        '''

if __name__ == "__main__":
    main()