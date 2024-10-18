# create a blackjack game
def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score


def draw_card():
    import random

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


for _ in range(2):
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(draw_card())
        computer_cards.append(draw_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        break

    while input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        user_cards.append(draw_card())
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        if user_score > 21:
            print("You went over. You lose.")
            break

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21:
        print("Computer went over. You win.")
    elif user_score == computer_score:
        print("It's a draw.")
    elif user_score == 0:
        print("You win with a blackjack.")
    elif computer_score == 0:
        print("Computer wins with a blackjack.")
    elif user_score > computer_score:
        print("You win.")
    else:
        print("You lose.")
    print()
