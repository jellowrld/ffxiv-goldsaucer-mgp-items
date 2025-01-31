import tkinter as tk
from tkinter import ttk

# Data
ITEMS = {
    "Mounts": {
        'Adamantoise Whistle': 200000, 'Pod 602 Identification Key': 300000, 'Archon Throne': 750000,
        'Korpokkur Kolossus Horn': 750000, 'Typhon Horn': 750000, 'Fenrir Horn': 1000000,
        'Sabotender Emperador Horn': 2000000, 'Blackjack Identification Key': 4000000
    },
    "Emotes": {'/biggrin': 20000, 'Thav Dance': 80000, 'Gold Dance': 80000, '/draw': 100000, '/sheathe': 100000},
    "Minions": {'Water Imp': 10000, 'Zu Hatchling': 10000, 'Black Coeurl': 20000, 'Heavy Hatchling': 20000, 
                'Wind-Up Nero tol Scaeva': 30000, 'Piggy': 30000, 'Unlucky Rabbit': 30000, 'Mama Automaton': 30000},
    "Hairstyles": {'Pony Tails': 8000, 'Curls': 9600, 'Great Lengths': 30000, 'Lexen Tails': 50000},
    "Others": {'Gambler Barding': 20000, 'False Spectacles': 100000, 'Manderville Barding': 150000, 
               'Gold Paper Parasol': 200000, 'Angel Wings': 500000}
}

# GUI functions
def display_items(item_dict, item_type):
    text_area.config(state=tk.NORMAL)
    text_area.delete('1.0', tk.END)
    total_cost = sum(item_dict.values())
    text_area.insert(tk.END, f"{item_type}:\n" + "\n".join(f"{item}: {cost:,} MGP" for item, cost in item_dict.items()))
    text_area.insert(tk.END, f"\nTotal {item_type} cost: {total_cost:,} MGP\n")
    text_area.config(state=tk.DISABLED)

def display_total_cost():
    text_area.config(state=tk.NORMAL)
    text_area.delete('1.0', tk.END)
    total_cost = sum(sum(items.values()) for items in ITEMS.values())
    for category, items in ITEMS.items():
        category_total = sum(items.values())
        text_area.insert(tk.END, f"{category}:\n" + "\n".join(f"{item}: {cost:,} MGP" for item, cost in items.items()))
        text_area.insert(tk.END, f"\nTotal {category} cost: {category_total:,} MGP\n\n")
    text_area.insert(tk.END, f"Grand total: {total_cost:,} MGP\n")
    text_area.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("Gold Saucer Item Lookup")
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Text area for displaying items
text_area = tk.Text(main_frame, wrap='word', width=60, height=20, state=tk.DISABLED)
text_area.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Buttons
buttons = {
    "Mounts": lambda: display_items(ITEMS["Mounts"], "Mounts"),
    "Emotes": lambda: display_items(ITEMS["Emotes"], "Emotes"),
    "Minions": lambda: display_items(ITEMS["Minions"], "Minions"),
    "Hair": lambda: display_items(ITEMS["Hairstyles"], "Hairstyles"),
    "Others": lambda: display_items(ITEMS["Others"], "Others"),
    "Total": display_total_cost,
    "Exit": root.quit
}

for i, (label, command) in enumerate(buttons.items()):
    ttk.Button(main_frame, text=label, command=command).grid(row=1 + i, column=0, columnspan=2, sticky=(tk.W, tk.E))

root.mainloop()
