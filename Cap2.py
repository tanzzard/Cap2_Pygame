import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
FROG_COLOR = (0, 255, 0)
CAR_COLOR = (255, 0, 0)

# Frog properties
frog_size = 35
frog_x = (SCREEN_WIDTH - frog_size) // 2
frog_y = SCREEN_HEIGHT - frog_size

# Car properties
car_width = 60
car_height = 50
car_x = 0
car_y = 500
car_speed = 0.7

# Second car properties
car2_width = 70
car2_height = 50
car2_x = 0
car2_y = 350
car2_speed = 0.6

# Third car properties
car3_width = 80
car3_height = 45
car3_x = SCREEN_WIDTH - car3_width
car3_y = 430
car3_speed = 0.5

# Turtle properties
turtle_width = 70
turtle_height = 50
turtle_x = SCREEN_WIDTH - turtle_width  # Start from the right side of the screen
turtle_y = 240
turtle_speed = 0.3

# Turtle 2 properties
turtle2_width = 70
turtle2_height = 50
turtle2_x = SCREEN_WIDTH - turtle2_width 
turtle2_y = 120
turtle2_speed = 0.4

# Log properties
log_width = 125
log_height = 25
log_x = SCREEN_WIDTH - log_width # Start from the right side of the screen
log_y = 190
log_speed = 0.2

# Log 2 properties
log2_width = 125
log2_height = 25
log2_x = SCREEN_WIDTH - log2_width
log2_y = 75
log2_speed = 0.3

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger Game")

# Load the car image
car_image = pygame.image.load("Car.png").convert_alpha()
car_image = pygame.transform.scale(car_image, (car_width, car_height)) 
car_image.set_colorkey((0, 0, 0))

# Load the second car image
car2_image = pygame.image.load("Car.2.png").convert_alpha()
car2_image = pygame.transform.scale(car2_image, (car2_width, car2_height)) 
car2_image.set_colorkey((0, 0, 0))

# Load the third car image
car3_image = pygame.image.load("Car.3.png").convert_alpha()
car3_image = pygame.transform.scale(car3_image, (car3_width, car3_height))
car3_image.set_colorkey((0, 0, 0))

# Load the turtle image
turtle_image = pygame.image.load("Turtle.png").convert_alpha()
turtle_image = pygame.transform.scale(turtle_image, (turtle_width, turtle_height)) 
turtle_image.set_colorkey((0, 0, 0))

# Load the turtle 2 image
turtle2_image = pygame.image.load("Turtle.2.png").convert_alpha()
turtle2_image = pygame.transform.scale(turtle2_image, (turtle2_width, turtle2_height))
turtle2_image.set_colorkey((0, 0, 0))

# Load the log image
log_image = pygame.image.load("Log.png").convert_alpha()
log_image = pygame.transform.scale(log_image, (log_width, log_height))
log_image.set_colorkey((0, 0, 0))

# Load the log 2 image
log2_image = pygame.image.load("Log.2.png").convert_alpha()
log2_image =pygame.transform.scale(log2_image, (log2_width, log2_height))
log2_image.set_colorkey((0, 0, 0))

# Load the background image
background_image = pygame.image.load("frogger_background.gif")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the frog image
frog_image = pygame.image.load("Frog.png").convert_alpha()
frog_image = pygame.transform.scale(frog_image, (40, 40)) 
frog_image.set_colorkey((0, 0, 0))

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the fonts
font_title = pygame.font.Font(None, 48)
font_menu = pygame.font.Font(None, 36)

# Set up the menu options
menu_options = ["Start Game", "Instructions", "Quit"]
selected_option = 0

# Load the music file
sound = pygame.mixer.Sound("Music/game.mp3")
sound.play(-1)

# Game loop
running = True
menu_open = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    running = False
                elif selected_option == 1:
                    # Show instructions
                    menu_open = False
                elif selected_option == 2:
                    sys.exit()

    screen.blit(background_image, (0, 0))

    if menu_open:
        # Draw the menu options
        for i, option in enumerate(menu_options):
            if i == selected_option:
                color = WHITE
            else:
                color = BLACK

            text = font_menu.render(option, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + i * 50))
            screen.blit(text, text_rect)
    else:
        # Draw the instructions
        instructions = [
            "Instructions:",
            "Use the arrow keys to move the frog.",
            "Avoid the cars and jump on the logs and turtles to cross the river.",
            "Reach the other side to win the game.",
            "",
            "Press Backspace to go back to the main menu."
        ]
        for i, line in enumerate(instructions):
            text = font_menu.render(line, True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 50))
            screen.blit(text, text_rect)

        # Check if Backspace key is pressed to go back to the main menu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            menu_open = True

    pygame.display.flip()

