from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import os
import subprocess


# Fetch the service account key JSON file contents
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-2a4e2-default-rtdb.firebaseio.com/"
})


class attendance(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Attendance Report")
        self.geometry("1280x720")

        imgBG = Image.open(r"D:\Monday HP\facial recognition system HP\photosInGUI\register.png")
        imgBG = imgBG.resize((1280, 720), Image.ANTIALIAS)
        self.photoimgBG = ImageTk.PhotoImage(imgBG)

        f_label = Label(self, image=self.photoimgBG)
        f_label.place(relx=0, rely=0)

        img = Image.open(r"D:\Monday HP\facial recognition system HP\photosInGUI\downcsv.png")
        img = img.resize((160, 48), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.fun1()

    def fun1(self):

        self.DownBut = ttk.Button(self,image=self.photoimg, text="Download CSV", command=self.get_CSV)
        self.DownBut.place(relx=0.5, rely=0.5, anchor="center")

    def get_CSV(self):
        # Get a database reference to the data you want to retrieve
        ref = db.reference('Students/')

        # Retrieve the data as a dictionary
        data_dict = ref.get()

        # Convert the dictionary to a pandas dataframe
        df = pd.DataFrame.from_dict(data_dict, orient='index')

        # Save the dataframe as a CSV file
        df.to_csv('attendance_report.csv')

        messagebox.showinfo("Done", "attendance_report.csv has been downloaded!")
        # Get the absolute path of the CSV file
        csv_file_path = os.path.abspath("attendance_report.csv")

        # Open the CSV file in Excel
        subprocess.run(["start", "", csv_file_path], shell=True)
        self.stop()

    def stop(self):
        self.quit()
        self.destroy()


# # Get a database reference to the data you want to retrieve
# ref = db.reference('Students/')
#
# # Retrieve the data as a dictionary
# data_dict = ref.get()
#
# # Convert the dictionary to a pandas dataframe
# df = pd.DataFrame.from_dict(data_dict, orient='index')
#
# # Save the dataframe as a CSV file
# df.to_csv('attendance_report.csv')

if __name__ == "__main__":
    att = attendance()
    att.mainloop()
    att.stop()
