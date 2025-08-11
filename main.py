import math
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import sys
import os
from creature import Creature
# from save_manager import load_creature, save_creature
from config import *
from save_manager import load_creature, save_creature

test_creature = None

def restart(window):
    print("Restarting application...")
    window.destroy()  # close the current window
    python = sys.executable
    os.execl(python, python, *sys.argv)  # re-launch the script with same args

# NEW NEW NEW NEW NEW NEW
def delete_game(window):
    import os
    from config import SAVE_FILE

    # also new, but inside this method (only this if block)
    confirm = messagebox.askyesno('Delete creature', 'Are you sure you want to delete your creature and start over?')
    if not confirm:
        return

    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
        print("Save file deleted. Restarting...")
    else:
        print("No save file to delete.")
    
    restart(window)
    
def setup_ui():
    # initialize Tkinter UI components (labels, buttons, etc.)
    # window:
    window = ttk.Window(themename='solar')
    window.protocol('WM_DELETE_WINDOW', lambda: (on_exit(), window.destroy()))

    window.bind('<r>', lambda event: restart(window))

    # main layout split
    main_frame = ttk.Frame(window)
    main_frame.pack(fill='both', expand=True)

    # left: status bar frame
    status_frame = ttk.Frame(main_frame)
    status_frame.grid(row=0, column=0, sticky='n', padx=10, pady=10)

    # right: canvas, messages, buttons
    right_frame = ttk.Frame(main_frame)
    right_frame.grid(row=0, column=1, sticky='n', padx=10, pady=10)

    window.title('My Virtual Buddy')
    window.geometry('800x800')

    # canvas:
    canvas = tk.Canvas(right_frame, width=400, height=400)
    canvas.grid(row=0, column=0, pady=(10, 0))

    # creature
    x_offset = 100
    og_coords = [x + x_offset if i % 2 == 0 else x for i, x in enumerate([100, 150, 120, 100, 160, 90, 200, 110, 220, 160, 200, 200, 140, 210, 100, 180])]
    creature = canvas.create_polygon(og_coords, fill="lime", outline="black", smooth=True)
    eye_left = canvas.create_oval(125 + x_offset, 130, 135 + x_offset, 140, fill='black')
    eye_right = canvas.create_oval(165 + x_offset, 130, 175 + x_offset, 140, fill='black')
    eyes = (eye_left, eye_right)

    # virtual buddy methods
    # animation
    tick = [0]

    def creature_breathe():
        tick[0] += 1
        new_coords = []

        for i in range(0, len(og_coords), 2):
            x = og_coords[i]
            y = og_coords[i + 1]

            # "pulse" on y-value
            offset = math.sin(tick[0] / 10 + i) * 5
            new_coords.extend([x, y + offset])
        
        canvas.coords(creature, *new_coords)
        window.after(50, creature_breathe)
    
    creature_breathe()

    def creature_blink():
        for eye in eyes:
            canvas.itemconfig(eye, state='hidden')
        window.after(200, creature_unblink)
    
    def creature_unblink():
        for eye in eyes:
            canvas.itemconfig(eye, state='normal')
        window.after(3000, creature_blink)
    
    window.after(3000, creature_blink)

    # message label:
    message_label = tk.Label(right_frame, text='', font=('Courier', 12), height=2)
    message_label.grid(row=1, column=0, pady=10)

    # preventing "needs update" text from disappearing early when button mashing
    message_timer_id = None

    def show_message(text):
        nonlocal message_timer_id
        if message_timer_id is not None:
            window.after_cancel(message_timer_id)
        message_label.config(text=text)
        message_timer_id = window.after(4000, lambda: message_label.config(text=''))

    # methods for needs (connected to buttons, so they stay here)
    def pet():
        test_creature.pet()
        mood_bar['value'] = test_creature.happiness
        show_message(f'{test_creature.name} rumbles softly.')
    
    def feed():
        test_creature.feed()
        show_message(f'{test_creature.name} eats and looks happy.')
    
    def bathroom():
        test_creature.go_to_bathroom()
        show_message(f'{test_creature.name} went for walkies.\nThey feel much better now (:')

    # status
    ttk.Label(status_frame, text='Mood:', font=('Courier', 12)).pack(anchor='w')
    mood_bar = ttk.Progressbar(status_frame, maximum=100, length=200)
    mood_bar.pack(anchor='w', pady=(0, 10))

    ttk.Label(status_frame, text='Hunger:', font=('Courier', 12)).pack(anchor='w')
    hunger_bar = ttk.Progressbar(status_frame, maximum=100, length=200)
    hunger_bar.pack(anchor='w', pady=(0, 10))

    ttk.Label(status_frame, text='Bathroom:', font=('Courier', 12)).pack(anchor='w')
    bathroom_bar = ttk.Progressbar(status_frame, maximum=100, length=200)
    bathroom_bar.pack(anchor='w', pady=(0, 10))

    spacer = ttk.Frame(right_frame, height=100)
    spacer.grid(row=2, column=0)

    # horizontal button container
    button_frame = ttk.Frame(right_frame)
    button_frame.grid(row=3, column=0, pady=10)

    # buttons + giving them all the same size
    max_chars = max(len('pet'), len('feed'), len('bathroom'), len('delete'))

    button_pet = ttk.Button(button_frame, text='pet', command=pet)
    button_pet.configure(width=max_chars)
    button_pet.pack(side='left', padx=10, pady=5)

    button_feed = ttk.Button(button_frame, text='feed', command=feed)
    button_feed.configure(width=max_chars)
    button_feed.pack(side='left', padx=10)

    button_bathroom = ttk.Button(button_frame, text='bathroom', command=bathroom)
    button_bathroom.configure(width=max_chars)
    button_bathroom.pack(side='left', padx=10)

    # NEW NEW NEW NEW NEW NEW
    button_delete = ttk.Button(button_frame, text='DELETE', command=lambda: delete_game(window), bootstyle='danger')
    button_delete.config(width=max_chars)
    button_delete.pack(side='left', padx=10, pady=5)

    return window, hunger_bar, bathroom_bar, mood_bar

