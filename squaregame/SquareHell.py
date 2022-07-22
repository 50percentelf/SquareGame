
import pygame
import sys
from pygame.locals import *


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
RED = (230, 50, 50)
BLUE = (50, 50, 230)
GREEN = (50, 230, 50)
YELLOW = (255, 255, 0)
square_width = 250
square_height = 250

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

sq1_cycle = 0
sq2_cycle = 1
sq3_cycle = 2
sq4_cycle = 3
#Draw the squares
#Load sounds
pygame.mixer.init()
scare_sound = pygame.mixer.Sound("sound.wav")


def check_for_winner():
    global sq1_cycle, sq2_cycle, sq3_cycle, sq4_cycle
    are_you_a_winner = "yes"
    print("checking for winner...")
    if sq1_cycle == sq2_cycle == sq3_cycle == sq4_cycle:
        distribute_prize()


def distribute_prize():
    #print("YOU WIN")
    scare_sound.play()
    jump = pygame.image.load("image.png")
    screen.blit(jump, (0, 0))
    pygame.display.update()


def color_cycle(cycle):
    if cycle == 5:
        cycle = 0
    if cycle < 5:
        color = [RED, BLUE, GREEN, YELLOW, RED]
       # cycle += 1
        return color[cycle]




def draw_tl_square():

    # square int TL_RED
    square(1, RED)
    #pygame.draw.rect(screen, RED, Rect((x, y), (square_width, square_height)))



def draw_tr_square():
    # square int TR_BLUE
    square(2, BLUE)
    #pygame.draw.rect(screen, BLUE, Rect((x, y), (square_width, square_height)))


def draw_bl_square():
    # square int BL_GREEN
    square(3, GREEN)
    #pygame.draw.rect(screen, GREEN, Rect((x, y), (square_width, square_height)))


def draw_br_square():
    # square int BR_YELLOW
    square(4, YELLOW)
    #pygame.draw.rect(screen, YELLOW, Rect((x, y), (square_width, square_height)))


def square(square, color):
    if square == 1:
        x = 180
        y = 150
        pygame.draw.rect(screen, color, Rect((x, y), (square_width, square_height)))
    if square == 2:
        x = 430
        y = 150
        pygame.draw.rect(screen, color, Rect((x, y), (square_width, square_height)))
    if square == 3:
        x = 180
        y = 400
        pygame.draw.rect(screen, color, Rect((x, y), (square_width, square_height)))
    if square == 4:
        x = 430
        y = 400
        pygame.draw.rect(screen, color, Rect((x, y), (square_width, square_height)))

#returns the starting color of the square based on coords
def check_square(x, y):

    red_square = False
    blue_square = False
    green_square = False
    yellow_square = False

    #checks square coordinates possible to change square colors from here?
    if 180 <= x <= 430 and 400 >= y >= 150:

        change_squares(1)
        pygame.display.update()
        #change square function hre?
        return print("ONE")
    if 430 <= x <= 680 and 400 >= y >= 150:
        change_squares(2)
        pygame.display.update()
        return print("TWO")
    if 180 <= x <= 430 and 650 >= y >= 400:
        change_squares(3)
        pygame.display.update()
        return print("THREE")
    if 430 <= x <= 680 and 650 >= y >= 400:
        change_squares(4)
        pygame.display.update()
        return print("FOUR")


#attepmting to change squares.. dont know how to blit app yet

def change_squares(square_to_change):
    #Make global to calc sq cycle
    global sq1_cycle, sq2_cycle, sq3_cycle, sq4_cycle
    colors = [RED, BLUE, GREEN, YELLOW]
    # change square to next color
    square_width = 250
    square_height = 250
    square_has_changed = 0
   # x = 180 not sure why i had these, prob clean these out
   #y = 150 "" "" " "" " "" "

#TL make sure to check cycle============================================
    if square_to_change == 1 and sq1_cycle < 4:
        sq1_cycle += 1
        square(1, color_cycle(sq1_cycle))

        #pygame.draw.rect(screen, BLUE, Rect((x, y), (square_width, square_height)))
        #You should be drawing current square cycle, not initial???
        sq2_cycle += 1
        sq3_cycle += 1
        if sq1_cycle == 4:
            sq1_cycle = 0
        if sq2_cycle == 4:
            sq2_cycle = 0
        if sq3_cycle == 4:
            sq3_cycle = 0
        square(2, color_cycle(sq2_cycle))
        square(3, color_cycle(sq3_cycle))
        square(4, color_cycle(sq4_cycle))
        pygame.display.update()


     #square_has_changed += 0

#TR----------------============================================
    if square_to_change == 2 and sq2_cycle < 4:
        sq2_cycle += 1
        sq1_cycle += 1
        sq4_cycle += 1
        square(2, color_cycle(sq2_cycle))

        if sq1_cycle == 4:
            sq1_cycle = 0
        if sq2_cycle == 4:
            sq2_cycle = 0
        if sq4_cycle == 4:
            sq4_cycle = 0
        #pygame.draw.rect(screen, YELLOW, Rect((x, y), (square_width, square_height)))
        square(1, color_cycle(sq1_cycle))
        square(3, color_cycle(sq3_cycle))
        square(4, color_cycle(sq4_cycle))
        pygame.display.update()
        print("Attempting to change square..")
#BL============================================================

    if square_to_change == 3 and sq3_cycle < 4:

        sq3_cycle += 1
        sq1_cycle += 1
        sq4_cycle += 1
        square(3, color_cycle(sq3_cycle))
        if sq3_cycle == 4:
            sq3_cycle = 0
        if sq1_cycle == 4:
            sq1_cycle = 0
        if sq4_cycle == 4:
            sq4_cycle = 0
        square(1, color_cycle(sq1_cycle))
        square(2, color_cycle(sq2_cycle))
        square(4, color_cycle(sq4_cycle))
        pygame.display.update()
        #square_has_changed += 0
#BR==========================================================
    if square_to_change == 4 and sq4_cycle < 4:

        sq4_cycle += 1
        sq3_cycle += 1
        sq2_cycle += 1
        square(4, color_cycle(sq4_cycle))
        if sq4_cycle == 4:
            sq4_cycle = 0
        if sq3_cycle == 4:
            sq3_cycle = 0
        if sq2_cycle == 4:
            sq2_cycle = 0
        #pygame.draw.rect(screen, GREEN, Rect((x, y), (square_width, square_height)))
        square(1, color_cycle(sq1_cycle))
        square(2, color_cycle(sq2_cycle))
        square(3, color_cycle(sq3_cycle))
        pygame.display.update()
        print("Attempting to change square..")
        return





#----------before main game loop draw initial squares----
draw_bl_square()
draw_br_square()
draw_tl_square()
draw_tr_square()
pygame.display.update()
screen.fill((0, 0, 0))
#-----


while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:

            click_x, click_y = pygame.mouse.get_pos()
            check_square(click_x, click_y)
            print(pygame.mouse.get_pos())
            print("Test")
            check_for_winner()

            #pygame.display.update()





