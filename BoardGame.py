# Homework 3 - Board Game System
# Name: Jaylen Atsou
# Date: April 6, 2026

def loadGameData(filename):
    """Reads game data from a file and returns turn, players, and events."""
    players = {}
    events = {}
    turn = None

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            if line.startswith("Turn:"):
                turn = line.split(":", 1)[1].strip()
            else:
                space, name = line.split(":", 1)
                space = int(space.strip())
                name = name.strip()

                if name.startswith("Player"):
                    players[name] = space
                else:
                    events[space] = name

    return turn, players, events


def displayGame(turn, players, events, board_size=30):
    """Displays the current game state."""
    print("\nCurrent Game State")
    print("------------------")
    print("Current Turn:", turn)
    print()

    for space in range(1, board_size + 1):
        contents = []

        for player, position in players.items():
            if position == space:
                contents.append(player)

        if space in events:
            contents.append(events[space])

        if contents:
            print(f"{space}: " + ", ".join(contents))
        else:
            print(f"{space}: Empty")


def movePlayer(turn, players, events, board_size=30):
    """Moves the current player forward and handles events."""
    if turn not in players:
        print("\nCurrent player not found.")
        return turn

    try:
        move = int(input(f"\nHow many spaces should {turn} move? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return turn

    players[turn] += move

    if players[turn] > board_size:
        players[turn] = board_size

    print(f"\n{turn} moved to space {players[turn]}.")

    if players[turn] in events:
        print(f"{turn} landed on {events[players[turn]]}!")

    player_names = list(players.keys())
    current_index = player_names.index(turn)
    next_index = (current_index + 1) % len(player_names)

    return player_names[next_index]


def saveGameData(filename, turn, players, events):
    """Writes the updated game state back to the file."""
    with open(filename, "w") as file:
        file.write(f"Turn: {turn}\n")

        for player, position in players.items():
            file.write(f"{position}: {player}\n")

        for position, event in events.items():
            file.write(f"{position}: {event}\n")


def main():
    filename = "events.txt"

    turn, players, events = loadGameData(filename)
    displayGame(turn, players, events)

    choice = input("\nMove player? (y/n): ")
    if choice.lower() == "y":
        turn = movePlayer(turn, players, events)
        saveGameData(filename, turn, players, events)

        print("\nUpdated Game State:")
        displayGame(turn, players, events)


if __name__ == "__main__":
    main()