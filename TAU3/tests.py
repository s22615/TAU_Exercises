from main import create_board, move_player

def test_movement():
    board, start_pos, end_pos = create_board(5)

    # Test player movement
    player_pos = start_pos
    player_pos = move_player(board, player_pos, 'DOWN')
    assert player_pos == (start_pos[0], start_pos[1] + 1)

    player_pos = move_player(board, player_pos, 'RIGHT')
    assert player_pos == (start_pos[0] + 1, start_pos[1])

def test_win_condition():
    board, start_pos, end_pos = create_board(5)

    # Move the player to the end point
    player_pos = start_pos
    while player_pos != end_pos:
        player_pos = move_player(board, player_pos, 'DOWN' if player_pos[1] < end_pos[1] else 'RIGHT')

    assert player_pos == end_pos

if __name__ == "__main__":
    test_movement()
    test_win_condition()
    print("Tests passed!")