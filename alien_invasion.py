import game_functions as gf
import pygame

from pygame.sprite import Group
from settings import Settings

from ship import Ship
from alien import Alien
def run_game():
    # Initialize pygame, Setting and  screen object.
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_setting, screen)
    # Make a group to store bullets in.
    bullets = Group()
    #makeing a group of bullets.
    aliens = Group()

    #Make an alien
    alien = Alien(ai_setting, screen)
    # Create the fleet of aliens.
    gf.create_fleet(ai_setting, screen, aliens, ship)

    #Start the main loop for the game.
    while True:
        #Watch for keyboard and mouse events.
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
        gf.update_aliens(ai_setting, aliens)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets)


run_game()
