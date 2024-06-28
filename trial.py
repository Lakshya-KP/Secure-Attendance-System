import tkinter as tk

class RoundedButton(tk.Canvas):
    def __init__(self, parent, bg, fg, width, height, text='', radius=20, borderwidth=2, command=None):
        tk.Canvas.__init__(self, parent, bg=bg, highlightthickness=0, width=width, height=height)

        # Set button properties
        self.fg = fg
        self.radius = radius
        self.borderwidth = borderwidth
        self.command = command

        # Create rounded rectangle background
        self.bg = self.create_rounded_rect(0, 0, width, height, radius, fill=bg, outline=bg)

        # Create text label
        self.text = self.create_text(width/2, height/2, text=text, fill=fg)

        # Bind button click event
        self.bind('<Button-1>', self.on_click)

    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return self.create_polygon(points, **kwargs, smooth=True)

    def on_click(self, event):
        if self.command:
            self.command()

# Create root window
root = tk.Tk()

# Create rounded button
button = RoundedButton(root, bg='gray', fg='white', width=100, height=40, text='Click Me', radius=20, borderwidth=3)
button.pack(pady=10)

# Run the event loop
root.mainloop()
