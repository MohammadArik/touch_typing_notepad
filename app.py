from Data import Data
import tkinter as tk
import webbrowser


class App:
    @staticmethod
    def stackoverflow():
        webbrowser.open('https://stackoverflow.com/users/13786395/mohammadarik62')

    @staticmethod
    def youtube():
        webbrowser.open("https://www.youtube.com/channel/UCfdIVBdrbA3D7fUyBtme6xg")

    def __init__(self, geometry):
        master = tk.Tk()
        master.iconbitmap('./images/icon.ico')
        master.geometry(geometry)
        pinky_left = tk.PhotoImage(file='./images/fingers/pinky_left.png')
        pinky_right = tk.PhotoImage(file='./images/fingers/pinky_right.png')
        ring_left = tk.PhotoImage(file='./images/fingers/ring_left.png')
        ring_right = tk.PhotoImage(file='./images/fingers/ring_right.png')
        middle_left = tk.PhotoImage(file='./images/fingers/middle_left.png')
        middle_right = tk.PhotoImage(file='./images/fingers/middle_right.png')
        index_left = tk.PhotoImage(file='./images/fingers/index_left.png')
        index_right = tk.PhotoImage(file='./images/fingers/index_right.png')
        thumbs = tk.PhotoImage(file='./images/fingers/thumb.png')

        Fingers_data = {
            "pinky_left": [pinky_left, 23, 72, "#B2F14D"],
            "pinky_right": [pinky_right, 531, 72, "#B2F14D"],
            "ring_left": [ring_left, 79, 21, "#DB593A"],
            "ring_right": [ring_right, 480, 21, "#DB593A"],
            "middle_left": [middle_left, 130, 5, "#797CB9"],
            "middle_right": [middle_right, 429, 5, "#797CB9"],
            "index_left": [index_left, 182, 44, "#E48827"],
            "index_right": [index_right, 359, 44, "#E48827"],
            "thumbs": [thumbs, 207, 136, "#F171F3"]
        }

        def on_press(event):
            pressed = event.keysym
            out(pressed.lower())

        def out(key):
            obj = tk.Label(frame2, bg=Fingers_data[Data[key][5]][3], text=Data[key][0], padx=Data[key][1],
                           pady=Data[key][2])
            obj.place(x=Data[key][3], y=Data[key][4])

            obj1 = tk.Label(frame1, image=Fingers_data[Data[key][5]][0], bd=0)
            obj1.place(x=Fingers_data[Data[key][5]][1], y=Fingers_data[Data[key][5]][2])
            remove(master, obj, obj1)

        def remove(window, thing, thing1):
            def rem(obj, obj1):
                obj.place_forget()
                obj1.place_forget()

            window.after(500, lambda: rem(thing, thing1))

        self.background = tk.PhotoImage(file="./images/background.png")
        tk.Label(master, bd=0, image=self.background).grid(row=1, column=0, sticky="nsew")

        frame1 = tk.Frame(master, bg="#c2c2a3", width=600, height=300)
        frame1.place(x=680, y=105)

        frame2 = tk.Frame(master, bg="#c2c2a3", width=620, height=230)
        frame2.place(x=420, y=420)

        self.stack_pic = tk.PhotoImage(file='./images/stackoverflow.png')
        tk.Button(master, activebackground="#B041A0", relief="groove", image=self.stack_pic, bg="#B041A0", bd=0,
                  command=lambda: self.stackoverflow()).place(x=16, y=535)
        self.tube_pic = tk.PhotoImage(file='./images/youtube.png')
        tk.Button(master, activebackground="#B041A0", relief="groove", image=self.tube_pic, bd=0, bg="#B341A0",
                  command=lambda: self.youtube()).place(x=16, y=590)

        self.hands = tk.PhotoImage(file='./images/Hands.png')
        tk.Label(frame1, image=self.hands, bd=0).place(x=0, y=0)

        self.keyboard = tk.PhotoImage(file='./images/keyboard.png')
        tk.Label(frame2, image=self.keyboard, bd=0).place(x=0, y=0)

        textbox = tk.Text(master, height=16, width=67)
        textbox.place(x=138, y=105)
        textbox.configure(font=("Calbiri", 11, ""))

        master.bind("<KeyPress>", on_press)
        master.mainloop()


app = App('1280x720+0+30')