def game_over_screen():
    running = True
    while running:
        screen.fill(BLACK)
        game_over_text = font_title.render("Game Over", True, WHITE)
        restart_text = font_menu.render("Press R to Restart", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + game_over_text.get_height() // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    running = False

def congratulations_screen():
    running = True
    while running:
        screen.fill(BLACK)
        congrats_text = font_title.render("Congratulations!", True, WHITE)
        restart_text = font_menu.render("Press R to Restart", True, WHITE)
        screen.blit(congrats_text, (SCREEN_WIDTH // 2 - congrats_text.get_width() // 2, SCREEN_HEIGHT // 2 - congrats_text.get_height() // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + congrats_text.get_height() // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    running = False

# Initialize collision flag
collision_occurred = False

# Initialize font
font = pygame.font.Font(None, 36)

# Main game loop
while True:
    running = True
    riding_turtle = False
    riding_log = False
    riding_turtle2 = False
    riding_log2 = False
    jumping = False
    jump_height = 20
    jump_speed = 0.4
    jump_start_y = frog_y
    lives = 3

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and frog_x > 0 and not riding_turtle and not riding_log and not riding_turtle2 and not riding_log2:
            frog_x -= 0.4
        if keys[pygame.K_RIGHT] and frog_x < SCREEN_WIDTH - frog_size and not riding_turtle and not riding_log and not riding_turtle2 and not riding_log2:
            frog_x += 0.4
        if keys[pygame.K_UP] and frog_y > 0 and not jumping:
            jumping = True
        if keys[pygame.K_DOWN] and frog_y < SCREEN_HEIGHT - frog_size:
            frog_y += 0.3

        # Frog jump
        if jumping:
            frog_y -= jump_speed
            if frog_y <= jump_start_y - jump_height:
                jumping = False

        # Move the cars
        car_x += car_speed
        if car_x > SCREEN_WIDTH:
            car_x = -car_width

        car2_x += car2_speed
        if car2_x > SCREEN_WIDTH:
            car2_x = -car2_width

        car3_x -= car3_speed
        if car3_x < -car3_width:
            car3_x = SCREEN_WIDTH

        # Move the turtle
        turtle_x -= turtle_speed  # Decreases the x-coordinate
        if turtle_x < -turtle_width:  # If the turtle has moved off the screen
            turtle_x = SCREEN_WIDTH  # Move it back to the right side of the screen
            if riding_turtle:  # If the frog is riding the turtle, move the frog with the turtle
                frog_x = turtle_x

        # Move the turtle 2
        turtle2_x -= turtle2_speed
        if turtle2_x < -turtle2_width:
            turtle2_x = SCREEN_WIDTH
            if riding_turtle2:
                frog_x = turtle2_x 

        # Move the log
        log_x -= log_speed
        if log_x < -log_width:  # If the log has moved off the screen
            log_x = SCREEN_WIDTH  # Move it back to the right side of the screen
            if riding_log:  # If the frog is riding the log, move the frog with the log
                frog_x = log_x

        # Move the log 2
        log2_x -= log2_speed
        if log2_x < -log2_width:  
            log2_x = SCREEN_WIDTH  
            if riding_log2:  
                frog_x = log2_x     

        # Check for collisions with the first car
        if frog_x + frog_size > car_x and frog_x < car_x + car_width:
            if frog_y + frog_size > car_y and frog_y < car_y + car_height and frog_y > SCREEN_HEIGHT // 2.1:
                if not collision_occurred:
                    print("Collision with car 1! You lost.")
                    lives -= 1
                    collision_occurred = True
                    if lives == 0:
                        game_over_screen()
                        running = False
                    else:
                        # Reset frog position
                        frog_x = (SCREEN_WIDTH - frog_size) // 2
                        frog_y = SCREEN_HEIGHT - frog_size
                        # Reset collision flag
                        collision_occurred = False

        # Check for collisions with the second car
        if frog_x + frog_size > car2_x and frog_x < car2_x + car2_width:
            if frog_y + frog_size > car2_y and frog_y < car2_y + car_height and frog_y > SCREEN_HEIGHT // 2.1:
                if not collision_occurred:
                    print("Collision with car 2! You lost.")
                    lives -= 1
                    collision_occurred = True
                    if lives == 0:
                        game_over_screen()
                        running = False
                    else:
                        # Reset frog position
                        frog_x = (SCREEN_WIDTH - frog_size) // 2
                        frog_y = SCREEN_HEIGHT - frog_size
                        # Reset collision flag
                        collision_occurred = False

        # Check for collisions with the third car
        if frog_x + frog_size > car3_x and frog_x < car3_x + car3_width:
            if frog_y + frog_size > car3_y and frog_y < car3_y + car3_height and frog_y > SCREEN_HEIGHT // 2.1:
                if not collision_occurred:
                    print("Collision with car 3! You lost.")
                    lives -= 1
                    collision_occurred = True
                    if lives == 0:
                        game_over_screen()
                        running = False
                    else:
                        # Reset frog position
                        frog_x = (SCREEN_WIDTH - frog_size) // 2
                        frog_y = SCREEN_HEIGHT - frog_size
                        # Reset collision flag
                        collision_occurred = False

        # Render remaining lives
        lives_text = font.render("Remaining lives: " + str(lives), True, (255, 255, 255))

        # Update the display
        pygame.display.flip()

        # Check for collisions with the turtle
        if frog_x + frog_size > turtle_x and frog_x < turtle_x + turtle_width:
            if frog_y + frog_size > turtle_y and frog_y < turtle_y + turtle_height:
                frog_x = turtle_x # If the frog is on the turtle, make it ride the turtle
                riding_turtle = True
            else:
                riding_turtle = False
        else:
            riding_turtle = False

        # Check for collisions with the turtle 2
        if frog_x + frog_size > turtle2_x and frog_x < turtle2_x + turtle2_width:
            if frog_y + frog_size > turtle2_y and frog_y < turtle2_y + turtle2_height:
                frog_x = turtle2_x
                riding_turtle2 = True
            else:
                riding_turtle2 = False
        else:
            riding_turtle2 = False

        # Check for collisions with the log
        if frog_x + frog_size > log_x and frog_x < log_x + log_width:
            if frog_y + frog_size > log_y and frog_y < log_y + log_height:
                frog_x = log_x # If the frog is on the log, make it ride the log
                riding_log = True
            else:
                riding_log = False
        else:
            riding_log = False

        # Check for collisions with the log 2
        if frog_x + frog_size > log2_x and frog_x < log2_x + log2_width:
            if frog_y + frog_size > log2_y and frog_y < log2_y + log2_height:
                frog_x = log2_x # If the frog is on log 2, make it ride the log 2
                riding_log2 = True
            else:
                riding_log2 = False
        else:
            riding_log2 = False

        # Check if the frog can jump from turtle to log
        if riding_turtle and not riding_log and not riding_turtle2 and not riding_log2:
            if keys[pygame.K_UP] and frog_y > 0 and not jumping:
                jumping = True
                jump_start_y = frog_y
        elif riding_log and not riding_turtle and not riding_turtle2 and not riding_log2:
            if keys[pygame.K_UP] and frog_y > 0 and not jumping:
                jumping = True
                jump_start_y = frog_y

        # Check if the frog can jump from log to turtle 2
        if riding_turtle2 and not riding_log and not riding_turtle and not riding_log2:
            if keys[pygame.K_UP] and frog_y > 0 and not jumping:
                jumping = True
                jump_start_y = frog_y

        # Check if the frog can jump from log to turtle 2
        if riding_log2 and not riding_turtle and not riding_log and not riding_turtle2:
            if keys[pygame.K_UP] and frog_y > 0 and not jumping:
                jumping = True
                jump_start_y = frog_y

        # Check if the frog falls into the water
        if frog_y < SCREEN_HEIGHT // 2.2:
            if not riding_turtle and not riding_log and not riding_turtle2 and not riding_log2:
                print("Frog fell into the water! You have", lives, "lives remaining.")
                lives -= 1
                if lives == 0:
                    game_over_screen()
                    running = False
                else:
                    # Reset frog position
                    frog_x = (SCREEN_WIDTH - frog_size) // 2
                    frog_y = SCREEN_HEIGHT - frog_size
                    # Reset collision flag
                    collision_occurred = False
                    # Reset riding flags
                    riding_turtle = False
                    riding_log = False
                    riding_turtle2 = False
                    riding_log2 = False 

        # Check if the frog is on a safe platform
        if frog_y == SCREEN_HEIGHT - frog_size:
            on_platform = True
        else:
            on_platform = False

        # Check if the frog reaches the exit
        if frog_y < SCREEN_HEIGHT // 14:
            congratulations_screen()
            running = False

        # Clear the screen and draw the background
        screen.fill(BACKGROUND_COLOR)
        screen.blit(background_image, (0, 0))

        # Draw the frog
        screen.blit(frog_image, (frog_x, frog_y))

        # Draw the obstacles
        screen.blit(car_image, (car_x, car_y))
        screen.blit(car2_image, (car2_x, car2_y))
        screen.blit(car3_image, (car3_x, car3_y))
        screen.blit(turtle_image, (turtle_x, turtle_y))
        screen.blit(turtle2_image, (turtle2_x, turtle2_y))
        screen.blit(log_image, (log_x, log_y))
        screen.blit(log2_image, (log2_x, log2_y))
        screen.blit(lives_text, (10, 10))

        # Update the display
        pygame.display.update()

    # Stop the music before exiting the game
    sound.stop()
    
    # Quit Pygame
    pygame.quit()
    sys.exit()


