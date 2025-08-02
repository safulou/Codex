import random

FISH_TYPES = [
    ("Salmon", 5),
    ("Tuna", 8),
    ("Trout", 3),
    ("Carp", 4),
]


def cast_line():
    """Simulate casting the fishing line.

    Returns a tuple of (fish_name, weight) if a fish is caught.
    Returns None if no fish is caught.
    """
    # 50% chance to catch a fish
    if random.random() < 0.5:
        return random.choice(FISH_TYPES)
    return None


def main():
    """Run the virtual fishing game."""
    print("Welcome to Virtual Fishing!")
    print("Press Enter to cast your line or type 'quit' to exit.\n")
    total_weight = 0
    catches = []

    while True:
        user_input = input("Cast your line> ").strip().lower()
        if user_input == "quit":
            break

        result = cast_line()
        if result is None:
            print("No luck this time.\n")
        else:
            name, weight = result
            print(f"You caught a {name} weighing {weight} kg!\n")
            total_weight += weight
            catches.append(name)

    print("Thanks for playing!")
    print(f"You caught {len(catches)} fish with a total weight of {total_weight} kg.")
    if catches:
        print("Fish caught: " + ", ".join(catches))


if __name__ == "__main__":
    main()
