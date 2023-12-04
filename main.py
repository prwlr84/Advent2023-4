from input import input_string
from re import sub


def get_score(string):
    cards = []
    score = []
    strings = list(map(lambda x: sub(r'Card\s*\d*:\s*', '', x), string.split('\n')))
    for s in strings:
        if s:
            cards.append(list(map(lambda x: set(x.split()), s.split(' | '))))
    for c in cards:
        match_count = len(c[0].intersection(c[1]))
        if match_count > 0:
            part_score = 1
            for _ in range(match_count - 1):
                part_score *= 2
            score.append(part_score)

    print(sum(score))


def split_card_string(string):
    parts = string.split(': ')
    first_part = parts[0]
    second_parts = parts[1].split(' | ')

    card_id = int(first_part)
    second_list = set([int(num) for num in second_parts[0].split()])
    third_list = set([int(num) for num in second_parts[1].split()])

    return [card_id, second_list, third_list]


def get_cards_count(string):
    cards = []
    count = 0
    strings = list(map(lambda x: sub(r'Card\s*', '', x), string.split('\n')))
    for s in strings:
        if s:
            cards.append(split_card_string(s))

    cards_map = {}
    for index, card in enumerate(cards):
        win_count = card[1].intersection(card[2])
        cards_map[index + 1] = []
        for i in range(1, len(win_count) + 1):
            cards_map[index + 1].append(cards[index + i])

    while len(cards) > 0:
        c = cards.pop()
        count += 1
        cards += cards_map[c[0]]

    print(count)


if __name__ == '__main__':
    get_score(input_string)
    get_cards_count(input_string)
