import tkinter as tk
from tkinter import*
import subprocess
from tkinter import messagebox
import os
from tkinter import filedialog
from PIL import Image,ImageTk
from datetime import datetime
import json
import tkinter.ttk as ttk

class Registration(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration Portal")
        self.geometry("1280x720")

        img = Image.open(r"D:\Monday HP\facial recognition system HP\photosInGUI\register.png")
        img = img.resize((1280, 720), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_label = Label(self, image=self.photoimg)
        f_label.place(relx=0, rely=0)

        self.add_student()
        
    def add_student(self):



        # Add entry widgets for the different fields
        name_label = tk.Label(self, text="Name:", font=("Arial", 16), bg='white')
        name_label.place(relx=0.38, rely=0.2, anchor="center")
        name_entry = tk.Entry(self, font=("Arial", 16))
        name_entry.place(relx=0.5, rely=0.2, anchor="center")

        faculty_label = tk.Label(self, text="Faculty Number:", font=("Arial", 16), bg='white')
        faculty_label.place(relx=0.344, rely=0.25, anchor="center")
        faculty_entry = tk.Entry(self, font=("Arial", 16))
        faculty_entry.place(relx=0.5, rely=0.25, anchor="center")

        major_label = tk.Label(self, text="Major:", font=("Arial", 16), bg='white')
        major_label.place(relx=0.38, rely=0.3, anchor="center")
        major_entry = tk.Entry(self, font=("Arial", 16))
        major_entry.place(relx=0.5, rely=0.3, anchor="center")

        starting_year_label = tk.Label(self, text="Starting Year:", font=("Arial", 16), bg='white')
        starting_year_label.place(relx=0.351, rely=0.35, anchor="center")
        starting_year_entry = tk.Entry(self, font=("Arial", 16))
        starting_year_entry.place(relx=0.5, rely=0.35, anchor="center")

        total_attendance_label = tk.Label(self, text="Total Attendance:", font=("Arial", 16), bg='white')
        total_attendance_label.place(relx=0.34, rely=0.4, anchor="center")
        total_attendance_entry = tk.Entry(self, font=("Arial", 16))
        total_attendance_entry.place(relx=0.5, rely=0.4, anchor="center")

        standing_label = tk.Label(self, text="Standing:", font=("Arial", 16), bg='white')
        standing_label.place(relx=0.369, rely=0.45, anchor="center")
        standing_entry = tk.Entry(self, font=("Arial", 16))
        standing_entry.place(relx=0.5, rely=0.45, anchor="center")

        year_label = tk.Label(self, text="Year:", font=("Arial", 16), bg='white')
        year_label.place(relx=0.38, rely=0.5, anchor="center")
        year_entry = tk.Entry(self, font=("Arial", 16))
        year_entry.place(relx=0.5, rely=0.5, anchor="center")

        def take_image():
            # Open a file dialog to select an image file

            file_path = filedialog.askopenfilename(title="Select Image File", filetypes=(
                ("All files", "*.*"), ("PNG files", "*.png"), ("JPEG files", "*.jpg")))
            # Check if a file was selected
            if file_path:
                # Create a folder to store the images if it doesn't exist
                if not os.path.exists("Images"):
                    os.mkdir("Images")

                # Save the selected image to the images folder with the current date and time as the file name
                img = Image.open(file_path)
                if img.size != (216, 216):
                    img = img.resize((216, 216))
                faculty_number = faculty_entry.get()

                save_path = "Images/"

                img.save(save_path + faculty_number + ".png")

                # with open(image_name, "wb") as f:
                #     with open(file_path, "rb") as f2:
                #         f.write(f2.read())

                # Show a message box with the image file path
                tk.messagebox.showinfo("Image Taken", f"Image taken and saved successfully!")

            else:
                # Show a message box if no file was selected
                tk.messagebox.showerror("Error", "No image file selected")

        # Define a function to be executed when the 'Submit' button is pressed
        def save_student():
            # Get the data from the entry widgets
            # name = name_entry.get()
            faculty_number = faculty_entry.get().upper()
            name = name_entry.get().upper()
            major = major_entry.get()
            starting_year = int(starting_year_entry.get())
            total_attendance = int(total_attendance_entry.get())
            standing = standing_entry.get().upper()
            year = int(year_entry.get())

            last_attendance_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create a dictionary with the data
            student_data = {
                "name": name,
                "major": major,
                "starting_year": starting_year,
                "total_attendance": total_attendance,
                "standing": standing,
                "year": year,
                "last_attendance_time": last_attendance_time
            }

            # Save the data to a JSON file
            with open("students.json", "w") as f:
                f.write('')
                json.dump({faculty_number: student_data}, f)
                f.write('\n')

            subprocess.run(['python', 'AddDataToDatabase.py'])
            tk.messagebox.showinfo("Success", "Student data saved successfully!")

            # Close the window
            self.stop()

        # Insert Image Button
        style = ttk.Style()
        style.configure("RoundedButton.TButton", borderradius=20, foreground="black", bordercolor="black",
                        borderwidth=12, relief="raised", padding=10, font=("Helvetica", 16), width=10)
        image_button = ttk.Button(self, text="Insert Image", command=take_image, style="RoundedButton.TButton")
        image_button.place(relx=0.5, rely=0.55, anchor="center")

        # Add a 'Submit' button
        submit_button = ttk.Button(self, text="Submit", command=save_student, style="RoundedButton.TButton")
        submit_button.place(relx=0.5, rely=0.65, anchor="center")


    def stop(self):
        self.quit()
        self.destroy()

if __name__ == "__main__":
    register = Registration()
    register.mainloop()
    register.stop()