import pygame

board = [" "," "," "," "," "," "," "," "," "]

# Check for a winner
def check_win(board):
    if board[0] != " " and  board[0] == board[1] and board[1] == board[2]:
        outcome = True
    elif board[3] != " " and board[3] == board[4] and board[4] == board[5]:
        outcome = True
    elif board[6] != " " and board[6] == board[7] and board[7] == board[8]:
        outcome = True
    elif board[0] != " " and board[0] == board[3] and board[3] == board[6]:
        outcome = True
    elif board[1] != " " and board[1] == board[4] and board[4] == board[7]:
        outcome = True
    elif board[2] != " " and board[2] == board[5] and board[5] == board[8]:
        outcome = True
    elif board[0] != " " and board[0] == board[4] and board[4] == board[8]:
        outcome = True
    elif board[2] != " " and board[2] == board[4] and board[4] == board[6]:
        outcome = True
    else:
        outcome = False
    return outcome

# If there is a winner
def if_win():
    text_pos_x = 20
    text_pos_y = 580
    pygame.draw.rect(window, bg, (
        text_pos_x,text_pos_y, 500, 50))
    text = font.render("Player " + str(player_move(click_count)) + " wins!!!     Play again?", 1, [0, 0, 0])
    window.blit(text, (text_pos_x, text_pos_y))

pygame.init()
window_w = 530
window_h = 650

border_wid = 20
cell_wid = 150
window = pygame.display.set_mode((window_w,window_h))
pygame.display.set_caption("Noughts and Crosses")
bg = [75,75,76]
window.fill(bg)

click_count = 0

# Draw initial board
all_rects = []
for j in range(3):
    for i in range(3):
        rec = pygame.draw.rect(window, [255,255,255], (border_wid*(i+1) + i*cell_wid, border_wid*(j+1) + j*cell_wid, cell_wid, cell_wid))
        pygame.draw.rect(window, [255, 255, 255], (border_wid * (i + 1) + i * cell_wid, border_wid * (j + 1) + j * cell_wid, cell_wid, cell_wid))
        all_rects.append(rec)

# To reset board
def draw_board():
    all_rects = []
    for j in range(3):
        for i in range(3):
            # Record cell in an array for reference later
            rec = pygame.draw.rect(window, [255, 255, 255], (
            border_wid * (i + 1) + i * cell_wid, border_wid * (j + 1) + j * cell_wid, cell_wid, cell_wid))
            # Draw cell
            pygame.draw.rect(window, [255, 255, 255], (
            border_wid * (i + 1) + i * cell_wid, border_wid * (j + 1) + j * cell_wid, cell_wid, cell_wid))
            all_rects.append(rec)
    return all_rects

# Calculate whos move it is
def player_move(click_count):
    if click_count % 2 == 0:
        player_move = 1
    else:
        player_move = 2
    return player_move

# Re render score
def redraw_score():
    text_pos_x = 20
    text_pos_y = 580
    pygame.draw.rect(window, bg, (
        text_pos_x,text_pos_y, 500, 50))
    text = font.render("Player " + str(player_move(click_count)) + " move:", 1, [0, 0, 0])
    window.blit(text, (text_pos_x, text_pos_y))

# main
running =  True
# Set font
font = pygame.font.SysFont("Arial",30)
redraw_score()
while running:
        pygame.time.delay(100)

        # Check for event
        for event in pygame.event.get():
            # For quit game
            if event.type == pygame.QUIT:
                running = False

            # To reset board
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    all_rects = draw_board()
                    draw_board()
                    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                    click_count = 0
                    redraw_score()

            # To make move
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for item in all_rects:
                    # Check if click was valid and if move is valid
                    if item.collidepoint(event.pos) and board[all_rects.index(item)] == " ":
                        # If player 1
                        if click_count % 2 == 0:
                            # Add x to board
                            board[all_rects.index(item)] = "x"
                            # Add square to screen
                            pygame.draw.circle(window, [0, 0, 0], (item[0] + cell_wid / 2, item[1] + cell_wid / 2), (cell_wid - 50) / 2)
                            pygame.draw.circle(window, [255, 255, 255], (item[0] + cell_wid / 2, item[1] + cell_wid / 2), (cell_wid - 70) / 2)
                        else:
                            board[all_rects.index(item)] = "o"
                            pygame.draw.rect(window, [0, 0, 200], (item[0] + 25, item[1] + 25, cell_wid - 50, cell_wid - 50))
                            pygame.draw.rect(window, [255, 255, 255],(item[0] + 35, item[1] + 35, cell_wid - 70, cell_wid - 70))
                            # Check for a win, if no winner show player who's move
                        if check_win(board):
                            if_win()
                            all_rects = []
                        else:
                            # Increment move
                            click_count += 1
                            redraw_score()

        pygame.display.update()
pygame.quit