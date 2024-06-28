import tkinter as tk
import subprocess
import threading
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Train Face")
        self.geometry("1280x720")
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Text(self, wrap="word", font=("Arial", 12))
        self.text.pack(fill="both", expand=True)

        self.run_encode_generator()

    def run_encode_generator(self):
        self.text.delete(1.0, tk.END) # clear the Text widget
        self.process = subprocess.Popen(["python", "EncodeGenerator.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.thread = threading.Thread(target=self.read_output)
        self.thread.start()

    def read_output(self):
        while True:
            line = self.process.stdout.readline()
            if not line:
                break
            self.text.insert(tk.END, line.decode())

        messagebox.showinfo("Training Done", "Training Done Successfully")
        self.stop()

    def stop(self):
        self.quit()
        self.destroy()

app = App()
app.mainloop()
app.stop()