# I've already taken care of this tho?
def handle_user_action():
    # respond to user input (button press)
    pass

def on_exit():
    save_creature(test_creature)
    # handle cleanup and saving before exit
    hunger_bar['value'] = max(0, MAX_HUNGER - test_creature.hunger)
    bathroom_bar['value'] = max(0, MAX_BLADDER - test_creature.bathroom)
    # Calculate mood based on needs
    mood_bar['value'] = max(0, test_creature.get_mood_value())

def get_user_name():
    def submit():
        name = entry.get().strip()
        if not name:
            name_var.set('Buddy')
        else:
            name_var.set(name)
        prompt.destroy()

    prompt = tk.Tk()
    name_var = tk.StringVar()
    prompt.title('Name your creature.')
    prompt.geometry('300x150')

    label = tk.Label(prompt, text='Enter your creature\'s name: ')
    label.pack(pady=10)

    entry = tk.Entry(prompt)
    entry.pack()
    entry.focus()
    entry.bind('<Return>', lambda event: submit())

    submit_button = tk.Button(prompt, text='Start', command=submit)
    submit_button.pack()

    prompt.mainloop()
    return name_var.get()

def main():
    global hunger_bar, bathroom_bar, mood_bar
    # name = get_user_name()
    # global test_creature
    # test_creature = Creature(name, 0, 0)
    global test_creature
    test_creature = load_creature()
    if not test_creature:
        name = get_user_name()
        test_creature = Creature(name, 0, 0)
    window, hunger_bar, bathroom_bar, mood_bar = setup_ui()
    window.after(UPDATE_INTERVAL, update_game_loop)
    window.mainloop()

def update_game_loop():
    test_creature.update_needs()

    # update progress bars
    hunger_bar['value'] = 100 - test_creature.hunger
    bathroom_bar['value'] = 100 - test_creature.bathroom
    mood_bar['value'] = test_creature.happiness

    # continue the loop
    hunger_bar.after(UPDATE_INTERVAL, update_game_loop)

if __name__ == '__main__':
    main()