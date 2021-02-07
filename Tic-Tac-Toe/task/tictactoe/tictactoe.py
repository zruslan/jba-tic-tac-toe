# write your code here

def has_win_line(char, position):
    win_lines = [0b111000000, 0b000111000, 0b000000111,
                 0b100100100, 0b010010010, 0b001001001,
                 0b100010001, 0b001010100]

    cur_pos = int(''.join(['1' if x == char else '0' for x in position]), 2)
    return any([cur_pos & x == x for x in win_lines])


def index_from_coords(coords):
    return (int(coords[0]) - 1) * 3 + int(coords[1]) - 1


def get_new_position(position, player):
    while True:
        orig = input("Enter the coordinates:").split()
        if not orig[0].isnumeric() or not orig[1].isnumeric():
            print("You should enter numbers!")
        elif not all(x in "123" for x in orig):
            print("Coordinates should be from 1 to 3!")
        else:
            idx = index_from_coords(orig)
            if position[idx] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                position[idx] = player
                return


def print_position(position):
    print("-" * 9)
    print("|", " ".join(list(position[:3])), "|")
    print("|", " ".join(list(position[3:6])), "|")
    print("|", " ".join(list(position[6:])), "|")
    print("-" * 9)


def check_state(position):
    x_has_win_lines = has_win_line('X', position)
    o_has_win_lines = has_win_line('O', position)

    if (abs(grid.count('X') - grid.count('O')) > 1 or
            x_has_win_lines and o_has_win_lines):
        return "Impossible", True
    elif x_has_win_lines:
        return "X wins", True
    elif o_has_win_lines:
        return "O wins", True
    elif grid.count(" ") == 0:
        return "Draw", True
    else:
        return "Game not finished", False


turn = 0
players = "XO"
grid = list(" " * 9)
print_position(grid)

while True:
    get_new_position(grid, players[turn % 2])
    print_position(grid)

    mess, is_finish = check_state(grid)
    if is_finish:
        print(mess)
        break
    turn += 1
