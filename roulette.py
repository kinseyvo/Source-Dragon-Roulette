import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time
import os

base_dir = os.path.dirname(__file__)
image_dir = os.path.join(base_dir, "Symbols")

source_dragons = [
    ("Balance", os.path.join(image_dir, "balance.png")),
    ("Energy", os.path.join(image_dir, "energy.png")),
    ("Flow", os.path.join(image_dir, "flow.png")),
    ("Focus", os.path.join(image_dir, "focus.png")),
    ("Life", os.path.join(image_dir, "life.png")),
    ("Motion", os.path.join(image_dir, "motion.png")),
    ("Strength", os.path.join(image_dir, "strength.png"))
]

class DragonRoulette:
    def __init__(self, root):
        self.root = root
        self.root.title("Source Dragon Roulette")
        self.root.geometry("400x500")

        # Container frame for vertical layout
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True)

        # Image label
        self.image_label = tk.Label(self.main_frame)
        self.image_label.pack(pady=20)

        # Caption label
        self.caption_label = tk.Label(self.main_frame, text="", font=("Arial", 16))
        self.caption_label.pack(pady=10)

        # Spin button
        self.spin_button = tk.Button(self.main_frame, text="Find your Source Dragon!", command=self.start_spin, font=("Arial", 16), bg="#4CAF50", fg="white")
        self.spin_button.pack(pady=20)

        self.spinning = False
        self.spin_duration = 5000    # 5 seconds in ms
        self.spin_interval = 150     # ms between image changes
        self.start_time = 0

    def start_spin(self):
        if not self.spinning:
            self.spinning = True
            self.start_time = time.time()
            self.spin_animation()

    def spin_animation(self):
        if not self.spinning:
            return

        elapsed_time = (time.time() - self.start_time) * 1000
        name, filename = random.choice(source_dragons)

        if os.path.exists(filename):
            image = Image.open(filename)
            image = image.resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.caption_label.config(text=name)

        if elapsed_time < self.spin_duration:
            self.root.after(self.spin_interval, self.spin_animation)
        else:
            self.spinning = False
            self.highlight_result()

    def highlight_result(self, wiggles=6, distance=10, delay=80):
        # use .place for animation
        self.image_label.pack_forget()
        self.image_label.place(relx=0.5, y=60, anchor="center")

        def wiggle(count):
            if count <= 0:
                self.image_label.place_forget()
                self.image_label.pack(pady=20)
                return
            offset = distance if count % 2 == 0 else -distance
            self.image_label.place_configure(x=offset)
            self.root.after(delay, wiggle, count - 1)

        wiggle(wiggles)

if __name__ == "__main__":
    root = tk.Tk()
    app = DragonRoulette(root)
    root.mainloop()