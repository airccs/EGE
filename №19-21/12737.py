def game(s):
    if s >= 98:
        return 0
    game_protivnika = [game(s + 2), game(s + 3), game(2 * s)]
    any_lose = [position for position in game_protivnika if position <= 0]
    if any_lose:

