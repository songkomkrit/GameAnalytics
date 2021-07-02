"""
Role:       	Player (complement to space-wars-extended.py)
Author:     	Songkomkrit Chaiyakan
Github link:	https://github.com/songkomkrit/GameAnalytics

"""

import math

# Enter the player name before starting
reserved = ['#@$', ',', ':', '\'', '|', '=']
PLAYER_NAME = reserved[0]

def invalid_name(PLAYER_NAME):
    cond = PLAYER_NAME.upper() in ['SERVER', 'SERVERS']
    cond = cond or any([e in PLAYER_NAME for e in reserved])
    return cond

while invalid_name(PLAYER_NAME):
    PLAYER_NAME = input("Enter Player Name: ").upper()

print('Game starts now')


# Show name on the screen while playing
def show_player():
    y = 10
    message_display_center(PLAYER_NAME, font_small, 
                           (255, 255, 0), screen_sizeX/2, 2*y)


# Show top 3 scores while playing  
def show_top3():
        top3 = high_scores.high_scores_top_list(db_connection)[0:3]
        index = 0
        x = 10
        y = 10
        font_size = 16
        for entry in top3:
            # timestamp, name, score, date
            message_display_right(str(entry[1]), font_small, yellow,
                                  screen_sizeX-6.5*x, 2*y+(5+font_size)*index)
            message_display_right(str(entry[2]), font_small, yellow,
                                  screen_sizeX-x, 2*y+(5+font_size)*index)
            index += 1


# Add collectable coins (graphics and marks)
coin_image = pygame.image.load(os.path.join(images_path , 'coin.png'))
n = 5

def coin(score):
    return math.floor(score/n)

def show_coin_new(score):
    if (score > 0) and (score%n == 0):
        y = 10
        figure_add = pygame.transform.scale(coin_image, (50, 50))
        screen.blit(figure_add, (screen_sizeX*(43/64), 2*y))
                           
def show_coin(score):
    if score >= n:
        y = 10
        figure = pygame.transform.scale(coin_image, (20, 20))
        screen.blit(figure, (screen_sizeX*(29/64), 4*y))
        message_display_center(str(coin(score)), font_small, 
                           (255, 255, 0), screen_sizeX*(34/64), 5*y)
                          

# Initialize state
state = 'quit'