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

test_creature = Creature('Harold', 100, 100, 100)

def setup_ui():
    # initialize Tkinter UI components (labels, buttons, etc.)
    # okay, I'm starting...
    # window:
    window = ttk.Window(themename='solar')
    window.title('My Virtual Buddy')
    window.geometry('500x500')

    # canvas:
    canvas = tk.Canvas(window, width=300, height=300)
    canvas.pack()
    
    # creature
    og_coords = [100, 150, 120, 100, 160, 90, 200, 110, 220, 160, 200, 200, 140, 210, 100, 180]
    creature = canvas.create_polygon(
    og_coords,
    fill="lime", outline="black", smooth=True)
    eye_left = canvas.create_oval(125, 130, 135, 140, fill='black')
    eye_right = canvas.create_oval(165, 130, 175, 140, fill='black')
    eyes = (eye_left, eye_right)

    # virtual buddy methods
    # for animation
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

    # methods for needs (connected to buttons, so they stay here)
    def pet():
        message = test_creature.pet()
        pet_label.config(text=message)
        window.after(3500, lambda: pet_label.config(text=''))
    
    def feed():
        test_creature.feed()
        pet_label.config(text='The blob eats and looks happy.')
        window.after(3500, lambda: pet_label.config(text=''))
    
    def bathroom():
        test_creature.go_to_bathroom()
        pet_label.config(text='The blob went for walkies.\nIt feels much better now (:')
        window.after(3500, lambda: pet_label.config(text=''))
    

    # labels:
    pet_label = tk.Label(window, text='', font=('Courier', 12), height=2)
    pet_label.pack(pady=5)

    feed_label = tk.Label(window, text='', font=('Courier', 12), height=2)
    feed_label.pack(pady=5)

    bathroom_label = tk.Label(window, text='', font=('Courier', 12), height=2)
    bathroom_label.pack(pady=5)

    # horizontal button container
    button_frame = ttk.Frame(window)
    button_frame.pack(pady=10)

    # buttons
    button_pet = ttk.Button(button_frame, text='pet', command=pet)
    button_pet.pack(side='left', padx=10, pady=5)
    button_pet.configure(compound='center', anchor='center')

    button_feed = ttk.Button(button_frame, text='feed', command=feed)
    button_feed.pack(side='left', padx=10)

    button_bathroom = ttk.Button(button_frame, text='bathroom', command=bathroom)
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