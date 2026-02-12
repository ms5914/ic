import sys


# +AA
def parse_card(card_str):
    suit = card_str[0]
    letters_part = card_str[1:]
    letter_val = letters_part[0]
    count = len(letters_part)

    return {
        "suit": suit,
        "letter": letter_val,
        "count": count,
        "original": card_str
    }


def is_valid_set(c1, c2, c3):
    properties = ["suit", "letter", "count"]

    for prop in properties:
        val1 = c1[prop]
        val2 = c2[prop]
        val3 = c3[prop]
        unique_values = {val1, val2, val3}
        unique_count = len(unique_values)
        if unique_count == 2:
            return False

    return True


def solve(input_str):
    normalized_input = input_str.replace(',', ' ')
    raw_cards = normalized_input.split()

    cards = [parse_card(c) for c in raw_cards]
    n = len(cards)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if is_valid_set(cards[i], cards[j], cards[k]):
                    return f"{cards[i]['original']} {cards[j]['original']} {cards[k]['original']}"

    return "No valid hand found"

if __name__ == "__main__":
    test_input_1 = "+AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA"
    print(f"Test 1 Result: {solve(test_input_1)}")

    test_input_2 = "-A -B -BB +C -C -CC =CCC"
    print(f"Test 2 Result: {solve(test_input_2)}")

