"""Grasp showcase demo."""

from dexterous_hand import Hand


def main() -> None:
    """Run a scripted grasp showcase."""
    hand = Hand.mock()
    for grasp in ["open", "pinch", "cylindrical", "open"]:
        hand.move_to_grasp(grasp)
        print(f"Showing grasp: {grasp}")


if __name__ == "__main__":
    main()
