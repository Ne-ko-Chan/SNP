class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def turn_result(move1, move2) -> int:
    """Returns 1 if p1 wins, 2 if p2 wins,
    0 if it's a tie"""
    match move1:
        case "R":
            match move2:
                case "R":
                    return 0
                case "P":
                    return 2
                case "S":
                    return 1
        case "P":
            match move2:
                case "R":
                    return 1
                case "P":
                    return 0
                case "S":
                    return 2
        case "S":
            match move2:
                case "R":
                    return 2
                case "P":
                    return 1
                case "S":
                    return 0
    raise NoSuchStrategyError


def rps_game_winner(turns: list[list[str]]):
    if len(turns) % 2 != 0:
        raise WrongNumberOfPlayersError
    i = 0
    res = 0
    while i < len(turns) and not res:
        if turns[i][0] != "player1" or turns[i + 1][0] != "player2":
            raise WrongNumberOfPlayersError
        res = turn_result(turns[i][1], turns[i + 1][1])
        i += 2

    return (
        f"player1 {turns[i-2][1]}"
        if res == 1 or res == 0
        else f"player2 {turns[i-1][1]}"
    )


# print(rps_game_winner([["player1", "P"], ["player2", "S"], ["player3", "S"]]))
# print(rps_game_winner([["player1", "P"], ["player2", "A"]]))
print(rps_game_winner([["player1", "P"], ["player2", "S"]]))
print(rps_game_winner([["player1", "P"], ["player2", "P"]]))
