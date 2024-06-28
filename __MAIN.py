import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")


        # BG Image
        img3 = Image.open(r"D:\Monday HP\facial recognition system HP\photosInGUI\Photography Workshop.png")
        img3 = img3.resize((1280, 720), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1280, height=720)




        # student button
        img4 = Image.open(r"D:\facial recognition system\photosInGUI\studentgrp.jpg")
        img4 = img4.resize((120, 120), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.register)
        b1.place(x=260, y=250, width=120, height=120)

        b1_1 = Button(bg_img, text="Register Here!", cursor="hand2", font=("times new roman", 15), bg="#6f50f8",
                      fg="white")
        b1_1.place(x=260, y=370, width=120, height=40)

        # detect face button
        img5 = Image.open(
            r"D:\facial recognition system\photosInGUI\bigstock-Face-Detection-And-Recognition-194513554.jpg")
        img5 = img5.resize((120, 120), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.attendance)
        b2.place(x=580, y=250, width=120, height=120)

        b2_2 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15), bg="#6f50f8",
                      fg="white")
        b2_2.place(x=580, y=370, width=120, height=40)

        # Attendance button
        img6 = Image.open(r"D:\facial recognition system\photosInGUI\attendance.jpg")
        img6 = img6.resize((120, 120), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendanceReport)
        b3.place(x=900, y=250, width=120, height=120)

        b3_3 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15), bg="#6f50f8", fg="white",
                      command=self.attendanceReport)
        b3_3.place(x=900, y=370, width=120, height=40)


        # train face button
        img8 = Image.open(r"D:\facial recognition system\photosInGUI\train.jfif")
        img8 = img8.resize((120, 120), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_face)
        b5.place(x=260, y=450, width=120, height=120)

        b5_5 = Button(bg_img, text="Train Face", cursor="hand2", font=("times new roman", 15), bg="#6f50f8", fg="white")
        b5_5.place(x=260, y=570, width=120, height=40)

        # Photos button
        img9 = Image.open(r"D:\facial recognition system\photosInGUI\photos.jpg")
        img9 = img9.resize((120, 120), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b6.place(x=580, y=450, width=120, height=120)

        b6_6 = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 15), bg="#6f50f8", fg="white")
        b6_6.place(x=580, y=570, width=120, height=40)



        # Exit button
        img11 = Image.open(r"D:\facial recognition system\photosInGUI\exit.jpeg")
        img11 = img11.resize((120, 120), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b8.place(x=900, y=450, width=120, height=120)

        b8_8 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15), bg="#6f50f8", fg="white")
        b8_8.place(x=900, y=570, width=120, height=40)

    def register(self):
        subprocess.run(['python', 'Register.py'])

    def open_img(self):
        os.startfile("Images")

    def train_face(self):
        subprocess.run(['python', 'Train_Face.py'])

    def attendance(self):
        subprocess.run(['python', 'Attendance.py'])

    def attendanceReport(self):
        subprocess.run(['python', 'attendance_record.py'])

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure to exit the project")
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
