mounts = {
    'Adamantoise Whistle': 200000,
    'Pod 602 Identification Key': 300000,
    'Archon Throne': 750000,
    'Korpokkur Kolossus Horn': 750000,
    'Typhon Horn': 750000,
    'Fenrir Horn': 1000000,
    'Sabotender Emperador Horn': 2000000,
    'Blackjack Identification Key': 4000000
}

emotes = {
    '/biggrin': 20000,
    'Thav Dance': 80000,
    'Gold Dance': 80000,
    'Bees Knees': 80000,
    '/draw': 100000,
    '/sheathe': 100000
}

minions = {
    'Water Imp': 10000,
    'Zu Hatchling': 10000,
    'Black Coeurl': 20000,
    'Heavy Hatchling': 20000,
    'Wind-Up Nero tol Scaeva': 30000,
    'Piggy': 30000,
    'Unlucky Rabbit': 30000,
    'Mama Automaton': 30000
}

hairstyles = {
    'Pony Tails': 8000,
    'Curls': 9600,
    'Great Lengths': 30000,
    'Lexen Tails': 50000
}

others = {
    'Gambler Barding': 20000,
    'False Spectacles': 100000,
    'Manderville Barding': 150000,
    'Gold Paper Parasol': 200000,
    'Angel Wings': 500000
}

def print_items(item_dict, item_type):
    print(f"{item_type}:\t\tMGP cost")
    print("------------------------------")
    for item, cost in item_dict.items():
        print(f"{item}:\t{cost}")
    print(f"Total {item_type} cost:\t{sum(item_dict.values()):,} MGP\n")

def print_total_cost():
    total_cost = sum(mounts.values()) + sum(emotes.values()) + sum(minions.values()) + sum(hairstyles.values()) + sum(others.values())
    print(f"Grand total: {total_cost:,} MGP\n")

def main():
    print("Gold Saucer Item Lookup")
    print("---------------")
    print("Hello there!\n")
    print("Which would you like to view?")
    print("------------------------------")
    print("Mounts:\t\tDisplays list of mounts and their MGP cost")
    print("Emotes:\t\tDisplays list of emotes and their MGP cost")
    print("Minions:\tDisplays list of minions and their MGP cost")
    print("Hair:\t\tDisplays list of hairstyles and their MGP cost")
    print("Others:\t\tDisplays list of other things and their MGP cost")
    print("Total:\t\tDisplays combined total of all GS items")
    print("Exit:\t\tExit program\n")

    while True:
        user_input = input('Command: ').lower()
        if user_input == 'mounts':
            print_items(mounts, "Mounts")
        elif user_input == 'emotes':
            print_items(emotes, "Emotes")
        elif user_input == 'minions':
            print_items(minions, "Minions")
        elif user_input == 'hair':
            print_items(hairstyles, "Hairstyles")
        elif user_input == 'others':
            print_items(others, "Others")
        elif user_input == 'total':
            print_items(mounts, "Mounts")
            print_items(emotes, "Emotes")
            print_items(minions, "Minions")
            print_items(hairstyles, "Hairstyles")
            print_items(others, "Others")
            print_total_cost()
        elif user_input == 'exit':
            break
        else:
            print('Invalid command\n')

    print('GG, Have Fun farming.')

if __name__ == '__main__':
    main()
