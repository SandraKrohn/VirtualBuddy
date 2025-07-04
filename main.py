import math
import tkinter as tk
import ttkbootstrap as ttk
from creature import Creature
# from save_manager import load_creature, save_creature
from config import *

"""
starts the app, handles UI and game loop
 - launch Tkinter window
 - create or load a Creature instance
 - build and update GUI
 - set up the game loop using after()
 - connect buttons to creature actions
 - trigger save on exit
 """

test_creature = Creature('Harold', 100, 100)

def setup_ui():
    # initialize Tkinter UI components (labels, buttons, etc.)
    
    # window:
    window = ttk.Window(themename='solar')

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
        show_message('The blob rumbles softly.')
    
    def feed():
        test_creature.feed()
        show_message('The blob eats and looks happy.')
    
    def bathroom():
        test_creature.go_to_bathroom()
        show_message('The blob went for walkies.\nIt feels much better now (:')

    # status
    mood_label = tk.Label(status_frame, text='mood', font=('Courier', 12), height=2)
    mood_label.pack(padx=15, pady=5, anchor='w')
    hunger_label = tk.Label(status_frame, text='hunger', font=('Courier', 12), height=2)
    hunger_label.pack(padx=15, pady=5, anchor='w')
    bathroom_label = tk.Label(status_frame, text='bathroom', font=('Courier', 12), height=2)
    bathroom_label.pack(padx=15, pady=5, anchor='w')
    
    spacer = ttk.Frame(right_frame, height=100)
    spacer.grid(row=2, column=0)

    # horizontal button container
    button_frame = ttk.Frame(right_frame)
    button_frame.grid(row=3, column=0, pady=10)

    # buttons + giving them all the same size
    max_chars = max(len('pet'), len('feed'), len('bathroom'))

    button_pet = ttk.Button(button_frame, text='pet', command=pet)
    button_pet.configure(width=max_chars)
    button_pet.pack(side='left', padx=10, pady=5)

    button_feed = ttk.Button(button_frame, text='feed', command=feed)
    button_feed.configure(width=max_chars)
    button_feed.pack(side='left', padx=10)

    button_bathroom = ttk.Button(button_frame, text='bathroom', command=bathroom)
    button_bathroom.configure(width=max_chars)
    button_bathroom.pack(side='left', padx=10)

    return window

def update_game_loop():
    # periodic update: advance creature state and refresh UI
    pass

def handle_user_action():
    # respond to user input (button press)
    pass

def on_exit():
    # handle cleanup and saving before exit
    pass

def main():
    # main entry point: laod creature, start UI loop
    window = setup_ui()
    window.after(UPDATE_INTERVAL, update_game_loop)
    # this is for later when saving is a thing: window.protocol('WM_DELETE_WINDOW', on_exit)
    window.mainloop()

if __name__ == '__main__':
    main()