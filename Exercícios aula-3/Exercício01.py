
import random

def generate_bingo_card():
    numbers = list(range(100))
    random.shuffle(numbers)
    card = [numbers.pop() for _ in range(25)]
    return card

def print_bingo_card(card):
    for gol in range(0, 25, 5):
        print(card[gol:gol+5])

def main():
    num_cards = 5  

    for _ in range(num_cards):
        card = generate_bingo_card()
        print_bingo_card(card)
        print()

if __name__ == "__main__":
    main()
  
