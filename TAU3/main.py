import random
import pygame

"""
LEGEND:
E - end
S - start
X - empty
B - blocked
P - player
"""


def random_start_stop_placement(board_dim):
    rand_start = random.randint(0, board_dim - 1)
    rand_end = random.randint(0, board_dim - 1)

    start_pos = (0, 0)
    end_pos = (0, 0)

    if rand_start == 0 or rand_start == 4:
        rand_start_y = random.randint(0, board_dim - 1)
        start_pos = (rand_start, rand_start_y)
    else:
        start_pos = (rand_start, 0)

    if rand_end == 0 or rand_end == 4:
        rand_end_y = random.randint(0, board_dim - 1)
        end_pos = (rand_end, rand_end_y)
    else:
        end_pos = (rand_end, 0)

    return start_pos, end_pos


def create_board(board_dim):
    arr1 = []

    for i in range(board_dim):
        row = []
        for j in range(board_dim):
            row.append('X')
        arr1.append(row)

    start_pos, end_pos = random_start_stop_placement(board_dim)
    arr1[start_pos[1]][start_pos[0]] = 'S'
    arr1[end_pos[1]][end_pos[0]] = 'E'

    num_obstacles = 5
    for _ in range(num_obstacles):
        x = random.randint(0, board_dim - 1)
        y = random.randint(0, board_dim - 1)
        if (x, y) not in [start_pos, end_pos]:
            arr1[y][x] = 'B'
        else:
            continue

    return arr1, start_pos, end_pos


def move_player(board, player_pos, direction):
    x, y = player_pos
    new_x, new_y = x, y

    if direction == 'UP' and y > 0 and board[y - 1][x] != 'B':
        new_y -= 1
    elif direction == 'DOWN' and y < len(board) - 1 and board[y + 1][x] != 'B':
        new_y += 1
    elif direction == 'LEFT' and x > 0 and board[y][x - 1] != 'B':
        new_x -= 1
    elif direction == 'RIGHT' and x < len(board[0]) - 1 and board[y][x + 1] != 'B':
        new_x += 1

    if board[new_y][new_x] != 'B':
        if board[y][x] == 'P':
            if board[new_y][new_x] != 'S':
                board[y][x] = 'X'

        return new_x, new_y
    else:
        return x, y


def display_board(screen, board, player_pos):
    screen.fill((255, 255, 255))

    cell_size = 30

    # Draw the board
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == 'S':
                color = (0, 255, 0)
            elif cell == 'E':
                color = (255, 0, 0)
            elif cell == 'B':
                color = (255, 0, 255)
            else:
                color = (0, 0, 0)

            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

    player_x, player_y = player_pos
    player_color = (0, 128, 255)
    pygame.draw.rect(screen, player_color, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))

    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Display Board')

    board_dim = 5
    board, start_pos, end_pos = create_board(board_dim)

    player_pos = start_pos

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_pos = move_player(board, player_pos, 'UP')
                elif event.key == pygame.K_DOWN:
                    player_pos = move_player(board, player_pos, 'DOWN')
                elif event.key == pygame.K_LEFT:
                    player_pos = move_player(board, player_pos, 'LEFT')
                elif event.key == pygame.K_RIGHT:
                    player_pos = move_player(board, player_pos, 'RIGHT')

        display_board(screen, board, player_pos)

        if player_pos == end_pos:
            print("Congratulations! You've reached the end!")
            running = False

    pygame.quit()


if __name__ == "__main__":
    main()
