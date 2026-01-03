import random
magic_list_common = []
magic_list_uncommon = []
magic_list_rare = []
magic_list_legendary = []

more_cards = True
end_code = False

def add_cards():
    global more_cards

    rarity_def_call = input("What rarity are you inputing: ").lower()
    number_of_cards = int(input("How many cards in that class do you want to enter?: "))

    if rarity_def_call == "common":
        add_common(number_of_cards)
    elif rarity_def_call == "uncommon":
        add_uncommon(number_of_cards)
    elif rarity_def_call == "rare":
        add_rare(number_of_cards)
    elif rarity_def_call == "legendary":
        add_legendary(number_of_cards)
    else:
        print("input not valid please choose common, uncommon, rare, legendary")
        return

    choice = input("Do you want to add more cards y/n: ").lower()
    if choice == "n":
        more_cards = False


def add_common(number_of_cards):
    for _ in range(number_of_cards):
        new_card = input("please enter card name: ")
        magic_list_common.append(new_card)


def add_uncommon(number_of_cards):
    for _ in range(number_of_cards):
        new_card = input("please enter card name: ")
        magic_list_uncommon.append(new_card)


def add_rare(number_of_cards):
    for _ in range(number_of_cards):
        new_card = input("please enter card name: ")
        magic_list_rare.append(new_card)


def add_legendary(number_of_cards):
    for _ in range(number_of_cards):
        new_card = input("please enter card name: ")
        magic_list_legendary.append(new_card)


import random

def random_card():
    global end_code

    deck_selection = input("Which list are you wanting to pull from: ").lower()
    number_of_cards = int(input("How many cards do you want to randomly select?: "))

    if deck_selection == "common":
        source_list = magic_list_common
    elif deck_selection == "uncommon":
        source_list = magic_list_uncommon
    elif deck_selection == "rare":
        source_list = magic_list_rare
    elif deck_selection == "legendary":
        source_list = magic_list_legendary
    else:
        print("input not valid please choose common, uncommon, rare, legendary")
        return

    if number_of_cards > len(source_list):
        print("Not enough cards in this list.")
        return

    random_list = []
    used_cards = set()   # <- prevents duplicates

    while len(random_list) < number_of_cards:
        rand_card = random.choice(source_list)

        if rand_card not in used_cards:
            random_list.append(rand_card)
            used_cards.add(rand_card)

    print("\n".join(random_list))

    another_go = input("Do you need to pull more cards y/n: ").lower()
    if another_go == "n":
        end_code = True




while more_cards:
    add_cards()
while end_code is False:
    random_card()
